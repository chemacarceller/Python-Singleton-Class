# Singleton version 1
# The class name should be changed; instead of "Singleton," the name of the class we want to behave like a singleton should be used.
# If we need more than one singleton class, we must copy and paste this code.

class Singleton :

    # static variables (class variables in Python terminology)
    _instance = None
    _initialized = False

    # Creation of the object
    def __new__(cls, *args, **kwargs) :

        # If _instance is None
        if not cls._instance :

            # The __new__ function of the object is called to allocate memory on the heap and create the object that we store in _instance.
            cls._instance = super().__new__(cls)

        # We return the object that was newly created or previously created.
        return cls._instance

    # Object initialization
    def __init__(self, param1) :

        # We use a flag so that initialization only happens once.
        if not self._initialized :

            # Actual initialization
            self.attr1 = param1
            self._initialized = True

# Testing
s1 = Singleton("Value1") 
s2 = Singleton("Value2") 

print(s1 is s2) 
print(s2.attr1)