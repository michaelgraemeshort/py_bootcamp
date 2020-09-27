from random import choice

title = "Rock, Paper, Scissors"
print("=" * len(title))
print(title)
print("=" * len(title), "\n")
print("Enter 'rock', 'paper', or 'scissors'.\n")
p1 = input("Player one: ").lower()
p2 = choice(["rock", "paper", "scissors"])
print(f"Player two: {p2}")
result = "Player two wins!"
if p1 == "rock" and p2 == "scissors" or p1 == "paper" and p2 == "rock" or p1 == "scissors" and p2 == "paper":
	result = "Player one wins!"
elif p1 == p2:
	result = "Draw."
print(result)