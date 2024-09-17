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
    data['name'] = type(obj).__name__
    data['modul'] = type(obj).__module__
    data['type'] = type(obj)
    if isinstance(obj, (int, str, dict, list, tuple, set)):
        obj = type(obj)
    attrs = dir(obj)
    data['methods'] = []
    data['function'] = []
    data['attributes'] = [i for i in obj.__dict__.keys()]
    for attr in attrs:
        tp = getattr(obj, attr)
        if isroutine(tp):
            data['methods'].append(attr)
        elif isfunction(tp):
            data['function'].append(attr)
    return data


my_val = MyClass()
pprint(introspection_info(my_val))
my_val = 42
pprint(introspection_info(my_val))
my_val = ''
pprint(introspection_info(my_val))
my_val = []
pprint(introspection_info(my_val))
my_val = ()
pprint(introspection_info(my_val))
my_val = {1: 4}
pprint(introspection_info(my_val))
my_val = {1,2}
pprint(introspection_info(my_val))
