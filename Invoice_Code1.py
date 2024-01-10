print("Welcome")
while True:
    amount = int(input("Enter your amount: "))
    price = int(input("Enter your purchasing price: "))
    price1 = price*3
    gst = price1/100
    print("3% Tax apply : ", gst)
    a = int(price+gst)
    print ("Your remaining Amount: " , amount - a)
    next_calculation = input("continue shopping? (yes/no): ")
    if next_calculation == "no":
        break
else:
    print("Invalid Input")