class Mammal():

    def __init__(self, name):
        print(name, "Is a mammal")

class canFly(Mammal):

    def __init__(self, canFly_name):
        print(canFly_name, "cannot fly")

        # Calling Parent class
        # Constructor
        super().__init__(canFly_name)

class canSwim(Mammal):

    def __init__(self, canSwim_name):

        print(canSwim_name, "cannot swim")

        super().__init__(canSwim_name)

class Animal(canFly, canSwim):

    def __init__(self, name):
        super().__init__(name)

# Driver Code
Carol = Animal("Dog")
