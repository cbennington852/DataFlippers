# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['src/datascratch/main.py'],
    pathex=[],
    binaries=[],
    datas=[('myenv/lib/python3.12/site-packages/aquarel' , '.')],
    hiddenimports=['datascratch' , 'aquarel'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='datascratch',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    icon=resources/Mini_Logo_Alantis_2.svg
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main',
)
