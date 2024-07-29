@echo off
setlocal enabledelayedexpansion

:: Kiểm tra quyền admin
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo This script requires administrator privileges.
    echo Please run this script as an administrator.
    pause
    exit /b 1
)

:: Cài đặt Python nếu chưa có
where python >nul 2>&1
if %errorLevel% neq 0 (
    echo Python is not installed. Installing Python...
    powershell -Command "Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.9.7/python-3.9.7-amd64.exe -OutFile python-installer.exe"
    python-installer.exe /quiet InstallAllUsers=1 PrependPath=1
    del python-installer.exe
)

:: Cài đặt pyperclip
pip install pyperclip

:: Tạo thư mục trong Program Files
set "install_dir=%ProgramFiles%\error-to-chatgpt"
mkdir "%install_dir%" 2>nul

:: Copy script vào thư mục cài đặt
copy "%~dp0error_to_chatgpt.py" "%install_dir%"

:: Tạo file batch cho lệnh 'eo' và 'eoo'
(
    echo @echo off
    echo python "%install_dir%\error_to_chatgpt.py" %%*
) > "%install_dir%\eo.bat"

copy "%install_dir%\eo.bat" "%install_dir%\eoo.bat"

:: Thêm thư mục vào PATH
for /f "tokens=2*" %%a in ('reg query "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v Path') do set "current_path=%%b"
setx /M PATH "%current_path%;%install_dir%"

echo Installation completed successfully.
echo Please restart your command prompt to use 'eo' and 'eoo' commands.
pause