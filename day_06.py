# Modern python! 
## comprehensive style!
#  true block if logic else false block 
from typing import Union

cars : list[str] = ['audi','bmw','lemborghini'], 
for car in cars:
   if car[2] == 'audi':
      print("Car is Audi")
   elif car[2] == 'bmw':
      print("BMW Is Found")
   else:
      print('Print some Car')

## The Elif Blocks!

percentage : Union[float, int] = 88.0
grade : Union[str, None] = None
if percentage >=80:
   grade == 'A+'
elif percentage >=70:
   grade == 'A'
elif percentage >=60:
   grade == 'B+'

elif percentage >=50:
   grade == 'B'

elif percentage >=40:
   grade == 'C'
elif percentage >=33:
   grade == 'C'
else:
   grade = 'F'
print(grade)

perType = Union[float, int]

percentages : list[perType] = [88, 99, 58, 54, 70]

for std_percentages in percentages:
   print(std_percentages)
   
list[zip(percentages, grade)]


print(percentages)
sorted(percentages, key=lambda x:x[1], reverse=True)

cars : list[str] = ['bmw', 'audi','civic']
calc = [car.upper() if car=='audi' else car.title() for car in cars]
print(calc)