import random

def guess_num():
    print("welcome the number guessing game")
    print("i have select a random num between 1 and 50.try guess it")

    secret_num= random.randint(1,100)

    attempts = 0

    while True:
        guess = int (input("enter your guess : "))
        attempts += 1

        #check guess is correct

        if guess == secret_num:
            print(f"congratulations! you guessed the num in {attempts} attemots.")
            break

        elif guess < secret_num:
            print("too low! try again")

        else:
            print("too high! try again")

if __name__ == "__main__":
        guess_num()