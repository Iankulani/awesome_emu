# ===========================================
# AWESOME-EMU-V1 - PowerShell Installation
# ===========================================
# Author: Ian Carter Kulani
# Version: 1.0.0

#Requires -RunAsAdministrator

param(
    [switch]$Uninstall,
    [switch]$Force,
    [string]$InstallDir = "$env:ProgramFiles\AwesomeEMU",
    [string]$ConfigDir = "$env:ProgramData\AwesomeEMU\config",
    [string]$LogDir = "$env:ProgramData\AwesomeEMU\logs"
)

# Configuration
$AppName = "AWESOME-EMU-V1"
$AppVersion = "1.0.0"
$ServiceName = "AwesomeEMU"
$RepoUrl = "https://github.com/iancarterkulani/awesome-emu"

# Functions
function Write-Banner {
    Clear-Host
    Write-Host @"
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║    █████╗ ██╗    ██╗███████╗███████╗ ██████╗ ███╗   ███╗███████╗             ║
║   ██╔══██╗██║    ██║██╔════╝██╔════╝██╔═══██╗████╗ ████║██╔════╝             ║
║   ███████║██║ █╗ ██║█████╗  ███████╗██║   ██║██╔████╔██║█████╗               ║
║   ██╔══██║██║███╗██║██╔══╝  ╚════██║██║   ██║██║╚██╔╝██║██╔══╝               ║
║   ██║  ██║╚███╔███╔╝███████╗███████║╚██████╔╝██║ ╚═╝ ██║███████╗             ║
║   ╚═╝  ╚═╝ ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝             ║
║                                                                              ║
║                    AWESOME-EMU-V1 - Installation Script                      ║
║                         Author: Ian Carter Kulani                            ║
║                              Version: $AppVersion                                  ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
"@ -ForegroundColor White
}

function Write-Info {
    param([string]$Message)
    Write-Host "[INFO] " -ForegroundColor Green -NoNewline
    Write-Host $Message
}

function Write-Warn {
    param([string]$Message)
    Write-Host "[WARN] " -ForegroundColor Yellow -NoNewline
    Write-Host $Message
}

function Write-Err {
    param([string]$Message)
    Write-Host "[ERROR] " -ForegroundColor Red -NoNewline
    Write-Host $Message
}

function Write-Success {
    param([string]$Message)
    Write-Host "[SUCCESS] " -ForegroundColor Green -NoNewline
    Write-Host $Message
}

function Test-Python {
    Write-Info "Checking Python installation..."
    
    try {
        $pythonVersion = python --version 2>&1
        if ($pythonVersion -match "Python (\d+\.\d+\.\d+)") {
            $version = [Version]$Matches[1]
            if ($version -ge [Version]"3.7.0") {
                Write-Success "Found Python $version"
                return $true
            } else {
                Write-Err "Python 3.7+ required. Found $version"
                return $false
            }
        }
    } catch {
        Write-Err "Python not found. Please install from https://www.python.org/downloads/"
        return $false
    }
}

function Test-Pip {
    Write-Info "Checking pip..."
    
    try {
        $pipVersion = pip --version 2>&1
        Write-Success "Found pip"
        return $true
    } catch {
        Write-Err "pip not found. Installing..."
        python -m ensurepip --upgrade
        return $?
    }
}

function Install-SystemDependencies {
    Write-Info "Installing system dependencies..."
    
    # Check if Chocolatey is installed
    $choco = Get-Command choco -ErrorAction SilentlyContinue
    
    if ($choco) {
        Write-Info "Installing dependencies via Chocolatey..."
        choco install -y python3 nmap curl wget git wireshark openssh 2>&1 | Out-Null
    } else {
        Write-Warn "Chocolatey not found. Some dependencies may need manual installation."
        Write-Warn "Install from https://chocolatey.org/install"
    }
    
    Write-Success "System dependencies installed"
}

function Install-PythonDependencies {
    Write-Info "Installing Python dependencies..."
    
    python -m pip install --upgrade pip setuptools wheel
    
    $reqFile = Join-Path $PSScriptRoot "requirements.txt"
    if (Test-Path $reqFile) {
        python -m pip install -r $reqFile
    } else {
        Write-Err "requirements.txt not found!"
        exit 1
    }
    
    Write-Success "Python dependencies installed"
}

