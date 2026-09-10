#!/usr/bin/env python3
"""Check the shared plugin, local references and Git publication boundary."""
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins/super-humanizer"


def require(condition, message):
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def read_json(path):
    return json.loads((ROOT / path).read_text())


codex = read_json("plugins/super-humanizer/.codex-plugin/plugin.json")
claude = read_json("plugins/super-humanizer/.claude-plugin/plugin.json")
for key in ("name", "version", "description", "author", "license", "skills", "repository"):
    require(codex[key] == claude[key], f"manifest mismatch: {key}")
require(codex["name"] == PLUGIN.name, "plugin name and directory differ")
require(re.fullmatch(r"\d+\.\d+\.\d+", codex["version"]), "invalid version")
require(codex["skills"] == "./skills/", "unexpected skill directory")
for catalog in (".agents/plugins/marketplace.json", ".claude-plugin/marketplace.json"):
    market = read_json(catalog)
    require(market["name"] == "super-humanizer", f"marketplace name: {catalog}")
    require(len(market["plugins"]) == 1, f"unexpected plugin count: {catalog}")
    entry = market["plugins"][0]
    source = entry["source"]
    require(entry["name"] == codex["name"], f"plugin name: {catalog}")
    require((source["path"] if isinstance(source, dict) else source)
            == "./plugins/super-humanizer", f"source path: {catalog}")

skills = sorted((PLUGIN / "skills").glob("*/SKILL.md"))
require(len(skills) == 2, "expected two skills")
for skill in skills:
    text = skill.read_text()
    require(text.startswith("---\n"), f"missing frontmatter: {skill}")
    header = text.split("---", 2)[1]
    require(f"name: {skill.parent.name}\n" in header, f"skill name: {skill}")
    require("description: " in header, f"skill description: {skill}")
for path in PLUGIN.rglob("*"):
    require(not path.is_symlink(), f"symlink in distributable plugin: {path}")
    require(path.resolve().is_relative_to(PLUGIN.resolve()), f"path escapes plugin: {path}")
for path in [ROOT / "README.md", *list((ROOT / "docs").glob("*.md")),
             *list(PLUGIN.rglob("*.md"))]:
    for target in re.findall(r"\]\(([^)]+)\)", path.read_text()):
        if target.startswith(("https://", "http://", "#")):
            continue
        target = target.split("#", 1)[0]
        dest = path.parent / target
        require(not Path(target).is_absolute() and dest.exists(), f"broken local link: {path}: {target}")
        if path.is_relative_to(PLUGIN):
            require(dest.resolve().is_relative_to(PLUGIN.resolve()), f"external skill dependency: {target}")
require((ROOT / "LICENSE").read_bytes() == (PLUGIN / "LICENSE").read_bytes(), "license mismatch")

tracked = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT, capture_output=True)
require(tracked.returncode == 0, "run in a Git checkout")
public_roots = {"README.md", "LICENSE", ".gitignore", "scripts/validate_package.py",
                ".agents/plugins/marketplace.json", ".claude-plugin/marketplace.json"}
for name in tracked.stdout.decode().split("\0"):
    if name:
        require(name in public_roots or name.startswith(("plugins/super-humanizer/", "docs/", ".github/")),
                f"non-public file tracked: {name}")
print(f"PASS: two manifests, two catalogs, {len(skills)} skills, local links and tracked public files")
