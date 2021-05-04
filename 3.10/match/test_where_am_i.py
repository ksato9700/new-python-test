import pytest


def where_am_i(point):
    match point:
        case(0, 0):
            return "Origin"
        case(0, y):
            return f"Y={y}"
        case(x, 0):
            return f"X={x}"
        case(x, y):
            return f"X={x}, Y={y}"
        case _:
            raise ValueError("Not a point")


def test_where_am_i():
    assert where_am_i((0, 0)) == "Origin"
    assert where_am_i((0, 3)) == "Y=3"
    assert where_am_i((4, 0)) == "X=4"
    assert where_am_i((5, 6)) == "X=5, Y=6"

    with pytest.raises(ValueError) as excinfo:
        where_am_i((7, 8, 9))
    assert "Not a point" in str(excinfo.value)

    with pytest.raises(ValueError) as excinfo:
        where_am_i("(2,3)")
    assert "Not a point" in str(excinfo.value)
