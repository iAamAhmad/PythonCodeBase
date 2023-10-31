class Teacher():
    def __init__(self, teacher_id : int , teacher_name : str) -> None: # method/constructor
        self.name : str = teacher_name #self.attribute_name = value
        self.teacher_id : int  = teacher_id
        self.organization_name: str = "PIAIC"


    def speak(self, words : str )->None: # method
        print(f"{self.name} is speaking {words}")
    
    def teaching(self, subject : str )->None: # method
        print(f"{self.name} is teaching {subject}...!")
        
obj1 : Teacher = Teacher(1,"Sir Zia Khan") #initialize object->calling constructor __init__() method only this time
# obj1 = object, teacher class instance
obj2 : Teacher = Teacher(2, "Muhammad Qasim")
print(obj1.name)
print(obj1.teacher_id)
print(obj1.organization_name)

print(obj2.name)
print(obj2.teacher_id)
print(obj2.organization_name)
obj1.teaching("Generative AI")
obj2.teaching("Deep Learning")

class Teacher():
    counter : int = 0 # Class variable1
    help_line_number : str = "0315-2968211" # class variable2

    def __init__(self, teacher_id : int , teacher_name : str) -> None: # method/constructor
        self.name : str = teacher_name #self.attribute_name = value
        self.teacher_id : int  = teacher_id
        self.organization_name: str = "PIAIC"
        Teacher.counter += 1


    def speak(self, words : str )->None: # method
        print(f"{self.name} is speaking {words}")
    
    def teaching(self, subject : str )->None: # method
        print(f"{self.name} is teaching {subject}...!")

    def details(self)->None:
        information : str = f"""
Teacher name is {self.name}
our help line number is {Teacher.help_line_number}

"""
        print(information)


obj1 : Teacher = Teacher(1,"Sir Zia Khan")

print(Teacher.counter, obj1.counter)

print(obj1.counter)
print(obj2.counter)
print(Teacher.counter)

print(obj1.help_line_number)
print(obj2.help_line_number)
print(Teacher.help_line_number)


class Parents():
    def __init__(self)->None:
        self.eye_color : str = "Brown"
        self.hair_color : str = "black"

    def speak(self, words: str)->None:
        print(f"Parent method speak: {words}")

    def watching(sef, object_name : str)->None:
        print(f"You are looking {object_name}!")


class Child(Parents):
    def teaching(self, subject : str = None)->None:
        print(f'Child method for teaching : {subject}')
     


obj1 : Parents = Parents()
print(obj1.eye_color)
print(obj1.hair_color)
obj1.speak("Pakistan zinda bad!")
obj1.watching("TV")

print("======Child object=======")
### Child object 

obj2 : Child = Child()
obj2.watching("Cenima")
obj2.speak("Hello World")
print(obj2.eye_color)
print(obj2.hair_color)
obj2.teaching("Generative AI")


from typing import List

class Employee:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.education: str = ""
        self.department: str = ""
class Designer(Employee):
    def __init__(self, title: str, name: str) -> None:
        super().__init__(name)
        self.title: str = title
class Developer(Employee):
    def __init__(self, title: str, name: str) -> None:
        super().__init__(name)
        self.title: str = title
        self.programming_skills: List[str] = ["python"]

designer1: Designer = Designer("Animation Artist", "Asif Khan")
dev1: Developer = Developer("GenAI Engineer", "John Doe")

print(designer1.title)  # Output: Animation Artist
print(dev1.programming_skills)  # Output: ['python']