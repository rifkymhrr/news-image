"""Write the single pre-rendered newspaper image, byte for byte."""
from pathlib import Path
import shutil
import tempfile


def main():
    source = Path(__file__).resolve().with_name("entry.png")
    destination = Path("/output/entry.png")
    destination.parent.mkdir(parents=True, exist_ok=True)
    # Publish the image only after its copy is complete.
    with tempfile.TemporaryDirectory(dir=destination.parent) as temporary:
        staged = Path(temporary) / "entry.png"
        shutil.copyfile(source, staged)
        staged.replace(destination)


if __name__ == "__main__":
    main()
