#!/bin/bash
# ===========================================
# AWESOME-EMU-V1 - Bash Installation Script
# ===========================================
# Author: Ian Carter Kulani
# Version: 1.0.0

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
NC='\033[0m'

# Configuration
APP_NAME="AWESOME-EMU-V1"
APP_VERSION="1.0.0"
INSTALL_DIR="/opt/awesome-emu"
CONFIG_DIR="/etc/awesome-emu"
LOG_DIR="/var/log/awesome-emu"
BIN_DIR="/usr/local/bin"
SERVICE_NAME="awesome-emu"

# Functions
print_banner() {
    echo -e "${WHITE}"
    echo "╔══════════════════════════════════════════════════════════════════════════════╗"
    echo "║                                                                              ║"
    echo "║    █████╗ ██╗    ██╗███████╗███████╗ ██████╗ ███╗   ███╗███████╗             ║"
    echo "║   ██╔══██╗██║    ██║██╔════╝██╔════╝██╔═══██╗████╗ ████║██╔════╝             ║"
    echo "║   ███████║██║ █╗ ██║█████╗  ███████╗██║   ██║██╔████╔██║█████╗               ║"
    echo "║   ██╔══██║██║███╗██║██╔══╝  ╚════██║██║   ██║██║╚██╔╝██║██╔══╝               ║"
    echo "║   ██║  ██║╚███╔███╔╝███████╗███████║╚██████╔╝██║ ╚═╝ ██║███████╗             ║"
    echo "║   ╚═╝  ╚═╝ ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝             ║"
    echo "║                                                                              ║"
    echo "║                    AWESOME-EMU-V1 - Installation Script                      ║"
    echo "║                         Author: Ian Carter Kulani                            ║"
    echo "║                              Version: ${APP_VERSION}                                  ║"
    echo "║                                                                              ║"
    echo "╚══════════════════════════════════════════════════════════════════════════════╝"
    echo -e "${NC}"
}

log_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

check_root() {
    if [[ $EUID -ne 0 ]]; then
        log_error "This script must be run as root (use sudo)"
        exit 1
    fi
}

detect_os() {
    if [[ -f /etc/os-release ]]; then
        . /etc/os-release
        OS=$ID
        VER=$VERSION_ID
    elif [[ -f /etc/debian_version ]]; then
        OS="debian"
    elif [[ -f /etc/redhat-release ]]; then
        OS="rhel"
    elif [[ -f /etc/arch-release ]]; then
        OS="arch"
    elif [[ -f /etc/alpine-release ]]; then
        OS="alpine"
    else
        OS=$(uname -s)
    fi
    log_info "Detected OS: $OS"
}

install_dependencies() {
    log_info "Installing system dependencies..."
    
    case $OS in
        ubuntu|debian)
            apt-get update
            apt-get install -y \
                python3 python3-pip python3-dev python3-venv \
                build-essential libssl-dev libffi-dev \
                nmap traceroute mtr-tiny netcat-openbsd \
                dnsutils whois curl wget git \
                libpcap-dev tcpdump \
                iproute2 iptables iputils-ping \
                arping fping hping3 socat \
                openssh-client openssl ca-certificates \
                sqlite3 libsqlite3-dev \
                libjpeg-dev zlib1g-dev
            ;;
        centos|rhel|fedora)
            yum install -y epel-release
            yum install -y \
                python3 python3-pip python3-devel \
                gcc gcc-c++ make openssl-devel libffi-devel \
                nmap traceroute mtr nc \
                bind-utils whois curl wget git \
                libpcap-devel tcpdump \
                iproute iptables iputils \
                arping fping hping3 socat \
                openssh-clients openssl ca-certificates \
                sqlite sqlite-devel \
                libjpeg-turbo-devel zlib-devel
            ;;
        arch)
            pacman -Sy --noconfirm \
                python python-pip \
                base-devel openssl libffi \
                nmap traceroute mtr gnu-netcat \
                bind whois curl wget git \
                libpcap tcpdump \
                iproute2 iptables iputils \
                arping fping hping socat \
                openssh openssl ca-certificates \
                sqlite
            ;;
        alpine)
            apk update
            apk add --no-cache \
                python3 py3-pip python3-dev \
                build-base openssl-dev libffi-dev \
                nmap nmap-scripts traceroute mtr \
                netcat-openbsd bind-tools whois \
                curl wget git \
                libpcap-dev tcpdump \
                iproute2 iptables iputils \
                arping fping hping3 socat \
                openssh-client openssl ca-certificates \
                sqlite sqlite-dev \
                jpeg-dev zlib-dev
            ;;
        *)
            log_warn "Unknown OS: $OS. Please install dependencies manually."
            ;;
    esac
    
    log_success "System dependencies installed"
}

