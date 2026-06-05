print("Program starts...")

try:
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))

    c = a // b   # Integer division like Java

    print("The division of", a, "and", b, "is", c)

except ValueError:
    print("Error in data : Number not provided correctly")

except ZeroDivisionError:
    print("Error in data : Divisor should not be zero")

except Exception as e:
    print("Error in data :", e)

print("Program ends...")