# Singleton version 2


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class MyClass(metaclass=SingletonMeta):
    def __init__(self, param1):
        self.attr1 = param1

# Testing
mc1 = MyClass("Value1")
mc2 = MyClass("Value2")

print(mc1 is mc2) 
print(mc2.attr1)