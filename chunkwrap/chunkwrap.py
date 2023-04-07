from pathlib import Path
from typing import Optional, Union


def split_file_into_chunks(
    input_file: Union[str, Path],
    chunk_size: int,
    output_dir: Union[str, Path],
    pre_file: Optional[Union[str, Path]] = None,
    end_token: Optional[str] = "CHUNKWRAP_END",
) -> None:
    input_file = Path(input_file)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    if pre_file:
        pre_file = Path(pre_file)

    current_chunk = 1
    current_chunk_size = 0
    output_file = None

    with input_file.open() as f:
        if pre_file:
            pre_content = pre_file.read_text()
            pre_content_size = len(pre_content.encode("utf-8"))

        for line in f:
            line_size = len(line.encode("utf-8"))

            if (
                output_file is None
                or current_chunk_size
                + line_size
                + (0 if pre_file is None else pre_content_size)
                > chunk_size  # noqa: E501
            ):
                if output_file is not None:
                    output_file.write(end_token)
                    output_file.close()

                output_file_path = (
                    output_dir
                    / f"{input_file.stem}-chunks-{current_chunk:03d}.md"  # noqa: E501
                )
                output_file = output_file_path.open("w")

                if pre_file:
                    output_file.write(pre_content)
                    current_chunk_size = pre_content_size
                else:
                    current_chunk_size = 0

                current_chunk += 1

            output_file.write(line)
            current_chunk_size += line_size

    if output_file is not None:
        output_file.close()
