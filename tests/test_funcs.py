import pytesttut as ptt


def test_addition():
    """Example of a unit test for broken functionality"""
    assert ptt.add(41, 1) == 42


def test_power():
    """Example of a unit test for a not-yet-implemented feature"""
    assert ptt.power(2, 8) == 256
