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

---

## Project Structure

A typical LuaMoon project looks like this:

```
my-project/
├─ luamoon.toml      # Project manifest
├─ luamoon.lock      # Locked dependency graph
├─ .luamoon/         # Managed packages & metadata
└─ src/
```

### luamoon.toml

Defines your project and its dependencies:

```toml
[project]
name = "my-project"
version = "0.1.0"

[dependencies]
lua-cjson = "^2.1"
```

### luamoon.lock

Records exact versions, sources, and hashes to ensure reproducible installs.

Never edit this file manually.

---

## LuaRocks Interoperability

LuaMoon can optionally interoperate with LuaRocks:

```bash
luamoon luarocks add luasocket
```

This allows:

* Easier onboarding for existing Lua users
* Gradual migration instead of hard switching
* Reuse of the existing LuaRocks ecosystem

LuaMoon treats LuaRocks as a *backend*, not a dependency manager to wrap blindly.

---

## Philosophy

LuaMoon follows a few guiding principles:

* **Explicit is better than implicit**
* **Local over global**
* **Reproducibility is a feature, not an afterthought**
* **Tools should teach users what they are doing**

LuaMoon prefers clarity over cleverness—even when that costs a few extra keystrokes.

## Roadmap

Planned features include:

* Version solver improvements
* Binary package support
* Package index & registry
* Offline installs & caching
* Editor tooling (LSP integration)
* Cross-platform single-file binaries

Expect the roadmap to evolve as the project matures.

---

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
