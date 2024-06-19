def calci():
    print("\n                                     ......Welcome to the simple calculator...... \n") 
    print("                               .....Here you can perform your arithmetics operations.....\n")                                

    num1 = float(input("\nEnter the first number: "))
    num2 = float(input("Enter the second number: "))

    while True:
        print("......Select the arithmetic operation......\n")
        print("1. Addition \n")
        print("2. Subtraction \n")
        print("3. Multiplication \n")
        print("4. Division \n")
        print("5. Exit\n")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            result = num1 + num2
            print(f" \nThe addition of {num1} and {num2} is {result}.\n")

        elif choice == 2:
            result = num1 - num2
            print(f" \nThe subtraction of {num1} and {num2} is {result}.\n")

        elif choice == 3:
            result = num1 * num2
            print(f" \nThe multiplication of {num1} and {num2} is {result}.\n")

        elif choice == 4:
            if num2 != 0:
                result = num1 / num2
                print(f" \nThe division of {num1} and {num2} is {result}.\n")
            else:
                print("\nError: Division by zero is not allowed.\n")

        elif choice == 5:
            print("\nExited...\n")
            break

        else:
            print("Invalid input. Please choose between 1 to 4.")

calci()