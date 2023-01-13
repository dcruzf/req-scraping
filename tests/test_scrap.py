from src import scrap


def test_scrap(code_string):
    result = scrap(code_string)

    assert len(result)
