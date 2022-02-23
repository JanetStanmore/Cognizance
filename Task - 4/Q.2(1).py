# Write a program to accept a string from the user and display characters, that are present at an even index number.

x = input('Enter a message: ')
i = 0
for y in x: 
    if (i%2==0):
      print(y, end ='')
    i = i + 1