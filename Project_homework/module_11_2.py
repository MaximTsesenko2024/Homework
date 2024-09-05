from pprint import pprint
from inspect import isclass,  isfunction, isroutine


class MyClass:
    def __init__(self):
        self.number = 0

    def get_number(self):
        return self.number

    def set_number(self, number):
        self.number = number


def introspection_info(obj: object):
    data = {}
    attrs = dir(obj)
    data['name'] = type(obj).__name__
    data['methods'] = []
    data['function'] = []
    data['attributes'] = [i for i in obj.__dict__.keys()]
    data['modul'] = type(obj).__module__
    for attr in attrs:
        tp = getattr(obj, attr)
        if isclass(tp):
            data['type'] = type(obj)
        elif isroutine(tp):
            data['methods'].append(attr)
        elif isfunction(tp):
            data['function'].append(attr)
    return data


my_val = MyClass()
pprint(introspection_info(my_val))
