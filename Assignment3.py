"""
***1. Indexing***

Write code for retriving values from list by indexing and print a statement message for given lists

"""
print("1. INDEXING\n")

studentData = ['Ahmed', 'Bilal', 'Government College University', 'Computer Science', 'BS', 50000,'28 Januray 2020', '05 February 2020']

output = "\'Hello {} {},\nYour application is accepted for admission in \"{} {}\" in {}.\nYou have to submit fee {} before {}.\nYour classes will start from {}.\nThanks\'".format(studentData[0],studentData[1],studentData[4],studentData[3],studentData[2],studentData[5],studentData[6],studentData[7])

print(output)



"""
***2. Slicing***

You have a list of cities given as follows. Use positive and negative slicing methods to print out following outputs:

"""

cities = ["Faisalabad", "Lahore", "Islamabad", "Peshawar", "Quetta", "Sahiwal", "Rawalpindi", "Sialkot"]

# POSITIVE SLICING 

S1 = cities[:4]
S2 = cities[2:6]
S3 = cities[5:8]

print("\n2. SLICING")

print("\nPositive Slicing:")
print(S1)
print(S2)
print(S3)

# NEGATIVE SLICING 

S4 = cities[-4:-1]
S5 = cities[-5:]

print("\nNegative Slicing:")
print(S4)
print(S5)



"""
***3. Update Lists***

You have a list of student information. You need to update it for following statements

studentData = ["Ali Raza", 22, 91.24, "Computer Science", 5, "University of Agriculture"]
Add values to this list using append

1. '20 February 2019'
2. 8
Use insert method to insert at specific index

1. 25000 at index 4
2. 'M. Iqbal' at index 1
Update list using list update method:

1. Change Name from 'Ali Raza' to 'Zohaib Ali'
2. Change No of subjects from 5 to 7
Remove values from list using remove method

1. 'Computer Science'
2. 91.24
Remove using pop method

1. Last value from list
2. value at 3rd index
"""

studentData = ["Ali Raza", 22, 91.24, "Computer Science", 5, "University of Agriculture"]

print("\n3. UPDATE LISTS\n")

# APPEND()
print("append() Method:")
studentData.append("20 February 2019")
studentData.append(8)

print(studentData)

# INSERT()
print("\ninsert() Method:")
studentData.insert(4, 25000)
studentData.insert(1, "M. Iqbal")

print(studentData)

# UPDATING LIST METHOD
print("\nUpdating a List Method:")
studentData[0] = "Zohaib Ali"
studentData[6] = 7

print(studentData)

# REMOVING ELEMENTS FROM LIST
print("\ndel & remove() Methods:")
studentData.remove("Computer Science")      #It just removes first occurrence that it founds in a list, however there would be more alike it.
del studentData[-7]                         #It removes an element from a specific index.

print(studentData)

# REMOVING ELEMENTS USING POP() METHOD
print("\npop() Method:")
studentData.pop()                           #Without any parameters, it would remove last value from List, by default.
studentData.pop(2)                          #Index 2 = 3rd Index of list

print(studentData)



"""
***4. Multidimensional list tasks***

You have given data of an employee

employeeData = [["Ali", 35000, "Software Engineer"],
				["Talha", 55000, "Product Manager"],
				["Nasir", 79000, "Computer Engineer"],
				["Khalid", 44000, "DBA"]]

For Loop Tasks
1. Print name of employees with salary greater than 50000.
2. Calculate total salary of all employees.

List update tasks
1. Change salary of nasir from 79000 to 90000 and designation to "Product Manager"
2. Change salary of Khalid to 50000
"""

employeeData = [["Ali", 35000, "Software Engineer"],
				["Talha", 55000, "Product Manager"],
				["Nasir", 79000, "Computer Engineer"],
				["Khalid", 44000, "DBA"]]

print("\n4. MULTIDEMENSIONAL LIST TASKS\n")

print("For Loop Tasks:\n")

print("Employees with Salary greater than 50000:")
for data in employeeData:
    if data[1] > 50000:
        print(data[0])

totalSalary = 0
for sal in employeeData:
    totalSalary += sal[1]
print("\nTotal Salary of Employees:",totalSalary)

print("\nList Update Tasks:")

employeeData[2][1] = 90000
employeeData[2][2] = "Product Manager"

print(employeeData)



"""
***5. Login User***

You have given some users data. 
You have to write a script to check if username and password are correct. 
If username and password are correct. Then you have to check if email is verified or not. 
If it is verified then print Login Succeed else print Email not verified. 
If username or password are incorrect you have to print Incorrect Login details

# Data 1
username = "faizan1214"
password = "qwerty"
emailVerified = False

# Data 2
username = "faizan1214"
password = "qwerty"
emailVerified = True
"""

print("\n5. LOGIN USER")

username = "faizan1214"
password = "qwerty"
emailVerified = False

if username == "faizan1214" and password == "qwerty":
    if emailVerified == True:
        print("\nLogin Succeed")
    else:
        print("\nEmail not verified")
else:
    print("\nIncorrect Login details")


username = "faizan1214"
password = "qwerty"
emailVerified = True

if username == "faizan1214" and password == "qwerty":
    if emailVerified == True:
        print("\nLogin Succeed")
    else:
        print("\nEmail not verified")
else:
    print("\nIncorrect Login details")