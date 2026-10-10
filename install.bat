@echo off
REM ===========================================
REM AWESOME-EMU-V1 - Windows Batch Installation
REM ===========================================
REM Author: Ian Carter Kulani
REM Version: 1.0.0

setlocal EnableDelayedExpansion

REM Configuration
set APP_NAME=AWESOME-EMU-V1
set APP_VERSION=1.0.0
set INSTALL_DIR=C:\Program Files\AwesomeEMU
set CONFIG_DIR=C:\ProgramData\AwesomeEMU\config
set LOG_DIR=C:\ProgramData\AwesomeEMU\logs

REM Colors (Windows 10+)
for /F "tokens=1,2 delims=#" %%a in ('"prompt #$H#$E# & echo on & for %%b in (1) do rem"') do set "ESC=%%b"

title %APP_NAME% v%APP_VERSION% - Installation

echo.
echo ================================================================================
echo.
echo     AWESOME-EMU-V1 - Ultimate Cybersecurity Command ^& Control Platform
echo.
echo     Author: Ian Carter Kulani
echo     Version: %APP_VERSION%
echo.
echo ================================================================================
echo.

REM Check for Administrator privileges
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo [ERROR] This script must be run as Administrator
    echo Right-click and select "Run as administrator"
    pause
    exit /b 1
)

echo [INFO] Running with Administrator privileges
echo.

REM Check Python
echo [INFO] Checking Python installation...
python --version >nul 2>&1
if %errorLevel% neq 0 (
    echo [ERROR] Python is not installed or not in PATH
    echo Please install Python 3.7+ from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo [INFO] Found Python %PYTHON_VERSION%

REM Check pip
echo [INFO] Checking pip...
pip --version >nul 2>&1
if %errorLevel% neq 0 (
    echo [ERROR] pip is not installed
    echo Please install pip: python -m ensurepip --upgrade
    pause
    exit /b 1
)
echo [INFO] pip is available

REM Create directories
echo.
echo [INFO] Creating directories...
if not exist "%INSTALL_DIR%" mkdir "%INSTALL_DIR%"
if not exist "%CONFIG_DIR%" mkdir "%CONFIG_DIR%"
if not exist "%LOG_DIR%" mkdir "%LOG_DIR%"
if not exist "%INSTALL_DIR%\reports" mkdir "%INSTALL_DIR%\reports"
if not exist "%INSTALL_DIR%\payloads" mkdir "%INSTALL_DIR%\payloads"
if not exist "%INSTALL_DIR%\scans" mkdir "%INSTALL_DIR%\scans"
if not exist "%INSTALL_DIR%\wordlists" mkdir "%INSTALL_DIR%\wordlists"
echo [SUCCESS] Directories created

REM Install Python dependencies
echo.
echo [INFO] Installing Python dependencies...
python -m pip install --upgrade pip setuptools wheel
if exist "requirements.txt" (
    python -m pip install -r requirements.txt
) else (
    echo [ERROR] requirements.txt not found!
    pause
    exit /b 1
)
echo [SUCCESS] Python dependencies installed

REM Copy application files
echo.
echo [INFO] Copying application files...
copy /Y *.py "%INSTALL_DIR%\" >nul 2>&1
if exist config xcopy /E /I /Y config "%INSTALL_DIR%\config" >nul 2>&1
if exist templates xcopy /E /I /Y templates "%INSTALL_DIR%\templates" >nul 2>&1
if exist wordlists xcopy /E /I /Y wordlists "%INSTALL_DIR%\wordlists" >nul 2>&1
copy /Y requirements.txt "%INSTALL_DIR%\" >nul 2>&1
copy /Y README.md "%INSTALL_DIR%\" >nul 2>&1
copy /Y LICENSE "%INSTALL_DIR%\" >nul 2>&1
echo [SUCCESS] Application files copied

REM Create configuration
echo.
echo [INFO] Creating default configuration...
(
echo {
echo     "version": "1.0.0",
echo     "auto_start": false,
echo     "auto_block_enabled": false,
echo     "scan_timeout": 30,
echo     "web": {
echo         "enabled": true,
echo         "port": 5000,
echo         "host": "0.0.0.0"
echo     }
echo }
) > "%CONFIG_DIR%\config.json"
echo [SUCCESS] Configuration created

REM Create CLI wrapper
echo.
echo [INFO] Creating CLI wrapper...
(
echo @echo off
echo cd /d "%INSTALL_DIR%"
echo python awesome_emu.py %%*
) > "%INSTALL_DIR%\awesome-emu.bat"

REM Add to PATH
setx PATH "%PATH%;%INSTALL_DIR%" /M >nul 2>&1
echo [SUCCESS] CLI wrapper created

REM Create Windows Service (using NSSM if available)
echo.
echo [INFO] Checking for NSSM (Non-Sucking Service Manager)...
where nssm >nul 2>&1
if %errorLevel% equ 0 (
    echo [INFO] NSSM found, creating service...
    nssm install AwesomeEMU "%INSTALL_DIR%\awesome-emu.bat"
    nssm set AwesomeEMU DisplayName "AWESOME-EMU-V1"
    nssm set AwesomeEMU Description "Ultimate Cybersecurity Command ^& Control Platform"
    nssm set AwesomeEMU Start SERVICE_AUTO_START
    echo [SUCCESS] Windows service created
) else (
    echo [WARN] NSSM not found. Service not created.
    echo Download from https://nssm.cc/download to install as service
)

REM Create firewall rules
echo.
echo [INFO] Creating firewall rules...
netsh advfirewall firewall add rule name="AWESOME-EMU Web Dashboard" dir=in action=allow protocol=TCP localport=5000 >nul 2>&1
netsh advfirewall firewall add rule name="AWESOME-EMU Phishing Server" dir=in action=allow protocol=TCP localport=8080 >nul 2>&1
netsh advfirewall firewall add rule name="AWESOME-EMU C2 Server" dir=in action=allow protocol=TCP localport=4444 >nul 2>&1
netsh advfirewall firewall add rule name="AWESOME-EMU Agent Listener" dir=in action=allow protocol=TCP localport=5555 >nul 2>&1
echo [SUCCESS] Firewall rules created

REM Create desktop shortcut
echo.
echo [INFO] Creating desktop shortcut...
powershell -Command "$WS = New-Object -ComObject WScript.Shell; $SC = $WS.CreateShortcut('%USERPROFILE%\Desktop\AWESOME-EMU.lnk'); $SC.TargetPath = '%INSTALL_DIR%\awesome-emu.bat'; $SC.WorkingDirectory = '%INSTALL_DIR%'; $SC.Description = 'AWESOME-EMU-V1 Cyber Platform'; $SC.Save()"
echo [SUCCESS] Desktop shortcut created

REM Installation complete
echo.
echo ================================================================================
echo.
echo                         INSTALLATION COMPLETE
echo.
echo ================================================================================
echo.
echo Installation Directory: %INSTALL_DIR%
echo Configuration Directory: %CONFIG_DIR%
echo Log Directory: %LOG_DIR%
echo.
echo Usage:
echo   awesome-emu                    - Start AWESOME-EMU
echo   %INSTALL_DIR%\awesome-emu.bat  - Start from installation directory
echo.
echo Web Dashboard:
echo   http://localhost:5000
echo.
echo For authorized security testing only
echo.

REM Ask to start
set /p START_NOW="Start AWESOME-EMU now? (y/n): "
if /i "%START_NOW%"=="y" (
    cd /d "%INSTALL_DIR%"
    python awesome_emu.py
)

pause
endlocal
