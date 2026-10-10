#!/usr/bin/env python3
"""
===========================================
AWESOME-EMU-V1 - Requirements Checker
===========================================
Author: Ian Carter Kulani
Version: 1.0.0

This module checks all dependencies and requirements
"""

import os
import sys
import subprocess
import shutil
import platform
import importlib
from typing import Dict, List, Tuple, Optional

# Colors for output
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    RESET = '\033[0m'


def print_banner():
    """Print checker banner"""
    banner = f"""
{Colors.WHITE}╔══════════════════════════════════════════════════════════════════════════════╗
║{Colors.CYAN}           AWESOME-EMU-V1 - Requirements Checker                           {Colors.WHITE}║
║{Colors.CYAN}                    Author: Ian Carter Kulani                             {Colors.WHITE}║
╚══════════════════════════════════════════════════════════════════════════════╝{Colors.RESET}
"""
    print(banner)


def check_python_version() -> Tuple[bool, str]:
    """Check Python version"""
    version = sys.version_info
    if version >= (3, 7):
        return True, f"Python {version.major}.{version.minor}.{version.micro}"
    return False, f"Python {version.major}.{version.minor}.{version.micro} (3.7+ required)"


def check_system_tools() -> Dict[str, bool]:
    """Check system tools"""
    tools = {
        'python3': 'Python 3',
        'pip3': 'Package installer',
        'git': 'Version control',
        'curl': 'HTTP client',
        'wget': 'File downloader',
        'nmap': 'Network scanner',
        'ping': 'Network ping',
        'traceroute': 'Network tracer',
        'nc': 'Netcat',
        'dig': 'DNS lookup',
        'whois': 'WHOIS lookup',
        'ssh': 'SSH client',
        'openssl': 'SSL toolkit',
        'docker': 'Container platform',
        'hashcat': 'Password cracker',
        'signal-cli': 'Signal messenger'
    }
    
    results = {}
    for tool, description in tools.items():
        results[tool] = shutil.which(tool) is not None
    
    return results


def check_python_packages() -> Dict[str, Tuple[bool, str]]:
    """Check Python packages"""
    packages = {
        # Core
        'requests': '2.31.0',
        'urllib3': '2.0.0',
        'certifi': '2023.7.22',
        
        # System
        'psutil': '5.9.5',
        
        # Crypto
        'cryptography': '41.0.0',
        
        # SSH
        'paramiko': '3.3.0',
        
        # Discord
        'discord': '2.3.0',
        
        # Telegram
        'telethon': '1.29.0',
        
        # Slack
        'slack_sdk': '3.23.0',
        
        # Web
        'flask': '2.3.0',
        'flask_socketio': '5.3.0',
        'flask_cors': '4.0.0',
        
        # Google
        'google.oauth2': '2.23.0',
        'googleapiclient': '2.100.0',
        
        # Selenium
        'selenium': '4.14.0',
        
        # Scapy
        'scapy': '2.5.0',
        
        # WHOIS
        'whois': '0.8.0',
        
        # QR Code
        'qrcode': '7.4.0',
        'PIL': '10.0.0',
        
        # URL Shortening
        'pyshorteners': '1.0.1',
        
        # Visualization
        'matplotlib': '3.7.0',
        'seaborn': '0.12.0',
        'numpy': '1.24.0',
        
        # PDF
        'reportlab': '4.0.0',
        
        # Keylogger
        'pynput': '1.7.6',
        'pyperclip': '1.8.2',
        'pyautogui': '0.9.54',
        
        # DNS
        'dns': '2.4.0',
        
        # HTML
        'bs4': '4.12.0',
        'lxml': '4.9.0'
    }
    
    results = {}
    for package, min_version in packages.items():
        try:
            module = importlib.import_module(package)
            version = getattr(module, '__version__', 'unknown')
            results[package] = (True, version)
        except ImportError:
            results[package] = (False, 'Not installed')
        except Exception as e:
            results[package] = (False, str(e))
    
    return results


def check_network_connectivity() -> Dict[str, bool]:
    """Check network connectivity"""
    results = {}
    
    # Check DNS
    try:
        import socket
        socket.gethostbyname('google.com')
        results['dns'] = True
    except:
        results['dns'] = False
    
    # Check HTTP
    try:
        import urllib.request
        urllib.request.urlopen('http://httpbin.org/get', timeout=5)
        results['http'] = True
    except:
        results['http'] = False
    
    # Check HTTPS
    try:
        import urllib.request
        urllib.request.urlopen('https://httpbin.org/get', timeout=5)
        results['https'] = True
    except:
        results['https'] = False
    
    # Check ICMP
    try:
        if platform.system().lower() == 'windows':
            subprocess.run(['ping', '-n', '1', '8.8.8.8'], capture_output=True, timeout=5)
        else:
            subprocess.run(['ping', '-c', '1', '8.8.8.8'], capture_output=True, timeout=5)
        results['icmp'] = True
    except:
        results['icmp'] = False
    
    return results


