from pathlib import Path

import pytest
from bs4 import BeautifulSoup


@pytest.fixture(scope="session")
def soup():
    """Read requests DataFrame."""
    p = Path("tests/resource/test_html.html")
    if not p.exists():
        print(p)
        raise FileExistsError
    soup = BeautifulSoup(p.read_text(), "html.parser")
    return soup
