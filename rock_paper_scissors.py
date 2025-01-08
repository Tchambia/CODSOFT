import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "user"
    else:
        return "computer"

def display_scores(user_score, computer_score):
    print("\n--- Scores ---")
    print(f"User: {user_score}")
    print(f"Computer: {computer_score}")

def main():
    print("Welcome to Rock-Paper-Scissors!")
    print("Instructions: Type 'rock', 'paper', or 'scissors' to play.")
    print("Type 'exit' to quit the game.")

    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("\nYour choice (rock, paper, scissors): ").lower()
        if user_choice == "exit":
            print("\nThanks for playing! Final scores:")
            display_scores(user_score, computer_score)
            break

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please type 'rock', 'paper', or 'scissors'.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)
        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        display_scores(user_score, computer_score)

        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            print("\nThanks for playing! Final scores:")
            display_scores(user_score, computer_score)
            break

if __name__ == "__main__":
    main()
