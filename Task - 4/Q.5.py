''' Print the following pattern.
    *
   * *
  * * *
 * * * *
* * * * *

'''
n = int(input('Enter a number to create rows: \n'))
i = 1
for i in range(1, n + i):
    print(' '*(n-i)+'* '*i)


   