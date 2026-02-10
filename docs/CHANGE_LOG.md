# Changelog
All notable changes to LuaMoon will be documented in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial release of LuaMoon CLI
- Support for Lua 5.1+ scripts (in progress)
- Package management with `[dependencies]`
- Porting guide for existing Lua projects at `PORTING.md`
- Contribution guides in `CONTRIBUTING.md` and `CODE_OF_CONDUCT.md`
- Auto detection for Lua
- Added the following dependencies (`altgraph==0.17.5`, `certifi==2026.1.4`, `charset-normalizer==3.4.4`, `Cython==3.2.4`,
`idna==3.11`, `markdown-it-py==4.0.0`, `mdurl==0.1.2`, `packaging==26.0`, `pefile==2024.8.26`, `Pygments==2.19.2`, 
`pyinstaller==6.18.0`, `pyinstaller-hooks-contrib==2026.0`, `pywin32-ctypes==0.2.3`, `requests==2.32.5`, `rich==14.3.2`,
`setuptools==80.10.1`, `toml==0.10.2`, `tqdm==4.67.1`, `urllib3==2.6.3`)
- Added some package to the index (for existing packages that doesn't use the structure that luamoon use a
`pkg_name.manifest.toml` has been added to them)
- support for lockfiles, project manifests (two types `lualib.toml` and `luaproject.toml`)
- support for caching downloaded packages
- support for global config
