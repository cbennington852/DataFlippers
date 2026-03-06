python -m venv menv
source myenv/Scripts/activate
pip install -r requirments.txt
pip install -e .
pyinstaller windows.spec -y
