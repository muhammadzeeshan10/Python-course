print("**************************Calculate Profit and Loss **************************")
# profit
cost=float(input("Enter the price of Cost:"))
selling=float(input("Enter Selling Price"))
profit:float=cost-selling


if cost>selling:
    print("your Profit is:",profit)
else:
    print("Your loss is:",profit)

