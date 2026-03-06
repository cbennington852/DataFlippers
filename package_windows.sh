python -m venv menv
source myenv/Scripts/activate
pip install -r requirements.txt
pip install -e .
pyinstaller windows.spec -y
