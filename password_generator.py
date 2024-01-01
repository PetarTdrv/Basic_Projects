# More or less, but maybe more
import random
 
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '?', '_']
random_symbols = random.choice(symbols)
 
upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
random_upper_letters = random.choice(upper_letters)
 
lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
random_lower_letters = random.choice(lower_letters)
 
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9',]
random_numbers = random.choice(numbers)
 
password = f"{random_upper_letters}{random_lower_letters}{random_numbers}{random_symbols}"
print(password)
