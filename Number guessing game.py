import random
num = random.randint(1,100)
while True:
    try:
        guess = int(input("Guess a num: "))
        if guess == num:
            print("You Won")
            break
        elif guess< num:
            print("High")
        else:
            print("Lower")
    except:
        print("Enter valid number")
