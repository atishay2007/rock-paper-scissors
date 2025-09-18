import random

print("✊ ✋ ✌️ Rock, Paper, Scissors!")
choices = ["rock", "paper", "scissors"]

while True:
    player = input("👉 Your choice (rock/paper/scissors): ").lower()
    if player in choices:
        break
    else:
        print("🤨 Bruh… that’s not a valid move. Try again.")

computer = random.choice(choices)
print(f"Computer chose: {computer}")

if player == computer:
    print("😐 It's a tie!")
elif (player == "rock" and computer == "scissors") \
        or (player == "paper" and computer == "rock") \
        or (player == "scissors" and computer == "paper"):
    print("🎉 You win!")
else:
    print("💀 You lose!")
