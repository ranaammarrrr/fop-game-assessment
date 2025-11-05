import random

def play():
    """Main function to play Rock-Paper-Scissors game."""
    choices = ["rock", "paper", "scissors"]
    wins, losses, ties, round_number = 0, 0, 0, 1

    while True:
        print(f"\n--- Round {round_number} ---")
        round_number += 1
        player = input("Enter rock, paper, or scissors (or 'quit' to exit): ").strip().lower()

        if player == "quit":
            print(f"Final Score -> Wins: {wins}, Losses: {losses}, Ties: {ties}")
            print("Thanks for playing!")
            break

        if player not in choices:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue

        computer = random.choice(choices)
        print(f"Computer chose: {computer}")

        if player == computer:
            print("It's a tie!")
            ties += 1
        elif (player == "rock" and computer == "scissors") or \
             (player == "paper" and computer == "rock") or \
             (player == "scissors" and computer == "paper"):
            print("You win!")
            wins += 1
        else:
            print("You lose!")
            losses += 1

if __name__ == "__main__":
    play()
