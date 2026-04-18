n1, n2 = map(int, input("Enter two numbers: ").split(","))
op = input("Enter operator: ")
if op == "+":
    print("Result=", n1 + n2)
if op == "-":
    print("Result=", n1 - n2)
if op == "*":
    print("Result=", n1 * n2)
if op == "/":
    print("Result=", n1 / n2)
