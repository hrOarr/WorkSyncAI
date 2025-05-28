# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
            ('collectors', 'collectors'),
            ('storage', 'storage'),
            ('api', 'api'),
            ('mq', 'mq'),
            ('configs', 'configs'),
        ],
    hiddenimports=[
    'sqlalchemy.sql.default_comparator',
            'sqlalchemy.ext.baked',
            'sqlalchemy.event',
            'sqlalchemy.pool',
            'sqlalchemy.orm',
    ],
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
    name='worksync',
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
