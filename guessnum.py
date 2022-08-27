from itertools import count
import random
name = input("Enter your name.")
print("Enter the range you want:")
start , end = map(int , input().split('-'))

a = random.randint(start , end)
print(f"Guess the number between {end} to {start} - ")
count = 0
score = 50

while (score!=0):
    guess = int(input("Guess the number:"))
    if a == guess:
        print(f"You the correct no. in{count} guesses.")
        print(f"you got{points} points.")
    else:
        points = points - 5
        count = count+1
        print ("hint----")
        if a > guess:
            print("Try greater than that number.")
        else:
            print("Try smaller number than that.")
        if(a%2==0):
            print("Try even number")
        else:
            print("Try odd number")
        

