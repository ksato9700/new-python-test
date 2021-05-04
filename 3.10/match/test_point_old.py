import pytest
from .point import Point


def where_am_i_Point(point: Point):
    if not isinstance(point, Point):
        raise ValueError("Not a point")

    if point.x == 0 and point.y == 0:
        return "Origin"
    elif point.x == 0:
        return f"Y={point.y}"
    elif point.y == 0:
        return f"X={point.x}"
    else:
        return f"X={point.x}, Y={point.y}"


def test_where_am_i_Point():
    assert where_am_i_Point(Point(0, 0)) == "Origin"
    assert where_am_i_Point(Point(0, 3)) == "Y=3"
    assert where_am_i_Point(Point(4, 0)) == "X=4"
    assert where_am_i_Point(Point(5, 6)) == "X=5, Y=6"

    with pytest.raises(ValueError) as excinfo:
        where_am_i_Point((7, 8, 9))
    assert "Not a point" in str(excinfo.value)

    with pytest.raises(ValueError) as excinfo:
        where_am_i_Point("(2,3)")
    assert "Not a point" in str(excinfo.value)
