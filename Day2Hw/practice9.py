import random
rndm = random.randint(1,9)
guess = 0
guesses = 0
while guess != rndm and guess != "exit":
    guess = input("enter a guess between one and 9 ")
    if guess == "exit":
        break

    guess = int(guess)
    guesses += 1
    if guess < rndm:
        print("Too Low") 
    elif guess > rndm:
        print("Too High")
    else:
        print("Correct!")
        print("You only took", guesses, "tries!")
input()