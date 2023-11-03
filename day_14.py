from typing import Union, overload

class Adder:
    @overload
    def add(self, x: int, y: int) -> int:
        ...
        
    @overload
    def add(self, x: float, y: float) -> float:
        ...
        
    @overload
    def add(self, x: str, y: str) -> str:
        ...
        
    
    def add(self, x: Union[int, float, str], y: Union[int, float, str]) -> Union[int, float, str]:
        if isinstance(x, int) and isinstance(y, int):
            return x + y
        elif isinstance(x, float) and isinstance(y, float):
            return x + y
        elif isinstance(x, str) and isinstance(y, str):
            return x + y
        else:
            raise TypeError("Invalid argument types!")
   # Usage examples
adder = Adder()
result1 = adder.add(1, 2)  # Should return 3
result2 = adder.add(1.5, 2.5)  # Should return 4.0
result3 = adder.add("Hello, ", "world!")  # Should return "Hello, world!"

print(result1)
print(result2)
print(result3)


from typing import Union, overload

@overload
def add(x: int, y: int) -> int:
    ...

@overload
def add(x: float, y: float) -> float:
    ...

@overload
def add(x: str, y: str) -> str:
    ...

def add(x: Union[int, float, str], y: Union[int, float, str]) -> Union[int, float, str]:
    if isinstance(x, int) and isinstance(y, int):
        return x + y
    elif isinstance(x, float) and isinstance(y, float):
        return x + y
    elif isinstance(x, str) and isinstance(y, str):
        return x + y
    else:
        raise TypeError("Invalid argument types!")

# Usage examples
result1 = add(1, 2)  # Should return 3
result2 = add(1.5, 2.5)  # Should return 4.0
result3 = add("Hello, ", "world!")  # Should return "Hello, world!"


class Mother:
    def __init__(self,name:str) -> None:
        self.name : str = name
        self.eye_color : str = "blue"
    
    def speaking(self, words : str )->str:
        return f"Monther Speaking function: {words}"

class Father:
    def __init__(self, name:str)->None:
        self.name : str = name
        self.height : str = "6 Feet"

    def speaking(self, words : str )->str:
        return f"Father Speaking function: {words}"

class Child(Mother, Father):
    def __init__(self, mother_name : str, father_name : str , child_name: str)->None:
        Mother.__init__(self, mother_name)
        Father.__init__(self, father_name)
        self.child_name : str = child_name

qasim : Child = Child("Naseem Bano", "Muhammad Aslam","Muhammad Qasim")

print(f"object height {qasim.height}")
print(f"object eye color {qasim.eye_color}")
print(qasim.speaking("Pakistan zinda bad"))

class Mother:
    def __init__(self,name:str) -> None:
        self.name : str = name
        self.eye_color : str = "blue"
    
    def speaking(self, words : str )->str:
        return f"Monther Speaking function: {words}"

class Father:
    def __init__(self, name:str)->None:
        self.name : str = name
        self.height : str = "6 Feet"

    def speaking(self, words : str )->str:
        return f"Father Speaking function: {words}"

class Child(Father, Mother):
    def __init__(self, mother_name : str, father_name : str , child_name: str)->None:
        Mother.__init__(self, mother_name)
        Father.__init__(self, father_name)
        self.child_name : str = child_name

qasim : Child = Child("Naseem Bano", "Muhammad Aslam","Muhammad Qasim")

print(f"object height {qasim.height}")
print(f"object eye color {qasim.eye_color}")
print(qasim.speaking("Pakistan zinda bad"))

class Animal():
    def eating(self,food : str )->None: #same method 
        print(f"Animal is eating {food}")


class Bird(Animal):
    def eating(self, food: str) -> None:
        print(f"Bird is eating {food}")


bird : Bird = Bird()
bird.eating("bread")

animal : Animal = Animal()
animal.eating("grass")

animal : Animal = Bird()# run time it will decide which object method it will be run
animal.eating("grass")

animal : Animal = Animal()
animal.eating("grass")

class MathOperations:

    counter : int = 100
    organization : str = "PIAIC"

    @staticmethod
    def add(x: int, y: int) -> int:
        """Add two numbers."""
        return x + y

    @staticmethod
    def multiply(x: int, y: int) -> int:
        """Multiply two numbers."""
        return x * y

# Using the static methods
result_add = MathOperations.add(10, 20)
result_multiply = MathOperations.multiply(10, 20)

print("Addition:", result_add)
print("Multiplication:", result_multiply)

print("Static variable or Class variable",MathOperations.organization)


class Human():
    def eating(self, food : str)->None:
        print(f"Human is eating {food}")

    
obj1 : Human = Human()
obj1.eating("Biryani")

class Human1(object):
    def eating(self, food : str)->None:
        print(f"Human is eating {food}")

obj2 : Human1 = Human1()
obj2.eating("Biryani")

from typing import Any


class Human1(object):
    def eating(self, food : str)->None:
        print(f"Human is eating {food}")

    def __call__(self) -> None:
        self.eating("Nihari!")

obj3 : Human1 = Human1()
obj3.eating("Biryani")

obj3.__call__()