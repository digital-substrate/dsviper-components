#!/usr/bin/env python3
# Canonical build entry point for dsviper-components.
# Regenerates dsviper_components/ui_*.py and resources_rc.py from
# dsviper_components/*.ui and dsviper_components/resources.qrc.
#
# Run from the repo root:
#
#     python3 dev/build.py
#
# The generated files are listed in .gitignore — never commit them.
# The PySide6 version is pinned in requirements.txt to guarantee
# reproducible regeneration across contributors and CI.

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PKG = REPO / "dsviper_components"
QRC = PKG / "resources.qrc"
RCC_OUT = PKG / "resources_rc.py"


def require(tool: str) -> str:
    path = shutil.which(tool)
    if not path:
        sys.exit(f"error: {tool} not found in PATH (install PySide6).")
    return path


def pyside6_version() -> str:
    try:
        import PySide6
    except ImportError:
        sys.exit("error: PySide6 not installed (pip install -r requirements.txt).")
    return PySide6.__version__


def regen_resources(rcc: str) -> None:
    if not QRC.is_file():
        sys.exit(f"error: missing {QRC.relative_to(REPO)}")
    print(f"  pyside6-rcc {QRC.relative_to(REPO)} -> {RCC_OUT.relative_to(REPO)}")
    subprocess.run([rcc, str(QRC), "-o", str(RCC_OUT)], check=True, cwd=REPO)


def regen_ui(uic: str) -> None:
    ui_files = sorted(PKG.glob("*.ui"))
    if not ui_files:
        sys.exit(f"error: no *.ui files in {PKG.relative_to(REPO)}")
    for ui in ui_files:
        out = ui.with_name(f"ui_{ui.stem}.py")
        print(f"  pyside6-uic {ui.relative_to(REPO)} -> {out.relative_to(REPO)}")
        subprocess.run([uic, str(ui), "-o", str(out)], check=True, cwd=REPO)


def main() -> None:
    print(f"PySide6 {pyside6_version()}")
    rcc = require("pyside6-rcc")
    uic = require("pyside6-uic")
    print("Regenerating Qt resource module...")
    regen_resources(rcc)
    print("Regenerating UI modules...")
    regen_ui(uic)
    print("Done.")


if __name__ == "__main__":
    main()
