# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['totorand.py'],
    pathex=[],
    binaries=[('/Users/hristoiliev/Desktop/PycharmProjectsss/Toto-6-49-random-numbers-generator/venv/lib', '~/Users/hristoiliev/Desktop/PycharmProjectsss/toto')],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='totorand',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
