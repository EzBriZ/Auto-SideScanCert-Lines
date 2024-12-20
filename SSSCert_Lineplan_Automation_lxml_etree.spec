# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['SSSCert_Lineplan_Automation_lxml_etree.py'],
    pathex=['lxml','lxml.etree',               # Include lxml.etree
        'geopy',                    # Include geopy
        'geopy.distance',           # Include geopy.distance
        'math',                     # Include math module
        'math.sqrt',                # Explicitly include math.sqrt
        'utm',                      # Include utm module
        'tkinter',                  # Include tkinter
        'tkinter.filedialog',       # Include tkinter.filedialog
        'tkinter.simpledialog',     # Include tkinter.simpledialog
        'tkinter.messagebox'        # Include tkinter.messagebox
    ],
    binaries=[],
    datas=[],
    hiddenimports=[],
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
    a.binaries,
    a.datas,
    [],
    name='SSSCert_Lineplan_Automation_lxml_etree',
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
