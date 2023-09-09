import datetime
from pathlib import Path

from sphinx.ext import apidoc

copyright = f"{datetime.datetime.now(tz=datetime.timezone.utc).year}, Grigory Petrov"

# Auto generate documentation
apidoc.main(
    [
        "-f",  # force overwrite
        "-T",  # no modules.rst toc
        "-e",  # Each module on it's own page
        "-o",
        str(Path(__file__).parent),  # Output dir relative to "Sphinx root"
        str(Path(__file__).parent.parent / "pyparadoxdb"),  # Source code root
    ]
)
