# Write a program to check if the given number is a palindrome number.

a = str(input('Enter a number: \n'))
i = a[::-1]
if i==a:
    print('it is a palindrome number')
else:
    print('It is not a palindrome number')    