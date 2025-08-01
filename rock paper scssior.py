import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def get_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0
    round_number = 1

    print("🎮 Welcome to Rock, Paper, Scissors!")
    print("Instructions: Type 'rock', 'paper', or 'scissors' to play. Type 'exit' to quit.")

    while True:
        print(f"\n--- Round {round_number} ---")
        user_choice = input("Your choice: ").lower()

        if user_choice == 'exit':
            print("\n👋 Thanks for playing!")
            print(f"Final Score ➤ You: {user_score} | Computer: {computer_score}")
            break

        if user_choice not in ['rock', 'paper', 'scissors']:
            print("❌ Invalid input. Please choose rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()
        print(f"🤖 Computer chose: {computer_choice}")

        winner = get_winner(user_choice, computer_choice)

        if winner == "tie":
            print("⚖️ It's a tie!")
        elif winner == "user":
            print("✅ You win this round!")
            user_score += 1
        else:
            print("❌ Computer wins this round!")
            computer_score += 1

        print(f"Score ➤ You: {user_score} | Computer: {computer_score}")
        round_number += 1

# Run the game
play_game()

