#!/usr/bin/python3
"""A Rectangle module."""


class Rectangle:
    """The Rectangle class."""

    def __init__(self, width=0, height=0):
        """Initialize the Rectangle class.

        Args:
            width (int): Width of Rectangle.
            height (int): Height of Rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """The private property getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """The private property setter for width.

        Args:
            value (int): Set to this value.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """The height property getter."""
        return self.__height

    @height.setter
    def height(self, value):
        """The height property setter.

        Args:
            value (int): Set to this value.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Returns area of Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns perimeter of Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
