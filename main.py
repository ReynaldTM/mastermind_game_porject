import random

COLORS = ["B", "R", "Y", "G", "O", "W"]
TRIES = 10
CODE_LENGTH = 4
def generate_code():
    code = []

    for _ in range(CODE_LENGTH): # anon place-holder for when it doesn't matter
        color = random.choice(COLORS)
        code.append(color)

    return code

def guess_code():

    while True:

        guess = input("Guess: ").upper().split(" ")

        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors.")
            continue # will return to star of while loop

        for color in guess:
            if color not in COLORS:
                print(f"Invalid color: {color}. Try again.")
                break # breaks out of for loop, returns to while loop
        else:
            break # if break from for loop was encountered, will break out of while loop

    return guess

def check_code(guess, real_code):
