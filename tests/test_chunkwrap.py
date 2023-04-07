from pathlib import Path

import pytest

from chunkwrap.chunkwrap import split_file_into_chunks


@pytest.fixture
def input_file_content() -> str:
    content = (
        "This is a short line.\n"
        "This line is a bit longer, containing more words and characters than the previous one.\n"  # noqa: E501
        "  This line has leading spaces.\n"
        "\tThis line starts with a tab character.\n"
        "This line ends with trailing spaces.  \n"
        "This is another short line.\n\n"
        "This line is followed by a blank line.\n"
        "\n"
        "  This line has both leading and trailing spaces.  \n"
    )
    return content * 125


@pytest.fixture
def input_file(input_file_content: str) -> Path:
    tmp_dir = Path("tmp")
    tmp_dir.mkdir(parents=True, exist_ok=True)

    input_file_path = tmp_dir / "input.md"
    input_file_path.write_text(input_file_content)

    yield input_file_path


def remove_existing_files(directory: Path, pattern: str) -> None:
    for file in directory.glob(pattern):
        file.unlink()


def test_split_file_into_chunks(input_file: Path, input_file_content: str):
    chunk_size = 4000

    output_dir = Path("tmp") / f"{input_file.stem}-chunks"
    remove_existing_files(output_dir, "*.md")

    split_file_into_chunks(input_file, chunk_size, output_dir)

    # Verify side-effect achieved
    assert output_dir.exists()
    assert output_dir.is_dir()

    output_files = sorted(output_dir.glob("*.md"))
    assert output_files

    # Verify the contents of the generated files
    reconstructed_content = ""
    for output_file in output_files:
        with output_file.open() as f:
            file_content = f.read()
            assert len(file_content.encode("utf-8")) <= chunk_size
            reconstructed_content += file_content

    # Verify that the generated files reconstitute the original content
    assert reconstructed_content == input_file_content

    # Verify side-effect avoided
    assert input_file.exists()
    assert input_file.read_text() == input_file_content
