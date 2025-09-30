@echo off
setlocal enabledelayedexpansion

REM Get the script directory
set "SCRIPT_DIR=%~dp0"
set "SCRIPT_DIR=%SCRIPT_DIR:~0,-1%"
set "SESSION_DIR=%SCRIPT_DIR%\session"
set "SRC_DIR=%SCRIPT_DIR%\src"
set "BACKUP_DIR=%SCRIPT_DIR%\backup"

REM Check if session directory exists
if not exist "%SESSION_DIR%" (
    echo Error: Session directory '%SESSION_DIR%' does not exist.
    exit /b 1
)

REM Check if src directory exists
if not exist "%SRC_DIR%" (
    echo Error: Source directory '%SRC_DIR%' does not exist.
    exit /b 1
)

REM Create backup directory if it doesn't exist
if not exist "%BACKUP_DIR%" mkdir "%BACKUP_DIR%"

REM Get available sessions
set "count=0"
for /d %%d in ("%SESSION_DIR%\*") do (
    set /a count+=1
    set "session[!count!]=%%~nxd"
)

REM Check if any sessions exist
if %count%==0 (
    echo No sessions found in '%SESSION_DIR%'.
    exit /b 1
)

REM Display available sessions
echo What session would you like to load?
echo.
for /l %%i in (1,1,%count%) do (
    echo %%i. Session !session[%%i]!
)
echo.

REM Get user choice
:get_choice
set /p choice="Enter your choice (1-%count%): "

REM Validate input
set "valid=0"
for /l %%i in (1,1,%count%) do (
    if "%choice%"=="%%i" set "valid=1"
)

if %valid%==0 (
    echo Invalid choice. Please enter a number between 1 and %count%.
    goto get_choice
)

set "selected_session=!session[%choice%]!"

echo.
echo Selected session: %selected_session%
echo.

REM Generate timestamp for backup filename
for /f "tokens=2 delims==" %%I in ('wmic os get localdatetime /value') do set datetime=%%I
set "timestamp=%datetime:~0,4%-%datetime:~4,2%-%datetime:~6,2%-%datetime:~8,2%-%datetime:~10,2%-%datetime:~12,2%"
set "backup_filename=src-%timestamp%.zip"
set "backup_path=%BACKUP_DIR%\%backup_filename%"

REM Create backup of current src directory using PowerShell
echo Creating backup of current src directory...
powershell -command "Compress-Archive -Path '%SRC_DIR%\*' -DestinationPath '%backup_path%' -Force" 2>nul
if exist "%backup_path%" (
    echo Backup created: %backup_filename%
) else (
    echo Warning: Could not create backup.
)

REM Clear src directory by file extensions and support directories
echo Clearing src directory (preserving .gitkeep)...
del /s /q "%SRC_DIR%\*.py" 2>nul
del /s /q "%SRC_DIR%\*.md" 2>nul
del /s /q "%SRC_DIR%\*.ini" 2>nul
if exist "%SRC_DIR%\support\" rmdir /s /q "%SRC_DIR%\support" 2>nul

REM Copy session content to src directory
set "session_path=%SESSION_DIR%\%selected_session%"
echo Loading session %selected_session%...

xcopy "%session_path%\*" "%SRC_DIR%\" /e /i /y /q >nul 2>&1
if %errorlevel%==0 (
    echo Session %selected_session% loaded successfully!
) else (
    echo Warning: Session %selected_session% directory may be empty or copy failed.
)

echo.
echo Operation completed!
echo - Backup saved to: backup\%backup_filename%
echo - Session %selected_session% loaded into src directory

endlocal