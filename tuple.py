#empty tuple
my_tuple = ()
print(my_tuple)

#tuples having integers
my_tuple = (1, 10, 100)
print(my_tuple)

#tuples with mixed data types
mixed_tuple = (1, "hello", 3.14)
print(mixed_tuple)

#nested tuple: tuple inside another tuple
nested_tuple = (2, "mouse", [5.1, 2.6, 8.7], [33,55,66])
print(nested_tuple)
print(nested_tuple[3])
print(nested_tuple[3][1])
print(nested_tuple[1])

#accesing a tuple item/ element using index values
my_tuple = ("p", "y", "t", "h", "o", "n")
print(my_tuple[0])
print(my_tuple[5])

#slicing a tuple
print(my_tuple[2:6])

#iterating through tuple using loops
for letter in my_tuple:
    print(letter)