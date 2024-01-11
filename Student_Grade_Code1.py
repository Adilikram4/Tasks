print("Hello student")
while True:
    marks = float(input("Enter your number between 0-100:\n "))
    if 90 <= marks <= 100 :
        grade = ("A")
    elif 80 <= marks <= 89 :
        grade = ("B")
    elif 70 <= marks <= 79 :
        grade = ("C")
    elif 60 <= marks <= 69 :
        grade = ("D")
    else:
        00 <= marks <= 59
        grade = ("F")
    print("Your Grade is:", grade)
