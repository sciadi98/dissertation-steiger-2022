@echo off

:: Change to script directory
cd /D "%~dp0"

.\venv\Scripts\python.exe app.py
pause
