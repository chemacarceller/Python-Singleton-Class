# Singleton version 1
# The class name should be changed; instead of "Singleton," the name of the class we want to behave like a singleton should be used.

class Singleton:
    _instance = None
    _initialized = False

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self, param1):
        if self._initialized:
            return 
        self.attr1 = param1
        self._initialized = True

# Testing
s1 = Singleton("Value1") 
s2 = Singleton("Value2") 

print(s1 is s2) 
print(s2.attr1)