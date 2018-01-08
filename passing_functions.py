#lamdas are single line only - fat arrow-like functions

def methodception(another):
    return another()

def add_two_numbers():
    return 35 + 77

methodception(add_two_numbers)

###

methodception(lambda: 35 + 77)

my_list = [13, 56, 77, 484]
list(filter(lambda x: x != 13, my_list))  # A lambda function is just a short, one-line function that has no name.

# We could also do

def not_thirteen(x):
    return x != 13

list(filter(not_thirteen, my_list))

#as of python 3.5 - filter needs to be wrapped in list in order to return list

# filter() passes each element of my_list as a parameter to the function.
