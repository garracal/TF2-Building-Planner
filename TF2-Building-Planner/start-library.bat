@echo off
rem Starts the TF2 Building Planner library on this computer.
rem Put this file next to index.html (the planner) and the configs folder, then double-click it.
cd /d "%~dp0"
set "PY=python"
where py >nul 2>nul && set "PY=py"
if exist build_index.py (
  echo Rebuilding index.json...
  %PY% build_index.py
)
echo.
echo Library running at http://localhost:8000/   (close this window to stop it)
start "" cmd /c "timeout /t 2 >nul & start http://localhost:8000/"
%PY% -m http.server 8000
pause
