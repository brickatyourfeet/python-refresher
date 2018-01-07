should_continue = True

if should_continue:
    print('Hello')

known_people = ['John', 'Anna', 'Mary']

#person = input('Enter a person you know: ')

# if person in known_people:
#     print('you know this person!')
#
# if person not in known_people:
#     print('you do not know this person!')

# if person in known_people:
#     print('you know {}!'.format(person))
# else:
#     print('who is {}?'.format(person))
#.format is sort of like template literals in js

##some methods

def who_do_you_know():
    people = input('who do you know? separate by commas')
    people_list = people.split(',')

    people_without_spaces = []
    for person in people_list:
        people_without_spaces.append(person.strip())

    return people_without_spaces

def ask_user():
    person = input('enter a name of someone you know: ')
    if person in who_do_you_know():
        print('you know {}!'.format(person))

ask_user()







## examples of modulus and elif below

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def even_numbers():
    evens = []
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
    return evens


def user_menu(choice):
    if choice == "a":
        return "Add"
    elif choice == "q":
        return "Quit"
