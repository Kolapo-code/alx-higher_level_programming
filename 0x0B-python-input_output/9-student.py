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

    def to_json(self):
        """Inside to_json method."""
        return self.__dict__