function Create-Directories {
    Write-Info "Creating directories..."
    
    $dirs = @(
        $InstallDir,
        $ConfigDir,
        $LogDir,
        (Join-Path $InstallDir "reports"),
        (Join-Path $InstallDir "payloads"),
        (Join-Path $InstallDir "scans"),
        (Join-Path $InstallDir "wordlists"),
        (Join-Path $InstallDir "templates"),
        (Join-Path $InstallDir "agents"),
        (Join-Path $InstallDir "c2_logs")
    )
    
    foreach ($dir in $dirs) {
        if (-not (Test-Path $dir)) {
            New-Item -ItemType Directory -Path $dir -Force | Out-Null
        }
    }
    
    Write-Success "Directories created"
}

function Copy-ApplicationFiles {
    Write-Info "Copying application files..."
    
    Copy-Item -Path "*.py" -Destination $InstallDir -Force -ErrorAction SilentlyContinue
    Copy-Item -Path "config" -Destination $InstallDir -Recurse -Force -ErrorAction SilentlyContinue
    Copy-Item -Path "templates" -Destination $InstallDir -Recurse -Force -ErrorAction SilentlyContinue
    Copy-Item -Path "wordlists" -Destination $InstallDir -Recurse -Force -ErrorAction SilentlyContinue
    Copy-Item -Path "requirements.txt" -Destination $InstallDir -Force -ErrorAction SilentlyContinue
    Copy-Item -Path "README.md" -Destination $InstallDir -Force -ErrorAction SilentlyContinue
    Copy-Item -Path "LICENSE" -Destination $InstallDir -Force -ErrorAction SilentlyContinue
    
    Write-Success "Application files copied"
}

function Create-Configuration {
    Write-Info "Creating default configuration..."
    
    $config = @{
        version = $AppVersion
        auto_start = $false
        auto_block_enabled = $false
        scan_timeout = 30
        web = @{
            enabled = $true
            port = 5000
            host = "0.0.0.0"
        }
        monitoring = @{
            enabled = $true
            port_scan_threshold = 10
            syn_flood_threshold = 100
        }
    }
    
    $configPath = Join-Path $ConfigDir "config.json"
    $config | ConvertTo-Json -Depth 10 | Set-Content -Path $configPath
    
    Write-Success "Configuration created"
}

function Create-Service {
    Write-Info "Creating Windows service..."
    
    # Check for NSSM
    $nssm = Get-Command nssm -ErrorAction SilentlyContinue
    
    if ($nssm) {
        nssm install $ServiceName "$InstallDir\awesome-emu.bat"
        nssm set $ServiceName DisplayName $AppName
        nssm set $ServiceName Description "Ultimate Cybersecurity Command & Control Platform"
        nssm set $ServiceName Start SERVICE_AUTO_START
        Write-Success "Windows service created"
    } else {
        Write-Warn "NSSM not found. Service not created."
        Write-Warn "Download from https://nssm.cc/download"
    }
}

function Create-CLIWrapper {
    Write-Info "Creating CLI wrapper..."
    
    $wrapperPath = Join-Path $InstallDir "awesome-emu.bat"
    @"
@echo off
cd /d "$InstallDir"
python awesome_emu.py %*
"@ | Set-Content -Path $wrapperPath
    
    # Add to PATH
    $currentPath = [Environment]::GetEnvironmentVariable("Path", "Machine")
    if ($currentPath -notlike "*$InstallDir*") {
        [Environment]::SetEnvironmentVariable("Path", "$currentPath;$InstallDir", "Machine")
    }
    
    Write-Success "CLI wrapper created"
}

