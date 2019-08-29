# -*- mode: python -*-

block_cipher = None


a = Analysis(['wages.py'],
             pathex=['/Users/mbortoli/github/wages'],
             binaries=[],
             datas=[('money-bag.svg','.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='wages',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='wages')
app = BUNDLE(coll,
             name='wages.app',
             icon='money-bag.svg',
             bundle_identifier=None)
