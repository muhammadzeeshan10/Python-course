# Using For Loop
    # Your choice to For Loop run 1 to n times
for i in range(5):
    print("Enter Student Name ",i+1,)
    # Enter Name according to for loop time
    name=str(input("Enter Name"))


# --------------------------------------------------------\
#  Example Enter Five Students Marks and Calculate Average
print("**************Enter Five Students Number They obtain in physics subject************")
sum=0
for i in range(5):
    print("Enter Student ",i+1," Marks:")
    mark=int(input("Enter Marks:"))
    sum+=mark
print("Calculate Avergae")
avg=sum/5
print("Your avg of All Marks is:",avg)
