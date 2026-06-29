#!/usr/bin/env python3
"""LLM-agnostic skill adapter — translates semantic verbs to native tool calls.

Usage:
  python adapt.py path/to/SKILL.md              # Auto-detect backend
  python adapt.py --backend hermes SKILL.md      # Explicit backend
  cat SKILL.md | python adapt.py --backend claude # Pipe mode
"""
from __future__ import annotations
import sys, os, json, argparse
from pathlib import Path

MAP_FILE = Path(__file__).parent / 'semantic-map.json'

def load_map() -> dict:
    with open(MAP_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def detect_backend() -> str:
    if os.environ.get('CLAUDE_CODE') or Path.home().joinpath('.claude').exists():
        return 'claude'
    if os.environ.get('HERMES_HOME') or Path.home().joinpath('.hermes').exists():
        return 'hermes'
    if os.environ.get('CODEX_HOME') or Path.home().joinpath('.codex').exists():
        return 'codex'
    return 'generic'

def adapt(text: str, backend: str, verb_map: dict) -> str:
    verbs = verb_map['verbs']
    result = text
    for verb_name, verb_def in verbs.items():
        mapping = verb_def['mappings'].get(backend, verb_def['mappings'].get('generic', []))
        if not mapping or mapping == [None]:
            replacement = f'[{verb_name}: no native tool available for {backend}]'
        else:
            replacement = mapping[0]  # Use primary tool
        result = result.replace('{' + verb_name + '}', replacement)
    return result

def main():
    parser = argparse.ArgumentParser(description='Adapt LLM-agnostic skills to native tool calls')
    parser.add_argument('file', nargs='?', help='SKILL.md file to adapt (omit for stdin)')
    parser.add_argument('--backend', choices=['claude','hermes','codex','generic'],
                       help='Target LLM backend (auto-detect if omitted)')
    args = parser.parse_args()

    if args.file:
        text = Path(args.file).read_text(encoding='utf-8')
    else:
        text = sys.stdin.read()

    backend = args.backend or detect_backend()
    verb_map = load_map()
    result = adapt(text, backend, verb_map)

    print(f'# Adapted for {backend}', file=sys.stderr)
    print(result)

if __name__ == '__main__':
    main()
