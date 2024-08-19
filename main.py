import random

COLORS = ["B", "R", "Y", "G", "O", "W"]
TRIES = 10
CODE_LENGTH = 4


def generate_code():
    code = []

    for _ in range(CODE_LENGTH):  # anon place-holder for when it doesn't matter
        color = random.choice(COLORS)
        code.append(color)

    return code


def guess_code():
    while True:

        guess = input("Guess: ").upper().split(" ")

        if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors.")
            continue  # will return to star of while loop

        for color in guess:
            if color not in COLORS:
                print(f"Invalid color: {color}. Try again.")
                break  # breaks out of for loop, returns to start of while loop
        else:
            break  # if break from for loop was encountered, will break out of while loop

    return guess


def check_code(guess, real_code):
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1

    for guess_color, real_color in zip(guess, real_code):  # take the two args and turn to tuple list
        # subtract correct color from checking stage
        if guess_color == real_color:
            correct_pos += 1
            color_counts[guess_color] -= 1  # to mark color is at right position

    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1

    return correct_pos, incorrect_pos


def game():
    print(f"Welcome to mastermind, you have {TRIES} to guess the code....")
    print("The valid cors are", *COLORS)

    code = generate_code()
    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == CODE_LENGTH:
            print(f"You guess the code in {attempts} tries!")
            break

        print(f"Correct Positions: {correct_pos} | Incorrect_pos: {incorrect_pos}")

    else:
        print("You ran out of tries, the code was: ", *code)


if __name__ == "__main__":
    game()
