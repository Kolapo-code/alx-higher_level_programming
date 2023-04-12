#!/usr/bin/python3
"""Inside the Student class module."""



class Student:
    """Inside the class."""


    def __init__(self, first_name, last_name, age):
        """Initialize Student class.

        Args:
            first_name (str): Student's first name.
            last_name (str): Student's last name.
            age (int): Student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Inside to_json method.

        Args:
            attrs (list): Optional attributes.
        """
        if isinstance(attrs, list) and all(map(lambda x: type(x) == str, attrs)):
            return {j: getattr(self, j) for j in attrs if hasattr(self, j)}
        return self.__dict__

    def reload_from_json(self, json):
        """Inside reload  from json func.

        Args:
            json (dict): json obj.
        """
        for key, value in json.items():
            setattr(self, k, v)
