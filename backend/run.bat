@echo off
echo Starting CivicScoop Backend Server...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.7+ from https://python.org
    pause
    exit /b 1
)

REM Check if pip is available
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: pip is not installed
    echo Please install pip or reinstall Python
    pause
    exit /b 1
)

REM Install requirements if they don't exist
if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
)

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Installing/updating dependencies...
pip install -r requirements.txt

REM Initialize database if it doesn't exist
if not exist "civicscoop.db" (
    echo Initializing database...
    python -c "from app import app, db; app.app_context().push(); db.create_all(); print('Database created successfully!')"
)

echo.
echo ================================================
echo CivicScoop Backend Server Starting...
echo ================================================
echo.
echo Dashboard: http://localhost:5000
echo Add Meeting: http://localhost:5000/add_meeting
echo Analytics: http://localhost:5000/analytics
echo API Docs: Check README.md for API endpoints
echo.
echo Press Ctrl+C to stop the server
echo ================================================
echo.

REM Start the Flask application
python app.py

pause