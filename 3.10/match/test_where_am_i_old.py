import pytest


def where_am_i(point):
    # if type(point) != tupple or point.len() != 2:
    #     raise ValueError("Not a point")

    try:
        x, y = point
    except ValueError:
        raise ValueError("Not a point")

    if x == 0 and y == 0:
        return "Origin"
    elif x == 0:
        return f"Y={y}"
    elif y == 0:
        return f"X={x}"
    else:
        return f"X={x}, Y={y}"


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
