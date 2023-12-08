# type(name, bases, dict) is similar to creating a class in python
# classes are also objects that create objects of the class type
# type is a metaclass
# This is how you create a class using type
# arg 1 is the name of the class, arg 2 is the base class, arg 3 is the dictionary of the class methods
Test = type('Test', (), {'x': 1, 'y': 2})

def function(self):
    print('Hello World')
TestWithFunction = type('TestWithFunction', (), {'x': 1, 'y': 2, 'function': function})


class MetaClass(type):
    # Hook into class construction with __new__ where object is created
    # notice name, bases and dict are the same arguments of a class as the type instance since they are identical
    # the only extra value is the self argument aliased as cls
    def __new__(cls, clsname, bases, dct):
        uppercase_attr = {}
        for name, val in dct.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val
        return super().__new__(cls, clsname, bases, uppercase_attr)


class TestMeta(metaclass=MetaClass):
    x = 1
    y = 2
    def function(self):
        print('Hello World')

meta = TestMeta()
print(meta.X)
print(meta.Y)
meta.FUNCTION()

# This will throw an error because we renamed attributes to uppercase
meta.function()


"""
Meta classes can be useful to modify classes before they are created
and for example validate that the class has certain attributes or methods
or to restrict the class from having certain attributes or methods etc.
"""