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

:: Kiểm tra và thông báo nếu không có Python
(
    where python >nul 2>&1
    if %errorLevel% neq 0 (
        python --version >nul 2>&1
        if %errorLevel% neq 0 (
            echo Python is not installed. Please download and install Python from:
            echo https://www.python.org/downloads/
            pause
            exit /b 1
        )
    )
) || (
    echo Python is not installed. Please download and install Python from:
    echo https://www.python.org/downloads/
    pause
    exit /b 1
)

:: Tạo thư mục trong Program Files
set "install_dir=%ProgramFiles%\error-to-chatgpt"
if not exist "%install_dir%" (
    mkdir "%install_dir%" 2>nul
)

:: Copy script vào thư mục cài đặt
copy "%~dp0error_to_chatgpt.py" "%install_dir%" /Y

:: Tạo file batch cho lệnh 'eo'
(
    echo @echo off
    echo python "%install_dir%\error_to_chatgpt.py" %%*
) > "%install_dir%\eo.bat"

:: Tạo file batch cho lệnh 'eoo'
(
    echo @echo off
    echo python "%install_dir%\error_to_chatgpt.py" eoo %%*
) > "%install_dir%\eoo.bat"

:: Thêm thư mục vào PATH nếu chưa có
set "batch_path=%install_dir%"
for %%i in ("%PATH:;=";"%") do (
    if "%%~i"=="%batch_path%" set "found_path=true"
)
if not defined found_path (
    echo Adding %install_dir% to PATH...
    setx /M PATH "%PATH%;%install_dir%"
)

echo Installation completed successfully.
echo Please restart your command prompt to use 'eo' and 'eoo' commands.
pause
