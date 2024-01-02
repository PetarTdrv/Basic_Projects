import random

words = ['Elephant', 'Computer', 'Rainbow', 'Guitar', 'Sunshine', 
        'Butterfly', 'Chocolate', 'Mountain' 'Adventure', 'Universe',
        'Pumpkin Galaxy', 'Bicycle', 'Jazz', 'Keyboard', 'Trampoline',
        'Parrot', 'Waterfall', 'Firefly', 'Lighthouse']

random_word = random.choice(words)

tries = input()

if tries == random_word:
    print("Good job getting the word out!")
    exit()
elif tries != random_word:
    print("Wrong word!")
    while tries != random_word:
        tries = input()
        if tries == random_word:
            print("Good job getting the word out!")
            exit()
        else:
            print("Wrong word!")

        if tries == "Stop":
            break
