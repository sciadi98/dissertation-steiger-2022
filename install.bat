@echo off

:: Change to script directory
cd /D "%~dp0"

.\venv\Scripts\pip3.exe install -r requirements.txt
