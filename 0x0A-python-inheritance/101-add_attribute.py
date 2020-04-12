
#!/usr/bin/python3
"""
t adds a new attribute to an object if it's possible
"""


def add_attribute(obj, name, value):
    types = (set, tuple, dict, int, float, str, bool)
    if not isinstance(obj, types) and name is not str and value is not None:
        obj.name = value
    else:
        raise TypeError("can't add new attribute")
