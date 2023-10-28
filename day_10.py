
from typing import Callable
# variable.method_name()
a : str = print("Pakistan") # a = "Pakistan" | None

print(a) # None

print("aa")
print(len('aaa'))


def piaic()->None: # declaration/function signature
    # function body start
    print("PIAIC Generative Artificial Intelligence") # statement1
    print("Python Crash course") # statement2
    # function body end


piaic() # calling
piaic() # calling

def add_two_numbers(num1 : int , num2 : int)->int:
    return num1 + num2

result = add_two_numbers(7, 20)
print(f"Result of addition: {result}")

def add_two_numbers(num1 : int , num2 : int)->int:
    print(f"num1 value {num1} and num 2 value {num2}")
    
    return num1 + num2

result = add_two_numbers(7, 20)
print(f"Result of addition: {result}")


def add_two_numbers(num1: int, num2:int = 0) -> int:
    print(f"num1 value {num1} and num 2 value {num2}")
    
    return num1 + num2

result = add_two_numbers(7,34)
print(f"Result of addition: {result}")

a = lambda num1, num2 : num1 + num2
print(a(7,8))

add: Callable[[int, int], int] = lambda x, y: x + y
result = add(10, 20)  # result will be 30
print(result)

data : list[int] = [1,2,3,4,5,6,7,8,9,10]

data = list(map(lambda x:x**2 , data))
print(data)

data : list[int] = [1,2,3,4,5,6,7,8,9,10]
data = list(filter(lambda x:x%2 ==0 , data))
print(data)

data:list[int] = list(filter(lambda x:x%2==0 ,range(1,101)))
print(data)


def my_range(start:int , end:int , step: int=1):
    for i in range(start,end+1,step):
        yield i # Generator function
a = my_range(1,10)
print(a)
print(list(a))

a = my_range(1,10)
print(a)
print(next(a))
print(next(a))
print(next(a))
print("Pakistan")
print(next(a))


def abc(*nums):
    print(nums, type(nums))
    total = 0
    for n in nums:
        total += n

    return total


result = abc(1,2,3,3,5,6)
print(result)

from typing import Tuple

def greet(*names: Tuple[str, ...]) -> str:
    """
    This function greets all persons in the names tuple.
    """
    for name in names:
        print("Hello", name)

print(greet("Monica", "Luke", "Steve", "John","Sir Zia", "Muhammad Qasim"))

from typing import Dict
def greet(**xyz: Dict[str,str]) ->None :
    print(xyz)

greet(a="pakistan", b='China')


def xyz(**kargs):
    print(kargs, type(kargs))


xyz(a=7, b=20, c=30, x=1,y=2 , name="Muhammad Qasim")

def my_function(a:int, b:int, *abc:Tuple[int, ...], **xyz:Dict[str,int]):
    print(a,b, abc, xyz)

my_function(1,2, 7,9,9,9, c=20, d= 30, x=100)


def factorial(x : int) ->int:
   if x ==1:
      return 1
   else:
      return (x*factorial(x-1))
num = 6
print(f"The factorial of {num} is {factorial(num)}")