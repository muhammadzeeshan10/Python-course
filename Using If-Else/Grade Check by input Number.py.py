print("*****************Welcome to Github *************")
# Enter Number 
enter=int(input("Enter your Number:"))
#  After Entering Number you check the grade 
print("Check Grade According to this Number:",enter)
# check condition if/elif/else and show the output after condition is True:
if enter>=80:
    print("A+ Grade")
elif enter>=70:
    print("B+ Grade")
else:
    print("Need to Improvement")


# Check Vovle Number
print("Check Vovle Number")
print("Enter Vovle Number, and check this number is Vovle or NOT?")
#  Enter Any Random Number
Vovle=str(input("Enter Alphabet:"))
#  If/Elif Condition Check the number 
if Vovle =='a'or Vovle =='A':
# if the number is matched then show the output below given line
    print("This Number is Belong To vovle")
elif Vovle=='e'or Vovle=='E':
    print("This Number is Belong To vovle")
elif Vovle=='i'or Vovle=='I':
    print("This Number is Belong To vovle")
elif Vovle=='o'or Vovle=='O':
    print("This Number is Belong To vovle")
elif Vovle=='u'or Vovle=='U':
    print("This Number is Belong To vovle")
else:
    print("This Number Can't Belong to Vovle Number:",Vovle)