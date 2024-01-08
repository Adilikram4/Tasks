print("Hello world")
print("enter your first number")
a = int(input())
print("enter your operator")
b = str(input())
print('Enter your 2nd number')
c = int(input())
if b == "+" :
    print("your ans" , a + c)
elif b =='-':
    print("your ans" , a - c)
elif b =='*':
    print("your ans" , a * c)
elif b =='/':
    print("your ans" , a / c)
else:
    print('dont touch mycode')