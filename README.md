# Obsidian Vault Note Importer

Tools for maintaining an Obsidian vault as a structured markdown "database" of
learning notes (CS/programming, web dev, general knowledge). Imports raw
markdown notes into a vault with consistent frontmatter, tracks which topics
are new, and can use Claude to auto-draft notes for those missing topics.

## Note schema

Every note is a `.md` file with YAML frontmatter followed by a markdown body:

```markdown
---
title:
type: concept | project | reference | log
domain: cs | general | football | meta
tags: []
status: seed | growing | mature
created: YYYY-MM-DD
related: ["[[Note Name]]", ...]
source:
---

# Title

## Key Points
## Example
## Why It Matters
## Open Questions
```

See `Big O Notation.md` for a worked example.

## Files

- **`obsidianCreator.py`** — core library:
  - `parse(filename, dest_path=None)` — reads a markdown file, splits frontmatter/body, returns an `md_file`
  - `writeToFile(md_file)` — writes an `md_file` out to disk as `<title>.md` with YAML frontmatter, creating destination folders as needed
  - `doesFileExist(path, tag)` — checks whether `<tag>.md` already exists (and isn't empty) at `path`
  - `md_file` — small read-only wrapper around a note's data/path/title/tags/body
- **`main.py`** — the import loop: scans a source folder for `.md` files, imports any that aren't already in the vault, collects tags from newly imported notes as candidate "new topics," and (on confirmation) calls the Anthropic API to draft a note for each new topic using the schema above
- **`prototype.yaml`** — sample input note used for standalone testing of `obsidianCreator.py`
- **`prompt.txt`** — the vault schema/prompt notes this project is built around

## Setup

```bash
pip install anthropic python-dotenv python-frontmatter pyyaml
```

Create a `.env` file with:

```
ANTHROPIC_API_KEY=your-key-here
```

## Usage

`main.py` currently has the source/destination vault paths hardcoded
(`VAULT_DIR`, and the source notes folder in `importNotes`) — update those
paths for your machine, then run:

```bash
python main.py
```

It will:
1. Import any `.md` files from the source folder not already present in `VAULT_DIR`
2. Print newly discovered tags/topics
3. Ask whether to generate notes for those new topics via Claude (haiku)

To just test the write/parse logic in isolation:

```bash
python obsidianCreator.py
```

This parses `prototype.yaml` and writes the result as a `.md` file.

## Known issues / TODO

- `writeToFile` **overwrites** any existing file with the same title —
  there's no merge/append step yet (see the `WARNING` comment in
  `obsidianCreator.py`).
- No check for whether a source file itself is empty before writing.
- `getNewTags` is deprecated but still present.
- Paths in `main.py` are hardcoded rather than passed as arguments/input.
- `savedStatus` (session state persistence) is stubbed out but not implemented.
