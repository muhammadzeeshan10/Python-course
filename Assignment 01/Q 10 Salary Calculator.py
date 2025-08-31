# Salary Calculator
HRA=0
DA=0
basic=0
Total_Salary=0
print("*******************Calculate Basic Salary*****************")
print("Enter:")
HRA=float(input("Enter your House Allownce"))
DA=float(input("Enter your Dearness Allownace"))
basic=float(input("Enter your Basic Salary"))

Total_Salary=HRA+DA+basic
print("Your Total Salary is:",Total_Salary)