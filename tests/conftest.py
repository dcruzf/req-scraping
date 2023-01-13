from pathlib import Path

import pytest
from bs4 import BeautifulSoup


@pytest.fixture(scope="session")
def code_string():
    p = Path("tests/resource/test_html.html")
    if not p.exists():
        print(p)
        raise FileExistsError
    code = p.read_text()
    yield code


@pytest.fixture(scope="session")
def soup(code_string):
    """Read requests DataFrame."""
    soup = BeautifulSoup(code_string, "html.parser")
    yield soup
