
from random import choice

while True:
    print("what do you want to do ?")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4. Division")
    print("Enter Q to exit")

    choice = input("Enter your choice:")
    if choice == "q" or choice == "Q":
        break
    
    num1 = float(input("Enter first number : "))
    num2 = float(input("Enter second number : "))

    if choice == '1':
        print("Result:"+ str(num1 + num2))
        print("--------------------------")
    elif choice == '2':
        print("Result:" + str(num1-num2))
        print("--------------------------")
    elif choice == '3':
        print("result:"+ str(num1*num2 ))
        print("--------------------------")
    elif choice == '4':
         if num2 == 0:
            print("Cannot divide by 0")
         else:
            print("Result :" + str(num1 / num2))
            print("--------------------------")
    else:
        print("Invalid Choice")
