
import sys
counter: int = 0
while counter < 5:
    print("Counter is:", counter)
    counter += 1


numbers: list = [1, 2, 3, 4, 5]
for num in numbers:
    print("Number is:", num)
    
for i in range(5):
    if i == 3:
        break
    print(i)


for i in range(5):
    if i == 3:
        continue
    print(i)
    
for i in range(5):
    if i == 3:
        pass
    print(i)


name: str = input("Enter your name: ")
print("Hello,", name)


import sys

arguments = sys.argv

if len(arguments) < 2:
    print("Error: Not enough arguments provided.")
else:
    print("Script Name:", arguments[0])
    print("First Argument:", arguments[1])



