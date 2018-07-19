class Person:
    def __init__(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            return


a1 = Person('abc')
