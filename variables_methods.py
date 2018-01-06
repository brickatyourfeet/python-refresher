a = 5
b = 10
my_variable = 56
my_10_var = 10
# generally you won't use a number in the middle but you can
# symbols like $%#& are not allowed
# variables cannot start with a number

string_variable = "hello"
# strings can have single or double quotes
single_quotes = 'this is okay too'
# but keep it consistent

#print(string_variable)
# print is a method - takes in a value

## methods -
# whenever there is a colon, next line must be indented
# and keep indenting inside of that method
def my_print_method(my_argument):
    print('from print method....')
    print(my_argument)

my_print_method('guy')

def multiply(a, b):
    return a * b

result = multiply(5, 3)

my_print_method(result)

my_print_method(multiply(4,2))
