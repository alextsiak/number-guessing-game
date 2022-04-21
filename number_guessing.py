import random

difficulty = "easy" #default difficulty
mode = 0 #default mode

def startGame(diff):
    if diff == "normal":
        maxNum = 100
    elif diff == "hard":
        maxNum = 1000
    elif diff == "ultra":
        maxNum = 1000000
        print("[SECRET ULTRA BEAST HARD MODE ENABLED]")
    else:
        maxNum = 10 #baby mode. for babies.
    number = random.randint(1, maxNum)
    try:
        guess = int(input(f"Okay! I'm thinking of a number between 1 and {maxNum}. Give me your best guess!\n"))
    except:
        print("Hey, that wasn't a number!")
    else:
        while guess != number:
            if guess > number:
                print("You need to go lower!")
            elif guess < number:
                print("You need to go higher!")
            guess = int(input("Try again:\n"))
        print(f"Congrats! It's {guess}!")

def main():
    print("Welcome to the number guessing game!")
    difficulty = input("Select difficulty (type 'easy', 'normal' or 'hard'):\n").lower()
    startGame(difficulty)

if __name__ == "__main__":
    main()