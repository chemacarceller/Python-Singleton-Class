# Singleton version 4


class Singleton:
    def __init__(self, cls):
        self._cls = cls
        self._instance = None

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = self._cls(*args, **kwargs)
        return self._instance

@Singleton
class MyClass:
    def __init__(self, param1):
        self.attr1 = param1

# Testing
mc1 = MyClass("Value1")
mc2 = MyClass("Value2")

print(mc1 is mc2)
print(mc2.attr1)