from src.utils import get_sentences_tag_util
from bs4 import BeautifulSoup
import pytest

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
        ["ok", "ok ", "ok"],
    ),
    ("<ol><li><div><p>ok</p></div></li><li>ok</li></ol>", ["ok", "ok"]),
]


@pytest.mark.parametrize("html, expected", data)
def test_get_sentences_tag(html, expected):
    doc = BeautifulSoup(html, "html.parser")
    result = get_sentences_tag_util(doc()[0])
    assert result == expected
