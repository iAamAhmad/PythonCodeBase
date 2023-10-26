# from typing import Dict

# my_dict: Dict[str, int] = {'apple': 5, 'banana': 3}
# print(my_dict)  # Output: {'apple': 5, 'banana': 3}


# my_dict['cherry'] = 7
# print(my_dict)  # Output: {'apple': 5, 'banana': 3, 'cherry': 7}

# # my_dict.clear()
# print(my_dict)  # Output: {}

# copy_dict = my_dict.copy()
# print(copy_dict)  # Output: {'apple': 5, 'banana': 3, 'cherry': 7}


# sequence = ('apple', 'banana', 'cherry')
# new_dict = dict.fromkeys(sequence, 0)
# print(new_dict)  # Output: {'apple': 0, 'banana': 0, 'cherry': 0}

# value = my_dict.get('apple', 'Not Found')
# print(value)  # Output: 5


# items = my_dict.items()
# print(items)  # Output: dict_items([('apple', 5), ('banana', 3), ('cherry', 7)])


# keys = my_dict.keys()
# print(keys)
# #
# my_dict.pop('apple')
# print(my_dict)

# my_dict.popitem()
# print(my_dict)


# my_dict: Dict[str, int] = {'apple': 5, 'banana': 3}

# value = my_dict.setdefault('Apple', 6)
# print(value)

# my_dict.update({'apple': 5})
# print(my_dict)

# values = my_dict.values()
# print(values)

from typing import Dict

my_dict: Dict[str, int] = {'apple': 5, 'banana': 3}
print(my_dict)  # Output: {'apple': 5, 'banana': 3}


my_dict['cherry'] = 7
print(my_dict)  # Output: {'apple': 5, 'banana': 3, 'cherry': 7}

# my_dict.clear()
print(my_dict)  # Output: {}

copy_dict = my_dict.copy()
print(copy_dict)  # Output: {'apple': 5, 'banana': 3, 'cherry': 7}


sequence = ('apple', 'banana', 'cherry')
new_dict = dict.fromkeys(sequence, 0)
print(new_dict)  # Output: {'apple': 0, 'banana': 0, 'cherry': 0}

value = my_dict.get('apple', 'Not Found')
print(value)  # Output: 5


items = my_dict.items()
print(items)  # Output: dict_items([('apple', 5), ('banana', 3), ('cherry', 7)])


keys = my_dict.keys()
print(keys)

my_dict.pop('apple')
print(my_dict)

my_dict.popitem()
print(my_dict)


my_dict: Dict[str, int] = {'apple': 5, 'banana': 3}

value = my_dict.setdefault('Apple', 6)
print(value)

my_dict.update({'apple': 5})
print(my_dict)

values = my_dict.values()
print(values)