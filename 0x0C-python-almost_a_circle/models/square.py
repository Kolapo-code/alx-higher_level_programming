#!/usr/bin/python3
"""Square module."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Inside square class."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square.
        
        Args:
            size (int): size of square.
            x (int): x coord.
            y (int): y coord.
            id (int): Square id.
        """
        Rectangle.__init__(self, width=size, height=size, x=x, y=y, id=id)

    @property
    def size(self):
        """Size getter."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Str repesentation."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """Update method.
        
        Args:
            args (int): list of attrs.
            kwargs (dict): named attrs.
        """
        if args:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1

        elif kwargs:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}
