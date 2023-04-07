import pytest
from click.testing import CliRunner
from chunkwrap.main import main


@pytest.fixture(scope="module")
def runner():
    return CliRunner()


def test_cli_no_args(runner):
    result = runner.invoke(main, [])
    assert result.exit_code != 0
    assert "Error: Missing argument 'file'" in result.output


def test_cli_help(runner):
    result = runner.invoke(main, ["--help"])
    assert result.exit_code == 0
    assert "Split a text file into smaller chunks." in result.output
