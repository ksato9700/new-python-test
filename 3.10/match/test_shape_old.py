from .point import Point
from .shape import Rectangle, Circle


def identify_shape(shape):
    if isinstance(shape, Point):
        return f"This is a Point({shape.x}, {shape.y})"
    elif isinstance(shape, Rectangle):
        return f"This is a Rectangle({shape.width}, {shape.length})"
    elif isinstance(shape, Circle):
        return f"This is a Circle({shape.radius})"
    else:
        return "Unknown shape"


def test_identify_shape():
    assert identify_shape(Point(1, 2)) == "This is a Point(1, 2)"
    assert identify_shape(
        Rectangle(3.5, 6.8)) == "This is a Rectangle(3.5, 6.8)"
    assert identify_shape(Circle(2.55)) == "This is a Circle(2.55)"
    assert identify_shape(123) == "Unknown shape"
