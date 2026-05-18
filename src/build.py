from pathlib import Path

from src.app import render_homepage


def build(output_dir: Path = Path("dist")) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "index.html"
    output_file.write_text(render_homepage(), encoding="utf-8")
    return output_file


if __name__ == "__main__":
    built_file = build()
    print(f"Built {built_file}")
