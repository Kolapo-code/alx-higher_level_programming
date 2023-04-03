#!/usr/bin/python3
"""Rectangle class module."""


class Rectangle:
    """Rectangle class."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize Rectangle.
        
        Args:
            width (int): The width of rectangle.
            height (int): The height of rectangle.
        """
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get width of rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value ,int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height of rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns area of rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return perimeter of rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Prints the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        ans = []
        for i  in range(self.__height):
            for _ in range(self.__width):
                ans.append(str(self.print_symbol))
            if i != self.__height - 1:
                ans.append("\n")
        return "".join(ans)

    def __repr__(self):
        """Return repr of rectangle."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Delete dunder."""
        print("Bye rectangle...")

        Rectangle.number_of_instances -= 1
