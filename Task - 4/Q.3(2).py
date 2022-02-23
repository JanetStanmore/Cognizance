# Write a python program to make a 2-dimensional list that contains represents a table of records.
# Add some records in the list and print the list in tabular form.
# From created list, extract and print second record/row.

l1=[['Roll No','Student Name','Marks']]
condition='Y'
duplicate=1
while (condition.lower()=='y'):
    print(' Enter 1 to add a new row \n Enter 2 to display the entire table \n Enter 3 to display a single row ')
    choice=int(input(' Enter your Choice: '))
    if choice==1:
        l1.append([int(input('Enter the Roll No.: ')),input('Enter the Student Name: '),int(input('Enter the Marks: '))])
    elif choice==2:
        for a in range(len(l1)):
            for b in range(len(l1[a])):
                print(l1[a][b], '\t\t\t', end='')
            print('\n')
    elif choice==3:
        p = int(input('Enter the Roll No: '))
        for a in range(len(l1)):
            if p == l1[a][0]:
                for b in range(len(l1[a])):
                    print(l1[0][b], '\t', end='')
                print('\n')
                for b in range(len(l1[a])):
                    print(l1[a][b], '\t\t\t', end='')
                print('\n')
            else:
                duplicate=0
        if duplicate==0:
            print('Data Irrelevant')
    else:
        print('Enter a valid option \n')
    condition=input('Do you want to continue? (Y/N): \n')