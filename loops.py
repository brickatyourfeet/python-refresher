my_string = 'hello'

for char in my_string:
    print(char)

my_list = [1, 3, 5, 7, 9]

for num in my_list:
    print(num ** 2)  #prints each number to the second power

user_wants_number = True

while user_wants_number == True:
    print(10)

    user_input = input('should we print again? (y/n)')
    if user_input == 'n':
        user_wants_number = False
