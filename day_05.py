## Day 05 is starting..

# lists!

 
print("List Of Names:")
names : list[str] = ["Ahmad","Usman","Ehsan"]
for name in names:
   print(name)
print("List Of Fruits:")

fruits : list[str] = ["Banana","Apple","Oranges"]
for fruit in fruits:
   print(fruit)
   
#
fruits : list[str] = ["Banana","Apple","Oranges"]
for fruit in fruits:
   print(f'Hello Will you eat {fruit.title()}')

fruits : list[str] = ["Banana","Apple","Oranges"]
for fruit in fruits:
   print(f'Hello Will you eat {fruit.title()}')
print(f'So You decided to eat {fruit.title()}')


data_base : list[tuple[str,str]] = [(" Qasim", "123"), (" Ahmad", "143"), (" Fateh", "163")]

for row in data_base:
   print(row)
   print(row[0])
   
# User Authentication System!
data_base : list[tuple[str,str]] = [(" Qasim", "123"), ("Ahmad", "143"), (" Fateh", "163")]

for row in data_base:
   user, password = row
   print(user, password)

# input_user : str = input("What is Your UserName?")
# input_password : str = input("What is Your password?")
# for row in data_base:
#    user, password = row
#    if input_user == user and input_password == password:
#       print("Valid User")
#       break
# else:
#    print("User Not Found")

print(list(range(10)))

print(list(range(2,21,2)))

tables = list(range(2,21,2))
for i,n in enumerate(tables):
   print(f'2 x {i} = {n}')

for n in range(1,11):
   print(f'{2} X {n} = {n*2}')


# magicians = ['one', 'two','three']
# for index, name in enumerate(magicians):
#    print()

squares : list[int] = []
for value in range(1,11):
   square = value **2
   squares.append(square)
print(squares)


# List Comprehensive!

comp = [i**2 for i in range(1, 11)]
print(comp)


digits : list[int] = [2,4,5,7,8,9,13]
print(sum(digits))
print(max(digits))
print(min(digits))