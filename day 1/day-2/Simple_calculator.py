print("SIMPLE CALCULATOR")
while True:
    print("/n Select Operations")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Divison")
    print("5.close the calculator")

    choice=input("Enter your choice(1-5): ")
    if choice=='5':
        print("Calculator is closed")
        break

    n1=int(input("Enter the first number: "))
    n2=int(input("Enter the Second number: "))

    if choice=='1':
        print("Result: ",n1+n2)

    if choice=='2':
        print("Result: ",n1-n2)

    if choice=='3':
        print("Result: ",n1*n2)

    if choice=='4':
        if n2==0:
            print("Error: division by zero is not allowed")
        else:
            print("Result:",n1/n2)
print("Invalid choice")                

    



