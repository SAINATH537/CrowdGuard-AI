#!/usr/bin/env python3
"""
CrowdGuard-AI Full Stack Launcher
Runs Django backend and Next.js frontend concurrently
"""
import os
import sys
import subprocess
import threading
import time
from pathlib import Path

def run_django():
    """Run Django backend server"""
    print("🚀 Starting Django backend on http://127.0.0.1:8000")
    os.chdir(Path(__file__).parent)
    
    # Activate virtual environment and run Django
    if os.name == 'nt':  # Windows
        venv_python = Path(__file__).parent / 'venv' / 'Scripts' / 'python.exe'
    else:  # Unix/Mac
        venv_python = Path(__file__).parent / 'venv' / 'bin' / 'python'
    
    subprocess.run([str(venv_python), 'manage.py', 'runserver', '8000'])

def run_nextjs():
    """Run Next.js frontend server"""
    print("🎨 Starting Next.js frontend on http://localhost:3000")
    frontend_dir = Path(__file__).parent / 'landing-page-for-security'
    os.chdir(frontend_dir)
    
    # Install dependencies if needed
    if not (frontend_dir / 'node_modules').exists():
        print("📦 Installing Next.js dependencies...")
        subprocess.run(['npm', 'install', '--legacy-peer-deps'])
    
    # Run Next.js dev server
    subprocess.run(['npm', 'run', 'dev'])

def main():
    print("🎯 CrowdGuard-AI Full Stack System")
    print("=" * 50)
    
    # Check if virtual environment exists
    venv_dir = Path(__file__).parent / 'venv'
    if not venv_dir.exists():
        print("❌ Virtual environment not found. Please run setup first.")
        return
    
    # Check if model file exists
    model_file = Path(__file__).parent / 'model' / 'fight_detection_model.h5'
    if not model_file.exists():
        print("❌ Model file not found. Please ensure fight_detection_model.h5 is in the model/ directory.")
        return
    
    print("✅ Environment checks passed!")
    print("🔄 Starting services...")
    
    # Start Django in a separate thread
    django_thread = threading.Thread(target=run_django, daemon=True)
    django_thread.start()
    
    # Give Django time to start
    time.sleep(3)
    
    # Start Next.js in main thread (blocking)
    try:
        run_nextjs()
    except KeyboardInterrupt:
        print("\n👋 Shutting down servers...")
        sys.exit(0)

if __name__ == '__main__':
    main()
