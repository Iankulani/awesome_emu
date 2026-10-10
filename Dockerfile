# ===========================================
# AWESOME-EMU-V1 - Dockerfile (Alpine)
# ===========================================
FROM alpine:3.18

LABEL maintainer="Ian Carter Kulani"
LABEL description="AWESOME-EMU-V1 - Ultimate Cybersecurity Command & Control Platform"
LABEL version="1.0.0"

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    AWESOME_EMU_HOME=/opt/awesome-emu \
    AWESOME_EMU_CONFIG=/opt/awesome-emu/config

# Install system dependencies
RUN apk update && apk upgrade && \
    apk add --no-cache \
    python3 \
    py3-pip \
    py3-setuptools \
    py3-wheel \
    py3-cryptography \
    py3-numpy \
    py3-pillow \
    bash \
    curl \
    wget \
    git \
    nmap \
    nmap-scripts \
    traceroute \
    mtr \
    netcat-openbsd \
    bind-tools \
    whois \
    openssh-client \
    openssl \
    ca-certificates \
    tzdata \
    gcc \
    musl-dev \
    python3-dev \
    libffi-dev \
    openssl-dev \
    make \
    cmake \
    g++ \
    linux-headers \
    libpcap-dev \
    tcpdump \
    iproute2 \
    iptables \
    iputils \
    arping \
    fping \
    hping3 \
    socat \
    proxychains-ng \
    && rm -rf /var/cache/apk/*

# Create application directory
RUN mkdir -p ${AWESOME_EMU_HOME} && \
    mkdir -p ${AWESOME_EMU_CONFIG} && \
    mkdir -p /opt/awesome-emu/logs && \
    mkdir -p /opt/awesome-emu/reports && \
    mkdir -p /opt/awesome-emu/payloads && \
    mkdir -p /opt/awesome-emu/scans && \
    mkdir -p /opt/awesome-emu/wordlists

# Set working directory
WORKDIR ${AWESOME_EMU_HOME}

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt

# Copy application files
COPY awesome_emu.py .
COPY *.py ./
COPY config/ ./config/
COPY wordlists/ ./wordlists/ 2>/dev/null || true
COPY templates/ ./templates/ 2>/dev/null || true

# Create non-root user
RUN addgroup -S awesome && \
    adduser -S awesome -G awesome && \
    chown -R awesome:awesome ${AWESOME_EMU_HOME}

# Switch to non-root user
USER awesome

# Expose ports
EXPOSE 5000 8080 4444 5555

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python3 -c "import sys; sys.exit(0)" || exit 1

# Default command
ENTRYPOINT ["python3", "awesome_emu.py"]
CMD ["--help"]
