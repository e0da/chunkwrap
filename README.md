# Chunkwrap

Chunkwrap is a command-line tool that splits a text file into smaller chunks
while maintaining the original formatting.

## Installation

To install Chunkwrap, follow these steps:

1. Ensure you have Python 3.7 or higher installed.
2. Install [Poetry](https://python-poetry.org/) and
   [pipx](https://github.com/pipxproject/pipx) if you haven't already.
3. Clone this repository and navigate to the root directory.
4. Run `poetry build` to build the package.
5. Run `pipx install dist/chunkwrap-0.1.0-py3-none-any.whl` to install the
   package (replace `0.1.0` with the actual version number if it's different).

## Usage

```bash
chunkwrap input_file.md 4000
```

Replace input_file.md and 4000 with the actual input file and desired chunk size
in bytes, respectively.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE)
file for details.
