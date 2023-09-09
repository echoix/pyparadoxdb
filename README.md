# pyparadoxdb

[![PyPI - Version](https://img.shields.io/pypi/v/pyparadoxdb.svg)](https://pypi.org/project/pyparadoxdb)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyparadoxdb.svg)](https://pypi.org/project/pyparadoxdb)

Simple tool that mirrors Paradox database as SQLite at runtime.

-----

**Table of Contents**

- [Why?](#why)
- [Installation](#installation)
- [License](#license)

## Why?

I have a closed source third party application running on the server that
use Paradox database. In order to communicate with this application i read
Paradox database directly, but it takes about 10 minutes for a simple query
to execute due to the outdated database drivers. This tool reads
Paradox database binary file in background and updates SQLite database file
that mirrors changes. SQLite databse is than used to access data fast and
reliable way.

## Installation

```console
pip install pyparadoxdb
```

## License

`pyparadoxdb` is distributed under the terms of the [GPL-3.0-only](https://spdx.org/licenses/GPL-3.0-only.html) license.
