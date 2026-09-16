num=int(input("Enter a number for even and odd check: "))
if num%2==0:
    print("Even")
else:
    print("Odd")


a=int(input("Enter a number for greater check: "))
b=int(input("Enter another number for greater check: "))
c=int(input("Enter a third number for greater check: "))
if a > b:
    print("This no,", a, "is greater")
elif b > c:
    print("This no,", b, "is greater")
elif c > a:
    print("This no,", c, "is greater")


a=int(input("Enter a number for divisibility check: "))
if a%7==0:
    print("This number is divisible by 7.")
else:
    print("This number is not divisible by 7.") 