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
    guess = input("Guess: ").upper().split(" ")
    
