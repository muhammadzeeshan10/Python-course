print("******************Calculate Compound Interest************************")
# Enter Principle,Rate,Time
p=int(input("Enter Principle::"))
r=int(input("Enter Rate:"))
t=int(input("Enter Time:"))
# Formula
cl:float= p* (1 + r/100)**t - p
# final Result
print("Your Compound intresr is:",cl)