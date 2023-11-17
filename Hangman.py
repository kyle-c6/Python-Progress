import random, os, time

header = "\033[33mHangman\033[0m"
listOfWords = ["ninja", "bridge", "alligator", "magician", "history", "survival", "banana", "eagle", "allergic", "tornado", "protest", "jedi", "persistence"]
guessed = []
lives = 6
wrongCount = 0

pics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def printPic():
  print(pics[wrongCount])

def printGuesses():
  print("Previous Guesses: ")
  print("\033[31m", end="")
  for i in guessed:
    print(i, end=" ")
  print("\033[0m", end="")

answer = random.choice(listOfWords)

while True:
  time.sleep(2)
  os.system("clear")
  print(f"{header:^25}")
  printGuesses()
  print()
  printPic()
  complete = True # Check if puzzle complete
  for i in answer:
    if i.upper() in guessed:
      print(i.upper(),end=" ")
    else:
      print("_", end=" ")
      complete = False
  print("\n")

  if complete:
    print(f"\033[35mYou Win! You had {lives} lives remaining.\033[0m")
    break

  if lives == 0:
    print(f"\033[31mWomp, Womp. You lose! The answer was \033[32m{answer.upper()}\033[0m")
    break
    
  guess = input("\033[32mGuess a Letter\033[0m > ").lower()
  
  if guess.upper() in guessed:
    print("You've already guessed that!\n\n")
    continue

  guessed.append(guess.upper())
    
  if guess.lower() in answer:
    print("Letter Found")
  else:
    print(f"No {guess.upper()} in the answer.\n")
    wrongCount +=1
    lives -= 1
    print(f"Lives Remaining: {lives}")
