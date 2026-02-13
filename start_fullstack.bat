@echo off
echo 🎯 CrowdGuard-AI Full Stack Launcher
echo ===================================
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo ❌ Virtual environment not found. Creating one...
    python -m venv venv
    call venv\Scripts\activate.bat
    pip install -r requirements.txt
    echo ✅ Virtual environment created and dependencies installed!
)

REM Check if model file exists
if not exist "model\fight_detection_model.h5" (
    echo ❌ Model file not found. Please ensure fight_detection_model.h5 is in the model\ directory.
    pause
    exit /b 1
)

echo ✅ Environment checks passed!
echo 🔄 Starting services...
echo.

REM Start Django backend in background
start "Django Backend" cmd /k "call venv\Scripts\activate.bat && python manage.py runserver 8000"

REM Wait a moment for Django to start
timeout /t 3 /nobreak >nul

REM Start Next.js frontend
cd landing-page-for-security
if not exist "node_modules" (
    echo 📦 Installing Next.js dependencies...
    npm install --legacy-peer-deps
)

echo 🎨 Starting Next.js frontend...
echo.
echo 🌐 Services will be available at:
echo    Django Backend: http://127.0.0.1:8000
echo    Next.js Frontend: http://localhost:3000
echo.
echo Press Ctrl+C to stop both services
echo.

npm run dev
