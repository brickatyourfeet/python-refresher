my_var = 'hello'

#below is a list
grades = [77, 80, 90, 95, 100]

#below is a tuple - tuples are immutable
tuple_grades = (77, 80, 90, 95, 100)
#lists are like arrays, can be added to - for example
grades.append(108)
#tuples are immutable - no adding or subtracting from them

tuple_single = 15, #single item tuples have to have comma after

set_grades = {77, 80, 100, 90, 100}
#sets are unique and unordered - the non-unique values are auto removed

print(sum(grades) / len(grades))

#operations for lists tuples and sets

grades.append(50) #50 is added to the end

tuple_grades = tuple_grades + (100,)
# must have comma, this will add 100 and it is ordered so its at the end
print(tuple_grades)

print(grades[0])  #accessing elements is just like javascript

grades[0] = 60 #changes the first item to 60

#tuple_grades[0] = 60   -this is an error, tuples immutable

#set_grades[0] = 60    -would also error because its unordered

set_grades.add(60)  #this will 'add' 60 but its not unique so, peace out

## set operations

set_one = {1, 2, 3, 4, 5}
set_two = {1, 3, 5, 7, 9, 11}

print(set_one.intersection(set_two))
# outputs a set that has all matching numbers [1, 3, 5]

print(set_one.union(set_two))
#prints both in one set but all unique values [1, 2, 3, 4, 5, 7, 9, 11]
#no duplicate in sets!

print({1,2,3,4}.difference({1,2}))
#prints the items that do NOT match
