names :[] = ["Ahmad","Muhammad Ahmad","Muhammad Faisal"]
print(names[0])
print(names[0])
print(names[-2])
print(f'hello {names[2]}')
for i in names:
   print(i)


characters : list[str] = ['a','b','c','d,']
# Slicing [start: end : step ]
## Start is included, end is excluded
### return type will be an array(list)
print(characters[0 : 2])
print(characters[: 2])
print(characters[0 : ])
print(characters[0 : 3 : 2])
print(characters[ : : -1])
print(characters[ : : 2])
print(characters[ : : 3])

del names[2]
print(names)

print(characters.pop()) 

name : list[str] = []
name.append("Ahmad")
print(name)

a=name
a.append("Ahmad")
print(a)
print(name)
# deep Copy
a=name.copy()
a.append("Ahmad")
print(a)
print(name)








