import struct
import sys
import shutil
from pathlib import Path

PNG_SIG = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1048576
MAX_DIM = 1024


def validate(path: Path) -> None:
    header = path.open("rb").read(26)
    if header[:8] != PNG_SIG:
        sys.exit("not a PNG")
    if path.stat().st_size > MAX_BYTES:
        sys.exit("too large")
    w, h = struct.unpack(">II", header[16:24])
    if w > MAX_DIM or h > MAX_DIM:
        sys.exit("dimensions exceed 1024x1024")


def main() -> None:
    src = Path(__file__).parent / "entry.png"
    dst = Path("/output/entry.png")
    validate(src)
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


if __name__ == "__main__":
    main()
