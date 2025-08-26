import random
from hangman_art import stages, logo

print(logo)

with open("word_list.txt") as file:
  word_list = list(file)

chosen_word = random.choice(word_list).strip().lower()
print(chosen_word)

placeholder = ""

for position in range(len(chosen_word)):
  placeholder += "_"

print(placeholder)

game_finished = False
lives = 6

correct_letters = []

while not game_finished:
  print(f"******************************{lives}/6 LIVES LEFT******************************")
  guess = input("Guess a letter: ").lower()

  if guess in correct_letters:
    print(f"You've already guessed {guess}")

  # Check aussi si c'est une lettre et si il a mis un seul charactère AAAAAAAAAAAAAAAAA

  display = ""

  for letter in chosen_word:
    if letter == guess:
      display += guess
      correct_letters.append(guess)
    elif letter in correct_letters:
      display += letter
    else:
      display += "_"

  if not guess in chosen_word:
    lives -= 1
    print(f"you guessed {guess}, that's not in the word. You lose a life.")

    if lives == 0:
      game_finished = True
      print(f"******************************IT WAS {chosen_word}! YOU LOSE******************************")

  print(display)

  if "_" not in display:
    print(f"******************************YOU WIN******************************")
    game_finished = True
  
  print(stages[lives])
