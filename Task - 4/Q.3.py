# Write a python program to make a 2-dimensional list that contains represents a table of records.

list = []
list = [['Roll no','Student Name','Marks'], ['1','James','85'], ['2','Sam','90'], ['3','Grace','95']]
for j in list:
    print (j)

# Appending A new record

new_list = input('Enter a new record: ')
list.append(new_list)
for i in list:
    print(i)

# Extracting a record from the table

list1 = int(input('Enter the record to be extracted: '))
print(list[list1])