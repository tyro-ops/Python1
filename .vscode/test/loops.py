# numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
# sum = 0
# val = 0
# for val in numbers:
#     sum = sum+val
#     print(sum)
import sys
import math
x = 5
y = 10
temp = x
x = y
y = temp

# print(y)
# print(x)
# print(1, 2, 3, 4, sep='#', end='&')
# print('I love {0} and {1}'.format('bread', 'butter'))
# print(math.pi)
print(sys.path)
my_list = [1, 3, 6, 10]

# square each term using list comprehension
# Output: [1, 9, 36, 100]
[x**2 for x in my_list]
for x in my_list:
    print(x)
