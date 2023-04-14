#!/usr/bin/python3
"""The Rectangle class module."""
from models.base import Base


class Rectangle(Base):
    """The Rectangle class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle instance.
        
        Args:
            width (int): Rectangle width.
            height (int): Rectangle height.
            x (int): x coord.
            y (int): y coord.
            id (int):: Rectangle id.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        Base.__init__(self, id)

    @property
    def width(self):
        """Getter for width of Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """Getter for height of Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """Get for x coord."""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """Getter for y coord."""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """Cal area of Rectangle."""
        return self.__width * self.__height

    def display(self):
        """Print the rectangle as `#`."""
        if self.__width == 0 or self.__height == 0:
            print()
        else:
            [print("") for y in range(self.y)]
            for _ in range(self.__height):
                [print(" ", end="") for x in range(self.x)] 
                for j in range(self.__width):
                    print("#", end="")

                    if j == self.__width - 1:
                        print()

    def __str__(self):
        """New str representation."""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """Update the Rectangle.
        
        Args:
            *args (int): attrs.
            **kwargs (dict): named attrs.
        """
        if args:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                i += 1

        elif kwargs:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
    
    def to_dictionary(self):
        """Dict representation."""
        return {'x': self.x, 'y': self.y,  'id': self.id, 'width': self.width, 'height': self.height}
