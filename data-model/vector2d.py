import math


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        """Returns the string representation of the obj for inspection."""
        return f"Vector({self.x!r}, {self.y!r})"

    def __abs__(self):
        """
        Returns the absolute value of a 2D vector.\n
        Examples:
            >>> v = Vector(1,2)
            >>> abs(v)
            2.23606797749979
            >>> v = Vector(3,4)
            >>> abs(v)
            5.0
        """
        return math.hypot(self.x, self.y)

    def __bool__(self):
        """
        Returns False if the magnitude of a vector is 0.
        Example:
            >>> v = Vector(0,0)
            >>> bool(v)
            False
        """
        return bool(abs(self))

    def __add__(self, other):
        """
        Returns the vector addition of two 2D vector.\n
        Example:
            >>> v1 = Vector(1,2)
            >>> v2 = Vector(3,4)
            >>> v1+v2
            Vector(4, 6)
        """
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        """
        Returns the scalar multiplication of a 2D vector with a scalar.\n
        Example:
            >>> v = Vector(1,2)
            >>> scalar = 3
            >>> v*scalar
            Vector(3, 6)
        """
        return Vector(self.x * scalar, self.y * scalar)
