from src import scrap


def test_scrap_case1(case1):
    result = scrap(str(case1))

    assert len(result) > 0


def test_scrap_cas2(case2):
    result = scrap(str(case2))

    assert len(result) > 0
