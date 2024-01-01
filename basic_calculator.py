# Тo use the calculator, you must enter two numbers each on one line, when you enter the "stop" command, the program stops.
 
while True:
    command = input()
    if command == "stop":
        break
    
    first_num = int(command)
    second_num = int(input())
    operation = input()
 
    if operation == "+":
        result = first_num + second_num
        print(f"\n{result}")
    elif operation == "-":
        result = first_num - second_num
        print(f"\n{result}")
    elif operation == "*":
        result = first_num * second_num
        print(f"\n{result}")
    elif operation == "/":
        result = first_num // second_num
        print(f"\n{result}")
