#computes a given integer power using a for loop

def power():
    
    print("This program calculates the integer power of a given value using a for loop")

    a = int(input("Enter the Integer:"))

    b = int(input("Enter the power value:"))
    
    c=1 #determines how many times thee for loop runs

    for n in range (c):

        c = a**b

        print("The answer is:",c)

power()
