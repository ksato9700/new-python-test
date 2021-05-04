import pytest
from .point import Point


def where_am_i_Point(point: Point):
    match point:
        case Point(x=0, y=0):
            return "Origin"
        case Point(x=0, y=yy):
            return f"Y={yy}"
        case Point(x=xx, y=0):
            return f"X={xx}"
        # case Point(x=xx, y=yy):
        #     return f"X={xx}, Y={yy}"
        case Point() as p:
            return f"X={p.x}, Y={p.y}"
        case _:
            raise ValueError("Not a point")


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