function Create-FirewallRules {
    Write-Info "Creating firewall rules..."
    
    $ports = @(5000, 8080, 4444, 5555)
    $names = @("Web Dashboard", "Phishing Server", "C2 Server", "Agent Listener")
    
    for ($i = 0; $i -lt $ports.Count; $i++) {
        $existing = Get-NetFirewallRule -DisplayName "AWESOME-EMU $($names[$i])" -ErrorAction SilentlyContinue
        if (-not $existing) {
            New-NetFirewallRule -DisplayName "AWESOME-EMU $($names[$i])" `
                -Direction Inbound -Action Allow -Protocol TCP -LocalPort $ports[$i]
        }
    }
    
    Write-Success "Firewall rules created"
}

function Create-Shortcut {
    Write-Info "Creating desktop shortcut..."
    
    $WshShell = New-Object -ComObject WScript.Shell
    $Shortcut = $WshShell.CreateShortcut("$env:USERPROFILE\Desktop\AWESOME-EMU.lnk")
    $Shortcut.TargetPath = "$InstallDir\awesome-emu.bat"
    $Shortcut.WorkingDirectory = $InstallDir
    $Shortcut.Description = "AWESOME-EMU-V1 Cyber Platform"
    $Shortcut.Save()
    
    Write-Success "Desktop shortcut created"
}

function Uninstall-AwesomeEmu {
    Write-Info "Uninstalling $AppName..."
    
    # Stop and remove service
    $service = Get-Service -Name $ServiceName -ErrorAction SilentlyContinue
    if ($service) {
        Stop-Service -Name $ServiceName -Force -ErrorAction SilentlyContinue
        $nssm = Get-Command nssm -ErrorAction SilentlyContinue
        if ($nssm) {
            nssm remove $ServiceName confirm
        }
    }
    
    # Remove firewall rules
    $rules = Get-NetFirewallRule -DisplayName "AWESOME-EMU*" -ErrorAction SilentlyContinue
    foreach ($rule in $rules) {
        Remove-NetFirewallRule -DisplayName $rule.DisplayName -ErrorAction SilentlyContinue
    }
    
    # Remove desktop shortcut
    Remove-Item "$env:USERPROFILE\Desktop\AWESOME-EMU.lnk" -Force -ErrorAction SilentlyContinue
    
    # Ask about data directories
    if (-not $Force) {
        $removeData = Read-Host "Remove application data? (y/n)"
        if ($removeData -eq "y") {
            Remove-Item $InstallDir -Recurse -Force -ErrorAction SilentlyContinue
            Remove-Item $ConfigDir -Recurse -Force -ErrorAction SilentlyContinue
            Remove-Item $LogDir -Recurse -Force -ErrorAction SilentlyContinue
        }
    } else {
        Remove-Item $InstallDir -Recurse -Force -ErrorAction SilentlyContinue
        Remove-Item $ConfigDir -Recurse -Force -ErrorAction SilentlyContinue
        Remove-Item $LogDir -Recurse -Force -ErrorAction SilentlyContinue
    }
    
    Write-Success "Uninstallation complete"
}

function Show-Summary {
    Write-Host ""
    Write-Host "╔══════════════════════════════════════════════════════════════════════════════╗"
    Write-Host "║                    " -NoNewline
    Write-Host "INSTALLATION COMPLETE" -ForegroundColor Green -NoNewline
    Write-Host "                                    ║"
    Write-Host "╚══════════════════════════════════════════════════════════════════════════════╝"
    Write-Host ""
    Write-Host "Installation Directory: " -ForegroundColor Cyan -NoNewline
    Write-Host $InstallDir
    Write-Host "Configuration Directory: " -ForegroundColor Cyan -NoNewline
    Write-Host $ConfigDir
    Write-Host "Log Directory: " -ForegroundColor Cyan -NoNewline
    Write-Host $LogDir
    Write-Host ""
    Write-Host "Usage:" -ForegroundColor White
    Write-Host "  awesome-emu                    - Start AWESOME-EMU"
    Write-Host "  Start-Service AwesomeEMU       - Start as service"
    Write-Host "  Stop-Service AwesomeEMU        - Stop service"
    Write-Host "  Get-Service AwesomeEMU         - Check status"
    Write-Host ""
    Write-Host "Web Dashboard:" -ForegroundColor White
    Write-Host "  http://localhost:5000" -ForegroundColor Green
    Write-Host ""
    Write-Host "⚠️  For authorized security testing only" -ForegroundColor Yellow
    Write-Host ""
}

# Main installation
function Main {
    Write-Banner
    
    if ($Uninstall) {
        Uninstall-AwesomeEmu
        return
    }
    
    Write-Info "Starting installation of $AppName v$AppVersion..."
    Write-Host ""
    
    if (-not (Test-Python)) {
        exit 1
    }
    
    if (-not (Test-Pip)) {
        exit 1
    }
    
    Install-SystemDependencies
    Install-PythonDependencies
    Create-Directories
    Copy-ApplicationFiles
    Create-Configuration
    Create-CLIWrapper
    Create-Service
    Create-FirewallRules
    Create-Shortcut
    
    Show-Summary
    
    $startNow = Read-Host "Start AWESOME-EMU now? (y/n)"
    if ($startNow -eq "y") {
        Set-Location $InstallDir
        python awesome_emu.py
    }
}

# Run main
Main
