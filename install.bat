@echo off

:: Change to script directory
cd /D "%~dp0"

python -m venv venv

.\venv\Scripts\pip3.exe install -r requirements.txt
