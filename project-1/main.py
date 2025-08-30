import random

# Snake Water Gun Game
'''
s -> snake (1)
w -> water (-1)
g -> gun (0)
'''

youstr = input("Enter your choice (s for snake, w for water, g for gun): ")

youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

# convert your choice into number
younum = youDict.get(youstr.lower())

# computer makes a random choice
computer = random.choice([1, -1, 0])

print(f"You chose {reverseDict[younum]}")
print(f"Computer chose {reverseDict[computer]}")

# Game logic
if computer == younum:
    print("It's a Draw!")
elif (computer == 1 and younum == -1):  # snake drinks water
    print("You Lose!")
elif (computer == -1 and younum == 0):  # gun sinks in water
    print("You Lose!")
elif (computer == 0 and younum == 1):   # snake killed by gun
    print("You Lose!")
else:
    print("You Win!")
