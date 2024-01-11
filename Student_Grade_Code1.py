print("Hello student")
while True:
    marks = float(input("Enter your number between 0-100:   "))
    if 90 <= marks <= 100 :
        print("Your Grade is: A\n")
    elif 80 <= marks <= 89 :
        print("Your Grade is: B\n")
    elif 70 <= marks <= 79 :
        print("Your Grade is: C\n")
    elif 60 <= marks <= 69 :
        print("Your Grade is: D\n")
    elif 00 <= marks <= 59 :
        print("Your Grade is: F\n")
    else:
        print("Invalid Value\n     Enter Again\n")
