"""Fetch and verify the two external files required by the CVPR sample."""

from hashlib import sha256
from pathlib import Path
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parent
SOURCE = (
    "https://raw.githubusercontent.com/cvpr-org/author-kit/"
    "1ce836777851be0386e3d3868e9cc6b3ca8b4d48/"
)
FILES = {
    "cvpr.sty": "17022ee4d719c47f2030c5cf5f9b3ff21950dda74d79fcafd339adf0c7ee4d2d",
    "ieeenat_fullname.bst": "e38e6166bd7b1e6d23a1b79dcdb55c656e4fcdbe91bdf6b50d827e6b5d1aacfc",
}


def main():
    for name, checksum in FILES.items():
        path = ROOT / name
        present = path.exists()
        if present:
            data = path.read_bytes()
        else:
            with urlopen(SOURCE + name, timeout=20) as response:
                data = response.read()
        if sha256(data).hexdigest() != checksum:
            raise SystemExit(f"{name}: SHA-256 mismatch. Expected the pinned CVPR 2025 file.")
        if not present:
            path.write_bytes(data)
        print(f"{name}: verified")


if __name__ == "__main__":
    main()
