# Singleton version 3


def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class MyClass :
    def __init__(self, param1):
        self.attr1 = param1

# Testing
mc1 = MyClass('Value1')
mc2 = MyClass('Value2')

print(mc1 is mc2)  
print(mc2.attr1)