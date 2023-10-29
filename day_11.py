from day_10 import xyz


list_a: list[int] = [1, 2, 3] # 4
list_b = list_a
list_b.append(4)
print("list_b:", list_a) # Output: list_b: [1, 2, 3, 4]

num_a : int = 5
num_b = num_a
num_a += 1
print("num_b:", num_b) # Output: num_b: 5


x = 10
print("Before modification:", x, id(x))
x += 1
print("After modification:", x, id(x))


a : int = 5

print(f"First Assignment of variable a value is {id(a)}")

def abc(num1:int)->None:
    print(f"\tValue of start of function {num1} address {id(num1)}")
    num1 = 6# copy now it will change update object

    print(f"\tnum1 value end of function {num1} address {id(num1)}") # change here
    print("\tEnd of program")

abc(a) # pass by value immutable

print(f"End of program variable value is {a} address of a {id(a)}")

x : int = 7
b = x 

print(f"X value is {x} and X address {id(x)}")
print(f"X value is {b} and X address {id(b)}")
b = 200 # update then it will change address
print(f"X value is {b} and X address {id(b)}")

x : int = 7

b : int = 7

print(f"X value is {x} and X address {id(x)}")
print(f"X value is {b} and X address {id(b)}")

b = 200 # update then it will change address

print(f"X value is {b} and X address {id(b)}")

x : int = 7

b : int = int(7)# changes then it will create new object

print(f"X value is {x} and X address {id(x)}")
print(f"X value is {b} and X address {id(b)}")

b = 200 # update then it will change address
print(f"X value is {b} and X address {id(b)}")

a : list[int] = [1,2,3,4]

print(id(a))

def abc(num1:list[int])->None:
    print(f"\tValue of start of function {num1} address {id(num1)}")
    num1.append(200)# added on element
    print(f"num1 value is {num1} address {id(num1)}")

abc(a)# pass by reference (mutable data type)
print(a)

a : list[int] = [1,2,3,4]

def abc(num1:list[int])->None:
    num1:list[int] = [7] # reassign list variable -> create new object
    num1.append(200)# added on element
    print(f"num1 value is {num1}")

abc(a)# pass by reference (mutable data type)

print(a)

a : list[int] = [1,2,3,4]

def abc(num1:list[int])->None:
    num1:list[int] = [1,2,3,4] # reassign list variable -> create new object
    num1.append(200)# added on element
    print(f"num1 value is {num1}")

abc(a)# pass by reference (mutable data type)

print(a)

# a : int = int(input("Enter number1:\t"))
# b : int = int(input("Enter number2:\t"))

# print(a / b)

print("logic1")
print("logic2")
try:
    print(5/0)# Error
except ZeroDivisionError:
    print("Zero Division Error!")
print("logic4")
print("logic5")
print("logic1")
print("logic2")

l1 : list[int] = [1,2,3]

try:
    print(5/0)# Error
    print(l1[0])
    print(xyz)

    
except (ZeroDivisionError,IndexError):
    print("Zero Division Error!")
print("logic4")
print("logic5")
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