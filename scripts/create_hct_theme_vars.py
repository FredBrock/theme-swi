#!/usr/bin/env python3
"""Generate UiConfigProvider themeVars from a seed color using Material HCT.

This script keeps Material Color Utilities out of the app runtime. It installs the
TypeScript package in a temporary cache outside the repo when needed, then asks
Node to generate the HCT tonal palette.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Any


PACKAGE_NAME = "@material/material-color-utilities"
PACKAGE_VERSION = "0.4.0"
TEMP_ROOT = Path("/var/folders/_9/7bzrbn3x23q2xtzwv41p9sj80000gp/T/opencode")
PACKAGE_DIR = TEMP_ROOT / "material-color-utilities-ts"
TONES = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 95, 99, 100]


def normalize_hex(value: str) -> str:
    color = value.strip()

    if not color.startswith("#"):
        color = f"#{color}"

    if re.fullmatch(r"#[0-9a-fA-F]{3}", color):
        color = "#" + "".join(char * 2 for char in color[1:])

    if not re.fullmatch(r"#[0-9a-fA-F]{6}", color):
        raise ValueError("seed color must be a 3-digit or 6-digit hex color, for example #00fEFF")

    return color.upper()


def run(command: list[str], cwd: Path | None = None) -> str:
    result = subprocess.run(
        command,
        cwd=str(cwd) if cwd else None,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    return result.stdout.strip()


def ensure_material_package() -> None:
    package_json = PACKAGE_DIR / "node_modules" / PACKAGE_NAME / "package.json"

    if package_json.exists():
        return

    PACKAGE_DIR.mkdir(parents=True, exist_ok=True)
    run(["pnpm", "add", f"{PACKAGE_NAME}@{PACKAGE_VERSION}", "--dir", str(PACKAGE_DIR)])


def generate_hct_palette(seed_color: str) -> dict[str, Any]:
    ensure_material_package()

    package_root = PACKAGE_DIR / "node_modules" / PACKAGE_NAME
    tones_js = ",".join(str(tone) for tone in TONES)
    script = f"""
import {{Hct}} from '{package_root}/hct/hct.js';
import {{TonalPalette}} from '{package_root}/palettes/tonal_palette.js';
import {{argbFromHex, hexFromArgb}} from '{package_root}/utils/string_utils.js';

const seed = '{seed_color}';
const hct = Hct.fromInt(argbFromHex(seed));
const palette = TonalPalette.fromHueAndChroma(hct.hue, hct.chroma);
const tones = [{tones_js}];

console.log(JSON.stringify({{
  seed,
  hue: Number(hct.hue.toFixed(2)),
  chroma: Number(hct.chroma.toFixed(2)),
  tone: Number(hct.tone.toFixed(2)),
  tones: Object.fromEntries(tones.map((tone) => [tone, hexFromArgb(palette.tone(tone))])),
}}));
"""

    output = run(["node", "--experimental-specifier-resolution=node", "--input-type=module", "-e", script])
    return json.loads(output)


def create_hct_theme_vars(seed_color: str, vivid: bool = False) -> dict[str, str]:
    palette = generate_hct_palette(seed_color)
    tones = palette["tones"]

    if vivid:
        return {
            "colorPrimaryBg": tones["99"],
            "colorPrimaryBgHover": tones["95"],
            "colorPrimaryBorder": tones["80"],
            "colorPrimaryHover": tones["90"],
            "colorPrimary": tones["80"],
            "colorPrimaryActive": tones["70"],
            "buttonPrimaryBg": "var(--mc-color-primary)",
            "buttonPrimaryBgHover": "var(--mc-color-primary-hover)",
            "buttonPrimaryBgActive": "var(--mc-color-primary-active)",
            "buttonPrimaryText": tones["10"],
        }

    return {
        "colorPrimaryBg": tones["99"],
        "colorPrimaryBgHover": tones["95"],
        "colorPrimaryBorder": tones["80"],
        "colorPrimaryHover": tones["70"],
        "colorPrimary": tones["50"],
        "colorPrimaryActive": tones["40"],
        "buttonPrimaryBg": "var(--mc-color-primary)",
        "buttonPrimaryBgHover": "var(--mc-color-primary-hover)",
        "buttonPrimaryBgActive": "var(--mc-color-primary-active)",
        "buttonPrimaryText": "#ffffff",
    }


def to_typescript_object(name: str, value: dict[str, Any]) -> str:
    lines = [f"const {name} = {{"]

    for key, item in value.items():
        if isinstance(item, dict):
            lines.append(f"  {key}: {{")
            for child_key, child_item in item.items():
                lines.append(f"    {json.dumps(str(child_key))}: {json.dumps(child_item)},")
            lines.append("  },")
        else:
            lines.append(f"  {key}: {json.dumps(item)},")

    lines.append("};")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate HCT themeVars from a seed color.")
    parser.add_argument("seed_color", help="3-digit or 6-digit hex color, for example #00fEFF")
    parser.add_argument("--vivid", action="store_true", help="Use brighter primary mapping for neon/display themes")
    parser.add_argument(
        "--format",
        choices=["json", "ts"],
        default="json",
        help="Output format. Defaults to json.",
    )
    args = parser.parse_args()

    try:
        seed_color = normalize_hex(args.seed_color)
        palette = generate_hct_palette(seed_color)
        theme_vars = create_hct_theme_vars(seed_color, vivid=args.vivid)
        output = {
            "seed": palette["seed"],
            "hct": {
                "hue": palette["hue"],
                "chroma": palette["chroma"],
                "tone": palette["tone"],
            },
            "tones": palette["tones"],
            "themeVars": theme_vars,
        }

        if args.format == "ts":
            print(to_typescript_object("hctTheme", output))
        else:
            print(json.dumps(output, ensure_ascii=False, indent=2))

        return 0
    except (ValueError, subprocess.CalledProcessError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