def check_permissions() -> Dict[str, bool]:
    """Check system permissions"""
    results = {}
    
    # Check admin/root
    if platform.system().lower() == 'windows':
        try:
            import ctypes
            results['admin'] = ctypes.windll.shell32.IsUserAnAdmin() != 0
        except:
            results['admin'] = False
    else:
        results['admin'] = os.geteuid() == 0
    
    # Check write permissions
    results['write_config'] = os.access('.', os.W_OK)
    results['write_temp'] = os.access('/tmp' if platform.system() != 'Windows' else os.environ.get('TEMP', '.'), os.W_OK)
    
    # Check network capabilities
    if platform.system().lower() == 'linux':
        results['raw_socket'] = os.geteuid() == 0
        results['iptables'] = shutil.which('iptables') is not None
    else:
        results['raw_socket'] = results['admin']
        results['iptables'] = False
    
    return results


def check_directory_structure() -> Dict[str, bool]:
    """Check directory structure"""
    dirs = {
        '.awesome_emu_v1': 'Main config directory',
        '.awesome_emu_v1/payloads': 'Payloads directory',
        '.awesome_emu_v1/scans': 'Scan results directory',
        '.awesome_emu_v1/phishing_pages': 'Phishing pages directory',
        '.awesome_emu_v1/wordlists': 'Wordlists directory',
        '.awesome_emu_v1/agents': 'Agents directory',
        '.awesome_emu_v1/c2_logs': 'C2 logs directory',
        'awesome_emu_reports': 'Reports directory',
        'awesome_emu_reports/pdf_reports': 'PDF reports directory'
    }
    
    results = {}
    for dir_path, description in dirs.items():
        results[dir_path] = os.path.isdir(dir_path)
    
    return results


def check_file_permissions() -> Dict[str, Tuple[bool, str]]:
    """Check file permissions"""
    files = {
        'awesome_emu.py': 'Main application',
        'requirements.txt': 'Dependencies list',
        'README.md': 'Documentation',
        'LICENSE': 'License file'
    }
    
    results = {}
    for file_path, description in files.items():
        if os.path.exists(file_path):
            readable = os.access(file_path, os.R_OK)
            results[file_path] = (True, f"{'✅' if readable else '❌'} Readable")
        else:
            results[file_path] = (False, '❌ Not found')
    
    return results


def print_results(title: str, results: Dict, show_details: bool = True):
    """Print check results"""
    print(f"\n{Colors.BOLD}{Colors.CYAN}{title}{Colors.RESET}")
    print(f"{Colors.WHITE}{'='*60}{Colors.RESET}")
    
    for key, value in results.items():
        if isinstance(value, tuple):
            success, detail = value
        elif isinstance(value, dict):
            success = value.get('success', False)
            detail = value.get('detail', '')
        else:
            success = bool(value)
            detail = ''
        
        status = f"{Colors.GREEN}✅{Colors.RESET}" if success else f"{Colors.RED}❌{Colors.RESET}"
        print(f"  {status} {key}: {detail}")
    
    print()


def generate_report() -> Dict:
    """Generate full report"""
    report = {
        'python': check_python_version(),
        'system_tools': check_system_tools(),
        'python_packages': check_python_packages(),
        'network': check_network_connectivity(),
        'permissions': check_permissions(),
        'directories': check_directory_structure(),
        'files': check_file_permissions()
    }
    
    return report


