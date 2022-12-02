scores = {
  "A X": 4, # Rock vs. Rock (Tie + 1)
  "A Y": 8, # Rock vs. Paper (Win + 2)
  "A Z": 3, # Rock vs. Scissors (Loss + 3)
  "B X": 1, # Paper vs. Rock
  "B Y": 5, # Paper vs. Paper
  "B Z": 9, # Paper vs. Scissors
  "C X": 7, # Scissors vs. Rock
  "C Y": 2, # Scissors vs. Paper
  "C Z": 6, # Scissors vs. Scissors
}

with open("inputs/day2.txt") as f:
  total_score = 0
  for combo in f:
    total_score += scores[combo.strip()]

print(total_score)

scores2 = {
  "A X": 3, # Rock Lose Scissors
  "A Y": 4, # Rock Draw Rock
  "A Z": 8, # Rock Win Paper
  "B X": 1, # Paper Lose Rock
  "B Y": 5, # Paper Draw Paper
  "B Z": 9, # Paper Win Scissors
  "C X": 2, # Scissors Lose Paper
  "C Y": 6, # Scissors Draw Scissors
  "C Z": 7, # Scissors Win Rock
}

with open("inputs/day2.txt") as f:
  total_score = 0
  for combo in f:
    total_score += scores2[combo.strip()]

print(total_score)