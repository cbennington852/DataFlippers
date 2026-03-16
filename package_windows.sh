python -m venv menv
source myenv/Scripts/activate
pip install -r requirments.txt
pip install -e .
pyinstaller windows.spec -y
IF_PATH="C:\Program Files (x86)\solicus\InstallForge\bin\ifbuildx86.exe"
PROJECT_PATH="C:\Projects\MyApp\Setup.ifp"
$IF_PATH $PROJECT_PATH