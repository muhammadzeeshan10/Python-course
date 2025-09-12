#  Task 05  
#  Loop Manipulation

# print 10 number using while
for i in range(1,10):
    number=int(input(f"Enter your {i} Number:"))


# Take input from user and print even number
enter=int(input("Enter Number :"))
if enter%2==0:
    print("Your Number is Even:")
elif enter%2==1:
    print("Your Number is Odd: ")
else:
    print("You Enter Wrong Number:")


from sympy import isprime
print("Check Prime Number:")
enter=int(input("Enter your Number:"))
print(isprime(enter))


table=int(input("Enter Number for Choose your Table:"))
for i in range(1,11):
    product=table*i
    print(f"{table}*{i}={product}")

# -------------------------------------------------------------------
# Task 01
# String Manipulation
firsts=[]
first=str(input("Enter Your First Name:"))
print(f"Count Occurance of {len(first)}")
middle=str(input("Enter Your Middle Name:"))
print("Count Occurance of Middle :",len(middle))
last=str(input("Enter Your Last Name:"))
print("Count Occurance of Middle :",len(last))


# Reverse String 
last_rev=last[::-1]
print(last_rev)
 
first_rev=first[::-1]
print(first_rev)

middle_rev=middle[::-1]
print(middle_rev)


# split String Throgh hyphen
first_split=first.split()
print(first_split)

middle_split=middle.split()
print(middle_split)

last_split=last.split()
print(last_split)


# Remove Punctuation
import re 
cleaned_first = re.sub(r'[^a-zA-Z0-9\s]', '', first)
print(cleaned_first)

cleaned_middle = re.sub(r'[^a-zA-Z0-9\s]', '', middle)
print(cleaned_middle)

cleaned_last = re.sub(r'[^a-zA-Z0-9\s]', '', last)
print(cleaned_last)

# ---------------------------------------------
# Task 02

# List Manipulation
namee=[]
name=str(input("Enter Your Name:"))
print(name)
print(name[::-1])

namee.append(name)
print(namee)

# Remove Empty String
if "" in namee:
    namee.remove("")
print(namee)

# Add new Name/Number in List:
newitem=str(input("Enter Name Which You want to add:"))
afteritem=str(input("Enter Name Which you want to add in List After:"))
if afteritem in namee:
    index=namee.index(afteritem)
    namee.insert(index+1,newitem)
else:
    print("Not Found")

print("after",namee)