def print_summary(report: Dict):
    """Print summary"""
    print(f"\n{Colors.BOLD}{Colors.WHITE}{'='*60}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}📊 SUMMARY{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.WHITE}{'='*60}{Colors.RESET}")
    
    # Python
    py_ok, py_version = report['python']
    print(f"  Python: {py_version} {'✅' if py_ok else '❌'}")
    
    # System tools
    tools = report['system_tools']
    tools_ok = sum(1 for v in tools.values() if v)
    tools_total = len(tools)
    print(f"  System Tools: {tools_ok}/{tools_total} {'✅' if tools_ok == tools_total else '⚠️'}")
    
    # Python packages
    packages = report['python_packages']
    packages_ok = sum(1 for v in packages.values() if v[0])
    packages_total = len(packages)
    print(f"  Python Packages: {packages_ok}/{packages_total} {'✅' if packages_ok == packages_total else '⚠️'}")
    
    # Network
    network = report['network']
    network_ok = sum(1 for v in network.values() if v)
    network_total = len(network)
    print(f"  Network: {network_ok}/{network_total} {'✅' if network_ok == network_total else '⚠️'}")
    
    # Permissions
    perms = report['permissions']
    perms_ok = sum(1 for v in perms.values() if v)
    perms_total = len(perms)
    print(f"  Permissions: {perms_ok}/{perms_total} {'✅' if perms_ok == perms_total else '⚠️'}")
    
    # Directories
    dirs = report['directories']
    dirs_ok = sum(1 for v in dirs.values() if v)
    dirs_total = len(dirs)
    print(f"  Directories: {dirs_ok}/{dirs_total} {'✅' if dirs_ok == dirs_total else '⚠️'}")
    
    print(f"{Colors.BOLD}{Colors.WHITE}{'='*60}{Colors.RESET}\n")


def fix_missing_requirements(report: Dict):
    """Attempt to fix missing requirements"""
    print(f"\n{Colors.BOLD}{Colors.YELLOW}🔧 Attempting to fix missing requirements...{Colors.RESET}\n")
    
    # Install missing Python packages
    missing_packages = [
        package for package, (success, _) in report['python_packages'].items()
        if not success
    ]
    
    if missing_packages:
        print(f"{Colors.YELLOW}Missing packages: {', '.join(missing_packages)}{Colors.RESET}")
        install = input(f"{Colors.WHITE}Install missing packages? (y/n): {Colors.RESET}").strip().lower()
        
        if install == 'y':
            try:
                subprocess.run([sys.executable, '-m', 'pip', 'install'] + missing_packages)
                print(f"{Colors.GREEN}✅ Packages installed{Colors.RESET}")
            except Exception as e:
                print(f"{Colors.RED}❌ Failed to install: {e}{Colors.RESET}")
    
    # Create missing directories
    missing_dirs = [
        dir_path for dir_path, success in report['directories'].items()
        if not success
    ]
    
    if missing_dirs:
        print(f"\n{Colors.YELLOW}Creating missing directories...{Colors.RESET}")
        for dir_path in missing_dirs:
            try:
                os.makedirs(dir_path, exist_ok=True)
                print(f"  ✅ Created: {dir_path}")
            except Exception as e:
                print(f"  ❌ Failed: {dir_path} - {e}")
    
    print(f"\n{Colors.GREEN}✅ Fix attempt complete{Colors.RESET}")


def main():
    """Main function"""
    print_banner()
    
    # Generate report
    print(f"{Colors.WHITE}🔍 Checking system requirements...{Colors.RESET}\n")
    
    report = generate_report()
    
    # Print detailed results
    py_ok, py_version = report['python']
    print_results("Python Version", {'Python': (py_ok, py_version)})
    
    print_results("System Tools", report['system_tools'])
    
    # Only show missing Python packages
    missing_packages = {
        k: v for k, v in report['python_packages'].items() if not v[0]
    }
    if missing_packages:
        print_results("Missing Python Packages", missing_packages)
    else:
        print(f"{Colors.GREEN}✅ All Python packages installed{Colors.RESET}\n")
    
    print_results("Network Connectivity", report['network'])
    print_results("Permissions", report['permissions'])
    print_results("Directory Structure", report['directories'])
    
    # Print summary
    print_summary(report)
    
    # Check if fix is needed
    all_ok = (
        py_ok and
        all(report['system_tools'].values()) and
        all(v[0] for v in report['python_packages'].values()) and
        all(report['directories'].values())
    )
    
    if not all_ok:
        fix = input(f"{Colors.WHITE}Attempt to fix missing requirements? (y/n): {Colors.RESET}").strip().lower()
        if fix == 'y':
            fix_missing_requirements(report)
    
    # Final status
    print(f"\n{Colors.BOLD}{Colors.WHITE}{'='*60}{Colors.RESET}")
    if all_ok:
        print(f"{Colors.GREEN}✅ All requirements satisfied!{Colors.RESET}")
    else:
        print(f"{Colors.YELLOW}⚠️ Some requirements need attention{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.WHITE}{'='*60}{Colors.RESET}\n")
    
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
