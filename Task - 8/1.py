# Question 1

a = [5,6,7,8,9]
first = 5
last= 9

final=[]
addZeros = False
for i in a:
    final.append(i)
    if i == first:
        addZeros = True
    if i == last:
        addZeros = False
    if addZeros:
        final.extend([0,0,0,0,0])

print("The output is ",final) 