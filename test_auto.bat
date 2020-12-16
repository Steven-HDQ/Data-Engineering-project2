@echo off

echo "Offline"

:check
wget -q --spider http://localhost:5000
if errorlevel 1 goto offline
if errorlevel 0 goto online

:online
echo "Online"
python test_app.py
pause

:offline
echo "Offline"
goto check