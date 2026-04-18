while True:
    print("\n ---CALCULATOR---\n")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiplication")
    print("4.Divide")
    print("5.Exit")
    choice = int(input("Enter choice(1-5): "))
    if choice == 5:
        print("Calculator closed")
        break
    if choice in [1, 2, 3, 4]:
        try:
            num1 = float(input("Enter number 1: "))
            num2 = float(input("Enter number 2: "))
            if choice == 1:
                print('%.2f + %.2f = %.2f' % (num1, num2, num1 + num2))
            elif choice == 2:
                print('%.2f - %.2f = %.2f' % (num1, num2, num1 - num2))
            elif choice == 3:
                print('%.2f * %.2f = %.2f' % (num1, num2, num1 * num2))
            elif choice == 4:
                if num2 != 0:
                    print('%.2f / %.2f = %.2f' % (num1, num2, num1 / num2))
                else:
                    print("Can't divide by zero")
        except:
            print("Invalid! Enter numbers only")
    else:
        print("Enter correct choice")
