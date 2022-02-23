# Write a program to check if the given number is a palindrome number.

from ast import Num


a = int(input('Enter a number: '))
x = a
reverse = 0
while(a>0):
    dig = a % 10
    reverse = reverse*10 + dig
    a = a//10

if (x == reverse):
    print('Its is a palindrome number')
else:
    print('It is not a palindrome number')
