from mock import Mock


class Animal:
    def __init__(self, name):
        self.name = name


class Person:
    def __init__(self, name):
        self.name = name

    query = Mock()
    name = Mock()
