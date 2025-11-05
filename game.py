import random

def play():
    choices = ["rock", "paper", "scissors"]
    while True:
        computer = random.choice(choices)
        player = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()

        if player == "quit":
            print("Thanks for playing!")
            break

        if player not in choices:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue

        print(f"Computer chose: {computer}")

        if player == computer:
            print("It's a tie!")
        elif (player == "rock" and computer == "scissors") or \
             (player == "paper" and computer == "rock") or \
             (player == "scissors" and computer == "paper"):
            print("You win!")
        else:
            print("You lose!")

if __name__ == "__main__":
    play()
