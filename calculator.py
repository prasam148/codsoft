

def add():
    c=a+b
    print(f"Addition of two numbers is {c}")


def sub():
    c=a-b
    print(f"Substraction of two numbers is {c}")


def mul():
    c=a*b
    print(f"Multiplication of two numbers is {c}")


def div():
    c=a/b
    if b==0:
        print("Division by 0 is not allowed")
    else:
        print(f"Division of two numbers is {c}")


def exp():
    c=a**b
    print(f"Exponential of two numbers is {c}")


def mod():
    c=a%b
    print(f"Modulus of two numbers is {c}")


def floor():
    c=a//b
    print(f"Floor Division of a & b is {c}")


print(" ****Calculator Application**** ")
print(" 1. Addition ")
print(" 2. Substraction ")
print(" 3. Multiplication ")
print(" 4. Division ")
print(" 5. Exponential ")
print(" 6. Modulus ")
print(" 7. Floor Division ")

option=int(input("Enter options (1 to 7) for calculation: "))

a=float(input("Enter first value: "))
b=float(input("Enter second value: "))

if option == 1:
    add()
elif option == 2:
    sub()
elif option == 3:
    mul()
elif option == 4:
    div()
elif option == 5:
    exp()
elif option == 6:
    mod()
elif option == 7:
    floor()
else:
    print("Invalid option. please choose valid option (1-7).")


