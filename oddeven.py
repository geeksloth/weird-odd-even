number = input("input: ")
try:
    number = int(number)
except:
    print("invalid")

if number == 0:
    print("Zero")
else:
    if (number % 2) == 0:
        print("Even")
    else:
        print("Odd")
