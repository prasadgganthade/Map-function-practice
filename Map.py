# 1. Write a Python program to triple all numbers in a given list of integers. Use Python map.
numbers = (5,10,15,20,25)
print(numbers)
result = map(lambda x: x +x + x,numbers)
print('\nTripple the given number:')
print(list(result))

# 2. Write a Python program to add three given lists using Python map and lambda.
num1 = [1,2,3]
num2 = [4,5,6]
num3 = [7,8,9]
print(num1)
print(num2)
print(num3)
result = map(lambda x, y ,z:x+y+z,num1,num2,num3)
print("Addition of three list is")
print(list(result))

# 3. Write a Python program to listify the list of given strings individually using Python map.
color = ['red', 'blue','black','white','yellow']
print(color)
result = list(map(list,color))
print(result)

# 4. Write a Python program to create a list containing the power of said number in bases raised to the corresponding number in the index using Python map.
base_num = []
for i in range(10,101,10):
    base_num.append(i)
print(base_num)
power = []
for i in range(1,11):
    power.append(i)
print(power)
result = list(map(pow, base_num,power))
print(result)
# 5. Write a Python program to square the elements of a list using the map() function.
def square_num(n):
    return n * n
nums = [10,15,20,25]
print('Original numbers :',nums)
result = map(square_num,nums)
print('Square of given number is :')
print(list(result))

# 6. Write a Python program to convert all the characters into uppercase and lowercase and eliminate duplicate letters from a given sequence. Use the map() function.
"""
def change_case(s):
    return str(s).upper(), str(s).lower()
character1 = {'a','B','c','D','G','o','i'}
print('Original characters :',character1)
result = map(change_case,character1)
print('\nAfter converting characters to upper and lower case')
print(list(result))
"""

# 7. Write a Python program to add two given lists and find the difference between them. Use the map() function.

def addition_subtraction(x,y):
    return x+y, x-y

numbers1 = [10,20,30,40]
numbers2 = [5,10,15,20]
print(numbers1)
print(numbers2)
result = map(addition_subtraction,numbers1,numbers2)
print('The addtion is :',list(result))

# 8. Write a Python program to convert a given list of integers and a tuple of integers in a list of strings
num_list = [1,2,3,4]
num_tuple = (10,20,30,40)
print('Original')
print(num_list)
print(num_tuple)
result_list = list(map(str,num_list))
result_tuple = tuple(map(str,num_tuple))
print('\nList of string : ',result_list)
print('\nTuple of string:',result_tuple)
# 9. Write a Python program to create a new list taking specific elements from a tuple and convert a string value to an integer.

family_details = [('Prasad Ganthade','09/07/1993','65kg'),
                   ('Ganesh Ganthade','26/09/1954','61kg'),
                   ('Gayatri Ganthade','15/02/1962','68kg')]

family_details_name = list(map(lambda x:x[0],family_details))
family_details_dob = list(map(lambda x:x[1],family_details))
family_details_weight = list(map(lambda x:x[2][:2],family_details))
print('Name :',family_details_name)
print('DOB :',family_details_dob)
print('Weight :',family_details_weight)

# 11. Write a Python program to compute the sum of elements of an array of integers. Use the map() function.

from array import array
def array_sum(num_array):
    sum = 0
    for i in num_array:
        sum += i
    return sum
numbers = array('i',[1,2,3,4,5])
print('Original array : ',numbers)
num1 = list(map(int,numbers))
result = array_sum(num1)
print('The sum is:',result)

# 12. Write a Python program to find the ratio of positive numbers, negative numbers and zeroes in an array of integers.
from array import array

def add_sub(numbers):
    n = len(numbers)
    n1 = n2 = n3 = 0
    for i in numbers:
        if i > 0:
            n1 += 1
        elif i < 0:
            n2 += 1
        else:
            n3 += 1
    return round(n1/n,2), round(n2/n,2), round(n3/n,2)
numbers = array('i',[0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])
print('Original :',numbers)
num_arr = list(map(int,numbers))
result = add_sub(num_arr)
print(result)

# 13. Write a Python program to count the same pair in two given lists. use map() function.
from operator import eq
def count_same_pair(num1,num2):
    result = sum(map(eq,num1,num2))
    return result

num1 = [1,2,3,4,5,6,7,8]
num2 = [2,2,3,1,2,6,7,9]

print('The number of same pair are')
print(count_same_pair(num1,num2))

# 14. Write a Python program to interleave two lists into another list randomly. Use the map() function.
# 15. Write a Python program to split a given dictionary of lists into list of dictionaries using the map function.

def list_of_dict(marks):
    result = map(dict, zip(*[[(key,val) for val in value] for key, value in marks.items()]))
    return list(result)
marks = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
print('Spilt dict')
print(list_of_dict(marks))

# 16. Write a Python program to convert a given list of strings into a list of lists using the map function.
# 17. Write a Python program to convert a given list of tuples to a list of strings using the map function

def tuple_list_of_string(list1):
    result = list(map(" ".join,list1))
    return result

color = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
print('convert to string')
print(tuple_list_of_string(color))

