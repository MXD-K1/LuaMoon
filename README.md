# LuaMoon
LuaMoon is an experimental, community-driven package manager for the Lua ecosystem.

Its goal is simple but ambitious: make Lua dependency management **predictable**, **reproducible**, and **pleasant**, 
without sacrificing Lua’s philosophy of simplicity.

LuaMoon is designed as a *modern companion* to existing tools, not a scorched-earth replacement.

---

## Why LuaMoon Exists
Lua is small, flexible, and embeddable, but its package story is fragmented.

LuaMoon aims to solve existing problems with LuaRocks such as:
- The lack of project-local installs. (Only global installs)
- The lack of virtual environments.
- The need to tweak package.path/package.cpath every time a project is created.
- Confusing CLI.
- The non-standard config format.
- Build failures.
- The lack of proper documentation.
- The need to write a rockspec for every version of the library.

---

## Quick Start
Here are the commands of LuaMoon: (These are not implemented yet)
- Initialize a new LuaMoon project: `luamoon init`
- Add a dependency: `luamoon add pkg`
- Update a dependency: `luamoon update pkg`
- Remove a dependency: `luamoon remove pkg`
- Search if a dependency exist: `luamoon search pkg-name`
- List project dependencies: `luamoon list`
- Run project: `luamoon run`
- Publish a package to the index: `luamoon publish`

(Note: Some of these commands might change as the project is in early development stage)

---

## Features (Intended but not implemented yet)

* Project-local dependencies (no global pollution)
* Lockfile-based reproducible installs
* Deterministic dependency resolution
*  Clear on-disk package layout
*  Simple, scriptable CLI
* Optional interoperability with LuaRocks
* Designed for experimentation and evolution

> LuaMoon is under active development. Expect rough edges, sharp ideas, and rapid iteration.

---

## Installation

> LuaMoon is currently in early development.

For now, clone the repository and use it directly:

```bash
git clone https://github.com/MXD-K1/luamoon.git
cd luamoon
```

Future releases will include standalone binaries and installer scripts.


## Contributing

Contributions of all kinds are welcome:

* Code
* Documentation
* Bug reports
* Feature ideas
* Design discussions
and more ...

Please read [`CONTRIBUTING.md`](docs/CONTRIBUTING.md) before opening a pull request.

---

## License

LuaMoon is licensed under the **MIT** [License](LICENSE).

You are free to use, modify, and distribute it under the terms of the license.

---

## Status

LuaMoon is experimental software.

Use it to learn, explore, and build—but not yet for production-critical systems.
