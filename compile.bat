@echo off
setlocal
pushd "%~dp0"
if errorlevel 1 (
    echo Failed to enter the project directory.
    exit /b 1
)

python -m PyInstaller --noconfirm --clean --onefile --console --name "bit" --distpath "%~dp0output" --workpath "%~dp0build" --specpath "%~dp0build" --paths "." --collect-submodules "libs" --collect-all "consolemenu" --collect-all "colorama" --collect-all "pyfiglet" --collect-all "requests" "%~dp0main.py"
if errorlevel 1 (
    echo Build failed. Check the PyInstaller output above.
    popd
    pause
    exit /b 1
)

echo Build succeeded: "%~dp0output\bit.exe"
popd
pause
