import pytest
from bs4 import BeautifulSoup

from src.utils import get_text_general

data = [
    ("<p>ok</p>", ["ok"]),
    ("<p> ok </p>", ["ok"]),
    ("<p>\nok\n</p>", ["ok"]),
    ("<p>o<span>k</span></p>", ["ok"]),
    ("<p>o<span>k</span><br>ok</p>", ["ok", "ok"]),
    ("<p>ok<br>ok</p>", ["ok", "ok"]),
    ("<ul><li>ok</li><li>ok</li></ul>", ["ok", "ok"]),
    (
        "<ul><li><div><p>ok</p></div></li><li>ok <a>ok</a></li></ul>",
        ["ok", "ok ok"],
    ),
    ("<ol><li><div><p>ok</p></div></li><li>ok</li></ol>", ["ok", "ok"]),
    (
        "<div><ul><li><p>1</p></li></ul><ul><li>2</li></ul><ul><li>3</li><li><span>4<span> 5</li></ul></div>",
        ["1", "2", "3", "4 5"],
    ),
]


@pytest.mark.parametrize("html, expected", data)
def test_get_text_general(html, expected):
    doc = BeautifulSoup(html, "html.parser")
    result = get_text_general(doc()[0])
    assert result == expected
