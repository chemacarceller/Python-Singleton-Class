# Singleton version 4
# version with decorator class, instead of using a function to decorate, a class is used
# Pay attention to the __call__ method of the decorator class
# This method is more complex to understand; the Singleton object is created by executing __new__ and __init__, passing MyClass which stores it in _cls.
# Call __call__ to create the single instance that stores in _instance
# Subsequent calls are made to the already created object, so __init__ is not executed, but __call__ is executed directly.
# Python performs a name reassignment, creating a Singleton object that is stored in MyClass, which changes from a type object to an instance of MyClass.


# decorator class
class Singleton :

    # Initialization of the decorator class
    def __init__(self, cls) :

        # Create instance variables to store the class to be decorated and the instance object of the class
        self._cls = cls
        self._instance = None

    # Magic function __call__
    def __call__(self, *args, **kwargs) :

        # Singleton magic happens :)
        if self._instance is None :

            # Create an instance of the decorated class
            self._instance = self._cls(*args, **kwargs)

        # Returns the object of the decorated class, whether newly created or previously stored.
        return self._instance

# It is told to decorate the MyClass class through the Singleton class
@Singleton
class MyClass :

    # MyClass initializer
    def __init__(self, param1) :

        self.attr1 = param1

# Testing
mc1 = MyClass("Value1")
mc2 = MyClass("Value2")

print(mc1 is mc2)
print(mc2.attr1)