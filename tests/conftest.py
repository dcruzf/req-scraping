from pathlib import Path

import pytest
from bs4 import BeautifulSoup


def get_code(path):
    p = Path(path)
    if not p.exists():
        print(p)
        raise FileExistsError
    code = p.read_text()
    return code


@pytest.fixture(scope="module")
def case1():
    """Read requests DataFrame."""
    path = "tests/resource/case1_projeto-salas-verdes.html"
    soup = BeautifulSoup(get_code(path), "html.parser")
    yield soup


@pytest.fixture(scope="module")
def case2():
    """Read requests DataFrame."""
    path = "tests/resource/case2_obter-bolsa-premio-do-programa-de-acao-afirmativa-do-instituto-rio-branco.html"
    soup = BeautifulSoup(get_code(path), "html.parser")
    yield soup


@pytest.fixture(scope="module")
def case3():
    """Read requests DataFrame."""
    path = "tests/resource/case3_certificar-se-como-entidade-beneficente-de-assistencia-social.html"
    soup = BeautifulSoup(get_code(path), "html.parser")
    yield soup


@pytest.fixture(scope="module")
def case4():
    """Read requests DataFrame."""
    path = "tests/resource/case4_denunciar-violacao-de-direitos-humanos.html"
    soup = BeautifulSoup(get_code(path), "html.parser")
    yield soup
