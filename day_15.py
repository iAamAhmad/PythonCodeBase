@ExecutionTimer
def square_numbers(numbers):
    return [number ** 2 for number in numbers]


square_numbers(list(range(10)))
isfhan : Piaic = Piaic()

print(isfhan.piaic_helpline)
isfhan.piaic_helpline = '0300-1234567'
print(isfhan.piaic_helpline)

class StudentLogin():
    def __init__(self) -> None:
        self.__username : str = "Admin" # private
        self.__password : str = "Admin" # private


    def __dbconnectivity(self, user:str, passwrod:str):
        print("Successfully connected")
        if user == self.__username and passwrod==self.__password:
            return "Valid user"
        else:
            return "Invalid user"
        
    def update_password(self,password:str):
        self.__password = password

    def student_login(self, user: str , pass1: str):
        message :str = self.__dbconnectivity(user,pass1)
        print(message)

    def display_information(self):
        print(f"Hello Dear, {self.__username} and password {self.__password}")


qasim : StudentLogin = StudentLogin()
qasim.__password
qasim.student_login("qasim",'qasim123')
qasim.student_login("Admin",'Admin')
qasim.update_password("qasim123")

class Teacher():
    def __init__(self,name) -> None:
        self.name : str = name

sir_zia : Teacher = Teacher("sir zia")

print(sir_zia)


class Teacher():
    def __init__(self,name) -> None:
        self.name : str = name

    def __str__(self) -> str:
        return f"Teacher name is {self.name}"

sir_zia : Teacher = Teacher("sir zia")

print(sir_zia)


from abc import ABC, abstractmethod

from traitlets import Bool

class Animal(ABC):
    @abstractmethod
    def __init__(self) -> None:
        super().__init__()
        self.living_thing : bool = True
        



isfahan : Animal = Animal() 
from abc import ABC, abstractmethod

from traitlets import Bool

class Animal(ABC):
    @abstractmethod
    def __init__(self) -> None:
        super().__init__()
        self.living_thing : bool = True
        



isfahan : Animal = Animal() 

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def __init__(self) -> None:
        super().__init__()
        self.living_thing : bool = True

    @abstractmethod
    def eat(self,food:str):
        ...
        

class Cat(Animal):
    def __init__(self) -> None:
        super().__init__()

    

    

isfahan : Cat = Cat()


print(isfahan.living_thing)

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def __init__(self) -> None:
        super().__init__()
        self.living_thing : bool = True

    @abstractmethod
    def eat(self,food:str):
        ...
        

class Cat(Animal):
    def __init__(self) -> None:
        super().__init__()# parent

    def eat(self, food: str):
        return f"Cat is eating {food}"

    

    

isfahan : Cat = Cat()


print(isfahan.living_thing)

from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def eat(self,food:str):
        ...
        

class Cat(Animal):
    def __init__(self) -> None:
        super().__init__()# parent

    def eat(self, food: str):
        return f"Cat is eating {food}"

    

    

isfahan : Cat = Cat()


print(isfahan.living_thing)

class Duck:
    def quack(self)->str:
        return 'Quack!'

class Person:
    def quack(self)->str:
        return 'I\'m Quacking Like a Duck!'

def in_the_forest(malard):
    print(malard.quack())

donald : Duck = Duck()
john : Person = Person()
in_the_forest(donald)
in_the_forest(john)

# Output:
# 'Quack!'
# 'I'm Quacking Like a Duck!'

class Duck():
    def quack(self)->str:
        return 'Quack!'

class Person():
    def quack(self)->str:
        return 'I\'m Quacking Like a Duck!'

def in_the_forest(malard):
    print(malard.quack())

donald : Duck = Duck()
john : Person = Person()
in_the_forest(donald)
in_the_forest(john)

# Output:
# 'Quack!'
# 'I'm Quacking Like a Duck!'

class XYZ:
    pass

dir(XYZ)


