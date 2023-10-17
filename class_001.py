import re

print("Hello World!")
a:str="Hello World"
print(a)

name : str = "Muhammad Ahmad"
fname : str = "Muhammad Younas"
education : str = "Engineering"
age : int = 26

# Multiline String \
# f is for formatted String

cart : str = f"""
Student Name : {name}
Father's Name : {fname}
Education : {education}
Age : {age}
"""
print(cart)

# F-string and Jinja Styling 
## when we make variables able in HTML pages!


card : str = f"""
Student Name : %s
Father's Name : %s
Education : %s
Age : %d
""" % (name, fname, education, age)
print(card)

# PlaceHolders!

a = 7
b = 8
fString="Pakistan having value a = {} and standing at b = {}".format(a,b)
print(fString)

# Example 2!
cardOne : str = """
Student Name : {}
Father's Name : {}
Education : {}
Age : {}
""".format(name, fname, education, age)
print(cardOne)

# Example 3!

# Example PlaceHolding
cardTwo : str = """
Student Name : {name}
Father's Name : {fname}
Education : {education}
Age : {age}
""".format(name="Ahmad Pasha", fname="Younas", education="Masters", age=23)
print(cardTwo)

## String methods!

a : list[str] = [ i for i in dir(str) if "__" not in i]
print(a)
print(len(a))

firstName: str = "Muhammad ahmad Pasha"
print(firstName.capitalize())
print(firstName.casefold())
print(firstName.lstrip())
print(firstName.rstrip())
print(firstName.strip())


## Reg Expressions!

firstName: str = " Muhammad ahmad Pasha  "
# reString = re.sub(' {2,100},'', ')

## White Space Characters

print("Name: Muhammad \t\t Ahmad")
print("Name: Muhammad \n\n Ahmad")







