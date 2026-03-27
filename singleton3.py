# Singleton version 3
# This version uses a class decorator, a function that receives a class as a parameter that it decorates.
# The decorator function returns the single instance of the object of the class it decorates, and this function is the one that controls it.
# The decorator works as if its variables were static, not resetting between calls

# decorator function
def singleton(cls) :

    # Dictionary that stores the unique instances of decorated classes
    instances = {}

    # method that applies the singleton pattern
    def get_instance(*args, **kwargs) :

        # if the instance does not exist
        if cls not in instances :

            # the instance is created
            instances[cls] = cls(*args, **kwargs)

        # The function returns either a newly created instance or one that was previously stored.
        return instances[cls]
    
    # The decorator function returns either a newly created instance or a previously stored one.
    return get_instance

# It is said that the MyClass class should be decorated by the decorator called singleton
@singleton
class MyClass :

    # Class initialization
    def __init__(self, param1) :

        self.attr1 = param1

# Testing
mc1 = MyClass('Value1')
mc2 = MyClass('Value2')

print(mc1 is mc2)  
print(mc2.attr1)