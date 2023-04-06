import argparse
from pathlib import Path
from chunkwrap.chunkwrap import split_file_into_chunks


def main():
    parser = argparse.ArgumentParser(
        description="Split a text file into smaller chunks."
    )
    parser.add_argument("file", type=Path, help="The input file to be split.")
    parser.add_argument(
        "size", type=int, help="The maximum chunk size in bytes."
    )  # noqa: E501
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="%(prog)s 0.1",
        help="Show program's version number and exit.",
    )

    args = parser.parse_args()

    input_file = args.file
    chunk_size = args.size
    output_dir = input_file.parent / f"{input_file.stem}-chunks"

    split_file_into_chunks(input_file, chunk_size, output_dir)


if __name__ == "__main__":
    main()
