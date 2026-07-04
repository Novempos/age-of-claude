#!/usr/bin/env python3
"""Age of Claude - play an Age of Empires sound for a Claude Code hook.

Usage: python play.py <sound.wav> [<sound2.wav> ...]
If several names are given one is chosen at random.

Sounds live in ./.claude/sounds relative to this file, so the hook works from
any project (absolute resolution). Hooks set "async": true so Claude is never
blocked; on Windows winsound plays synchronously inside that background process
which keeps it alive long enough for the clip to finish. All errors are
swallowed - a missing player or file must never break a tool call.
"""
import os
import platform
import random
import sys
from pathlib import Path

SOUNDS = Path(__file__).resolve().parent / ".claude" / "sounds"


def main() -> None:
    names = [a for a in sys.argv[1:] if a.strip()]
    if not names:
        return
    path = SOUNDS / random.choice(names)
    if not path.is_file():
        return
    target = str(path)
    system = platform.system()
    try:
        if system == "Windows":
            import winsound

            winsound.PlaySound(target, winsound.SND_FILENAME | winsound.SND_NODEFAULT)
        elif system == "Darwin":
            os.system(f'afplay "{target}" >/dev/null 2>&1 &')
        else:
            os.system(f'aplay -q "{target}" >/dev/null 2>&1 &')
    except Exception:
        pass


if __name__ == "__main__":
    main()
