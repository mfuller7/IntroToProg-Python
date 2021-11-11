# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# MFuller,11.10.2021,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture of the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
file1 = open(objFile, 'r')
for row in file1:
    strData = row.split(',')
    dicRow = {'Task': strData[0].strip(), 'Priority': strData[1].strip()}
    lstTable.append(dicRow)
file1.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print('='*20)
        print('To Do List')
        print()

        for row in lstTable:
            print(row['Task'] + ' | ' + row['Priority'])
        print('=' * 20)

        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        task = input('Please enter task: ')
        priority = input('Please enter priority (high, med, low): ')
        dicRow = {'Task': task, 'Priority': priority}
        lstTable.append(dicRow)
        print()
        print('\"' + dicRow['Task'] + ' | ' + dicRow['Priority'] + '\" added!')
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        numRow = 1

        for row in lstTable:
            print(str(numRow) + ') ' + row['Task'], row['Priority'], sep=' | ')
            numRow += 1

        print()
        strChoice = str(input('Which task would you like to remove? - '))
        popItem = lstTable.pop((int(strChoice)-1))
        print()
        print('\"' + popItem['Task'] + ' | ' + popItem['Priority'] + '\" removed!')

        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        file2 = open(objFile, 'w')
        for row in lstTable:
            file2.write(row['Task'] + ',' + row['Priority'] + '\n')
        file2.close()

        print('Data saved!')
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print('Goodbye!')
        break  # and Exit the program
