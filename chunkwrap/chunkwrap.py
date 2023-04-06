from pathlib import Path
from typing import Union


def split_file_into_chunks(
    input_file: Union[str, Path], chunk_size: int, output_dir: Union[str, Path]
) -> None:
    input_file = Path(input_file)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    current_chunk = 1
    current_chunk_size = 0
    output_file = None

    with input_file.open() as f:
        for line in f:
            line_size = len(line.encode("utf-8"))

            if (
                output_file is None
                or current_chunk_size + line_size > chunk_size  # noqa: E501
            ):
                if output_file is not None:
                    output_file.close()

                output_file_path = (
                    output_dir
                    / f"{input_file.stem}-chunks-{current_chunk:03d}.md"  # noqa: E501
                )
                output_file = output_file_path.open("w")
                current_chunk += 1
                current_chunk_size = 0

            output_file.write(line)
            current_chunk_size += line_size

    if output_file is not None:
        output_file.close()
