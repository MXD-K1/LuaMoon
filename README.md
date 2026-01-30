# LuaMoon
LuaMoon is an experimental, community-driven package manager for the Lua ecosystem.

Its goal is simple but ambitious: make Lua dependency management **predictable**, **reproducible**, and **pleasant**, 
without sacrificing Lua’s philosophy of simplicity.

LuaMoon is designed as a *modern companion* to existing tools, not a scorched-earth replacement.

---

## Why LuaMoon Exists
Lua is small, flexible, and embeddable—but its package story is fragmented.

LuaRocks solved many problems, but over time a few pain points became clear:

* Inconsistent environments across machines
* Global vs local installs confusion
* Limited reproducibility guarantees
* Friction for beginners
* Tooling that assumes Unix-first workflows

LuaMoon explores a different design space:

* **Project-first** dependency management
* **Lockfiles** for reproducible installs
* **Explicit environments** instead of global magic
* **Beginner-friendly defaults**, expert-level control

---

## Features (Intened but not implemnted yet)

* 📦 Project-local dependencies (no global pollution)
* 🔒 Lockfile-based reproducible installs
* 🧩 Deterministic dependency resolution
* 🗂️ Clear on-disk package layout
* ⚙️ Simple, scriptable CLI
* 🔁 Optional interoperability with LuaRocks
* 🧪 Designed for experimentation and evolution

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
