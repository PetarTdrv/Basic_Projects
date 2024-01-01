import random
 
random_number = random.randint(1, 101)
number = int(input("Enter the number you think is: "))
while number != random_number:
    number = int(input("Enter the number you think is: "))
    if number == random_number:
        print(f"Well done! You succeeded the number is: {random_number}")