install_python_deps() {
    log_info "Installing Python dependencies..."
    
    pip3 install --upgrade pip setuptools wheel
    
    if [[ -f "requirements.txt" ]]; then
        pip3 install -r requirements.txt
    else
        log_error "requirements.txt not found!"
        exit 1
    fi
    
    log_success "Python dependencies installed"
}

create_directories() {
    log_info "Creating directories..."
    
    mkdir -p "$INSTALL_DIR"
    mkdir -p "$CONFIG_DIR"
    mkdir -p "$LOG_DIR"
    mkdir -p "$INSTALL_DIR/reports"
    mkdir -p "$INSTALL_DIR/payloads"
    mkdir -p "$INSTALL_DIR/scans"
    mkdir -p "$INSTALL_DIR/wordlists"
    mkdir -p "$INSTALL_DIR/templates"
    mkdir -p "$INSTALL_DIR/agents"
    mkdir -p "$INSTALL_DIR/c2_logs"
    
    log_success "Directories created"
}

copy_files() {
    log_info "Copying application files..."
    
    # Copy Python files
    cp -r *.py "$INSTALL_DIR/" 2>/dev/null || true
    cp -r config "$INSTALL_DIR/" 2>/dev/null || true
    cp -r templates "$INSTALL_DIR/" 2>/dev/null || true
    cp -r wordlists "$INSTALL_DIR/" 2>/dev/null || true
    cp requirements.txt "$INSTALL_DIR/" 2>/dev/null || true
    cp README.md "$INSTALL_DIR/" 2>/dev/null || true
    cp LICENSE "$INSTALL_DIR/" 2>/dev/null || true
    
    chmod +x "$INSTALL_DIR"/*.py 2>/dev/null || true
    
    log_success "Application files copied"
}

create_config() {
    log_info "Creating default configuration..."
    
    cat > "$CONFIG_DIR/config.json" << 'EOF'
{
    "version": "1.0.0",
    "auto_start": false,
    "auto_block_enabled": false,
    "auto_block_threshold": 5,
    "scan_timeout": 30,
    "report_format": "both",
    "generate_graphics": true,
    "web": {
        "enabled": true,
        "port": 5000,
        "host": "0.0.0.0"
    },
    "monitoring": {
        "enabled": true,
        "port_scan_threshold": 10,
        "syn_flood_threshold": 100
    }
}
EOF
    
    chmod 600 "$CONFIG_DIR/config.json"
    log_success "Configuration created"
}

create_service() {
    log_info "Creating systemd service..."
    
    cat > "/etc/systemd/system/${SERVICE_NAME}.service" << EOF
[Unit]
Description=AWESOME-EMU-V1 - Ultimate Cybersecurity Command & Control Platform
Documentation=https://github.com/iancarterkulani/awesome-emu
After=network.target network-online.target
Wants=network-online.target

[Service]
Type=simple
User=root
Group=root
WorkingDirectory=${INSTALL_DIR}
Environment="PYTHONUNBUFFERED=1"
Environment="AWESOME_EMU_CONFIG=${CONFIG_DIR}"
ExecStart=/usr/bin/python3 ${INSTALL_DIR}/awesome_emu.py
ExecReload=/bin/kill -HUP \$MAINPID
Restart=on-failure
RestartSec=5
StandardOutput=journal
StandardError=journal
SyslogIdentifier=awesome-emu

# Security hardening
NoNewPrivileges=true
ProtectSystem=strict
ProtectHome=true
ReadWritePaths=${INSTALL_DIR} ${LOG_DIR} ${CONFIG_DIR}
PrivateTmp=true

# Capabilities
AmbientCapabilities=CAP_NET_ADMIN CAP_NET_RAW CAP_SYS_ADMIN
CapabilityBoundingSet=CAP_NET_ADMIN CAP_NET_RAW CAP_SYS_ADMIN

[Install]
WantedBy=multi-user.target
EOF

    systemctl daemon-reload
    log_success "Systemd service created"
}

create_cli() {
    log_info "Creating CLI wrapper..."
    
    cat > "${BIN_DIR}/awesome-emu" << EOF
#!/bin/bash
# AWESOME-EMU-V1 CLI Wrapper
cd ${INSTALL_DIR}
exec python3 ${INSTALL_DIR}/awesome_emu.py "\$@"
EOF

    chmod +x "${BIN_DIR}/awesome-emu"
    log_success "CLI wrapper created"
}

setup_firewall() {
    log_info "Configuring firewall rules..."
    
    if command -v ufw &> /dev/null; then
        ufw allow 5000/tcp comment "AWESOME-EMU Web Dashboard"
        ufw allow 8080/tcp comment "AWESOME-EMU Phishing Server"
        ufw allow 4444/tcp comment "AWESOME-EMU C2 Server"
        ufw allow 5555/tcp comment "AWESOME-EMU Agent Listener"
    elif command -v firewall-cmd &> /dev/null; then
        firewall-cmd --permanent --add-port=5000/tcp
        firewall-cmd --permanent --add-port=8080/tcp
        firewall-cmd --permanent --add-port=4444/tcp
        firewall-cmd --permanent --add-port=5555/tcp
        firewall-cmd --reload
    elif command -v iptables &> /dev/null; then
        iptables -A INPUT -p tcp --dport 5000 -j ACCEPT
        iptables -A INPUT -p tcp --dport 8080 -j ACCEPT
        iptables -A INPUT -p tcp --dport 4444 -j ACCEPT
        iptables -A INPUT -p tcp --dport 5555 -j ACCEPT
    fi
    
    log_success "Firewall rules configured"
}

print_summary() {
    echo ""
    echo -e "${WHITE}╔══════════════════════════════════════════════════════════════════════════════╗"
    echo -e "║                    ${GREEN}INSTALLATION COMPLETE${WHITE}                                    ║"
    echo -e "╚══════════════════════════════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo -e "${CYAN}Installation Directory:${NC} $INSTALL_DIR"
    echo -e "${CYAN}Configuration Directory:${NC} $CONFIG_DIR"
    echo -e "${CYAN}Log Directory:${NC} $LOG_DIR"
    echo ""
    echo -e "${WHITE}Usage:${NC}"
    echo -e "  ${GREEN}awesome-emu${NC}                    - Start AWESOME-EMU"
    echo -e "  ${GREEN}systemctl start awesome-emu${NC}   - Start as service"
    echo -e "  ${GREEN}systemctl stop awesome-emu${NC}    - Stop service"
    echo -e "  ${GREEN}systemctl status awesome-emu${NC}  - Check status"
    echo ""
    echo -e "${WHITE}Web Dashboard:${NC}"
    echo -e "  ${GREEN}http://localhost:5000${NC}"
    echo ""
    echo -e "${YELLOW}⚠️  For authorized security testing only${NC}"
    echo ""
}

# Main installation
main() {
    print_banner
    
    check_root
    detect_os
    
    echo ""
    log_info "Starting installation of ${APP_NAME} v${APP_VERSION}..."
    echo ""
    
    install_dependencies
    install_python_deps
    create_directories
    copy_files
    create_config
    create_service
    create_cli
    setup_firewall
    
    print_summary
}

# Run main
main "$@"
