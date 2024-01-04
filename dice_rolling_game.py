import random

numbers = [1, 2, 3, 4, 5, 6]
points = 0

while True:
    random_number = random.choice(numbers)
    print(random_number)

    if 1 < random_number <= 6:
        points += random_number
        cont = input("Do you want to continue (yes/no): ").lower()
        if cont == "yes":
            continue
        elif cont == "no":
            print(points)
            break
    elif random_number == 1:
        points = 0
        print("Sorry, your points was reseted and game ended.")
        print(points)
        break 