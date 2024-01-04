import winsound

hour = int(input())
minutes = int(input())
seconds = int(input())

tim = f"{hour}:{minutes}:{seconds}"

for h in range(0, 24, 1):
    for m in range(0, 60, 1):
        for s in range(0, 60, 1):
            timer = f"{h}:{m}:{s}"
            print(timer)
            if timer == tim:
                winsound.Beep(1500, 2000)
                exit()