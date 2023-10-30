print("logic1")
print("logic2")

l1 : list[int] = [1,2,3]
try:
    print(5/2)
    print(l1[0])
    print(xyz) # error
except (ZeroDivisionError,IndexError,NameError):
    print("Zero Division Error!")
print("logic4")
print("logic5")

print("logic1")
print("logic2")

l1 : list[int] = [1,2,3]

try:
    print(5/2)
    print(l1[0])# Error
    # print(xyz) # error
    open("aa.txt")
except (ZeroDivisionError):
    print("Zero Division Error!")
except IndexError:
    print("Index Error")
except NameError:
    print("Name not defined")
except:
    print("Some thing is wrong!")
print("logic4")
print("logic5")
try:
    # print(age)
    print(l1[200])
except Exception as e:
    print(f"Some thing is wrong!\n{e}")
    
    
class StudentCard():
    def __init__(self, roll_no:int, name:str, age:int) -> None:
        if age < 18 or age > 60:
            raise StudentAgeError("Your are not eligible for this program!")
        self.roll_no = roll_no
        self.name = name
        self.age = age


class StudentAgeError(Exception):# custom error class
    pass

student1 = StudentCard(1,"Qasim",30)

print(student1.name, student1.roll_no, student1.age)


student2 = StudentCard(1,"Ahmad",61)

print(student2.name, student2.roll_no, student2.age)


with open("./abc.txt", 'r') as file:  # type: TextIO
    print(type(file))
    print(file.readlines()[:3]) 
    
with open("./abc1.txt", 'w') as file:  # type: TextIO
    file.write("Pakistan zinda bad")
    
with open("./abc1.txt", 'r+') as file:  # type: TextIO
    print(file.read())

    file.write("WE love our country!")

    print("After",file.read())
    
    with open("./abc2.txt", 'r') as file:  # type: TextIO
      print(file.read())