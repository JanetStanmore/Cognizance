# Write a python program to make a 2-dimensional list that contains represents a table of records.

list = []
list = [['Roll no','Student Name','Marks'],
['1','James','85'],
['2','Sam','90'],
['3','Grace','95']]
for j in list:
   print(j)

# Add some records in the list and print the list in tabular form.

list.append(['0','Alice','90'])
for j in list:
   print(j)

# From created list, extract and print second record/row.

print(list[2])