# Porting
This is an explanation on how to adapt an existing Lua (or Lua-based) project to work with LuaMoon, 
using the current LuaMoon manifest format as the reference. (Currently only pure Lua scripts are supported)

## Porting Steps
1. Create project manifest and fill it
2. adjust your source code if needed
3. Open a new [issue](https://github.com/MXD-K1/LuaMoon/issues/new?template=add_package_to_index.md) to add your module/library to the index

> Note: In the future new packages will be pushed using `luamoon publish` instead of opening new issues

## Project Manifest
A manifest currently looks like this:
```toml
[project]
name = "mylib"
version = "0.1.0"
description = "this is a lib"
author = "me"
license = "MIT"


[environment]
src_dir = "src"
lua_version = "5.1"


[dependencies]
argparse = "0.6.0"
penlight = "1.15.0"
```

When porting, your goal is to map your existing project structure and metadata to the same format.

## Filling Project Details 
> Note: Works for both existing and new packages

### Project Metadata `[project]`

| Info	         | Field                |
|:--------------|:---------------------|
| Project name  | project.name         |
| Version	      | project.version      |
| Description	  | project.description  |
| Author(s)	    | project.author       |
| License	      | project.license      |

> Note: It is preferred that version follows semantic versioning (MAJOR.MINOR.PATCH).

### Source Layout `[environment]`

| Info	            | Field                   | Example  |
|:-----------------|:------------------------|:---------|
| Lua Version      | environment.lua_version | `"5.1"`  |
| src (Source dir) | environment.src         | `"src"`  |

> Note: If you didn't put your source code in a separate folder you can simply type `"."`

### Dependencies `[dependencies]`
Move your external libraries here.

Whether you copied libraries/modules manually or used LuaRocks, you can add them using the format `pkg="version"` 
e.g. `argparse = "0.6.0"`

## Porting from LuaRocks

If you have a `.rockspec` file, you can roughly translate:

| rockspec field	 | LuaMoon field           |
|:----------------|:------------------------|
| package	        | project.name            |
| version	        | project.version         |
| description	    | project.description     |
| dependencies	   | `[dependencies]`        |
| source.files	   | environment.src_dir     |

## Adjusting Source Code
Most plain Lua code should work without changes.

You may need to modify:
- Package path if the module modifies it.
- Module paths.

## Checklist before Publishing
- Manifest is valid TOML
- src_dir correctly points to your Lua code	
- All external libraries are listed in `[dependencies]`
- No hardcoded `package.path` hacks remain


## Further Questions
If you have any questions or problems that aren't covered here, don't hesitate to 
open an [issue](https://github.com/MXD-K1/LuaMoon/issues/new) or 
email me at [hmdoonwork71@gmail.com](mailto:hmdoonwork71@gmail.com)
