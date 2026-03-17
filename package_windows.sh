python -m venv menv
source myenv/Scripts/activate
pip install -r requirments.txt
pip install -e .
pyinstaller windows.spec -y
IF_PATH="~/C:\Program Files (x86)\solicus\InstallForge\bin\ifbuild.bat"
PROJECT_PATH="~/C:\Users\vboxuser\Desktop\DataPenguins\DataScratch\datascratch_installer_windows.ifp"
./"$IF_PATH" "$PROJECT_PATH"
