# Singleton version 2
# Version created using a particular metaclass
# The metaclass is responsible for constructing the class; once the class is created using __new__ and __init__, the metaclass calls __call__.
# If the class has already been created, only __call__ is called.
# __call__ returns the instance of the object of the created class, and that's where the filtering happens so that there can't be more than one instance.
# The creation of the object that is the instance of the created class is carried out by calling the __call__ method of the superclass of our particular metaclass, which is the metaclass type

class SingletonMeta(type):

    # Registers the unique instance of all classes created with this metaclass
    _instances = {}

    # method __call__
    def __call__(cls, *args, **kwargs) :

        # If we have not created an instance of the created class
        if cls not in cls._instances :

            # We create the instance of the class by calling __call__ of the parent class of the particular metaclass
            instance = super().__call__(*args, **kwargs)

            # We register the class instance so that it is not created again.
            cls._instances[cls] = instance

        # We return the instance of the class taken from the dictionary
        return cls._instances[cls]

# definition of the class to which we want to apply the singleton pattern
class MyClass(metaclass=SingletonMeta) :

    # Initializer of our singleton class
    def __init__(self, param1) :
        self.attr1 = param1


# Testing
mc1 = MyClass("Value1")
mc2 = MyClass("Value2")

print(mc1 is mc2) 
print(mc2.attr1)