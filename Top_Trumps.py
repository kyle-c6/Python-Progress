import os,time

header = "Top Trumps"

contestants = {}
stats = ["Intelligence", "Tenacity", "Cleanliness", "Reliabilty"]

def viewContestants():
  for key in contestants:
    print(key)

def add_contestants():
  again = True
  while again == True:
    os.system("clear")
    name = input("What is your contestant's name? ").strip().title()
    if name in contestants.items():
      print("Contestant already exists")
      again = True
    else:
      intel = int(input(f"{name}'s Intelligence: ").strip())        
      ten = int(input(f"{name}'s Tenacity: ").strip())
      cle = int(input(f"{name}'s Cleanliness: ").strip())
      rel = int(input(f"{name}'s Reliability: ").strip())
      contestants[name] = {"Intelligence":intel, "Tenacity":ten, "Cleanliness":cle, "Reliability":rel}
      os.system("clear")
      print(f"{name} has been added.")
      time.sleep(1)
      more = input("Add more contestants? y/n\n").strip().lower()
      if more == "n":
        again = False
      else:
        again = True

def player1_choice():
  global player1
  player1 = ""
  while player1 not in contestants.keys():
    os.system("clear")
    viewContestants()
    print()
    player1 = input("Player 1, choose your contestant: ").strip().title()
    if player1 in contestants.keys():
      print(f"Great! You selected {player1}.")
      time.sleep(1)
      return(player1)
    else:
      print("Contestant does not exist")
      time.sleep(1)

def player2_choice():
  global player2
  player2 = ""
  while player2 not in contestants.keys():
    os.system("clear")
    viewContestants()
    print()
    player2 = input("Player 2, choose your contestant: ").strip().title() #PLAYER 2 CHOOSES CONTESTANT
    if player2 in contestants.keys() and player2 != player1:
      print(f"Great! You selected {player2}.")
      time.sleep(1)
    else:
      print("Invalid selection. Try again.")
      player2 = ""
      time.sleep(1)

def battle():
  global p1_score, p2_score
  os.system("clear")
  for i in stats:
    print(i, end="\n")
  print()
  stat = input("Choose your stat: ").strip().title()
  print()
  if contestants[player1][stat] > contestants[player2][stat]:
    p1_score += 1
    print(f"{player1}'s {stat}: {contestants[player1][stat]}\n{player2}'s {stat} of {contestants[player2][stat]}\n\nPlayer 1 wins the battle!\nThe score is now Player 1: {p1_score} - Player 2: {p2_score}")
    time.sleep(5)
  elif contestants[player1][stat] < contestants[player2][stat]:
    p2_score += 1
    print(f"{player2}'s {stat}: {contestants[player2][stat]}\n{player1}'s {stat}: {contestants[player1][stat]}\n\nPlayer 2 wins the battle!\nThe score is now Player 1: {p1_score} - Player 2: {p2_score}")
    time.sleep(5)


print(f"{header:^30}") #PROGRAM START
time.sleep(1)
print("Rules")
time.sleep(1)
print("1. Choose contestants")
time.sleep(1)
print("2. Alternate choosing which attribute to battle with")
time.sleep(1)
print("3. First to 3 wins")
time.sleep(3)
os.system("clear")
print("Let's find out about our conestants!")
time.sleep(2)


while len(contestants) < 2:
  add_contestants()

  player1_choice()
  player2_choice()

  p1_score = 0
  p2_score = 0
  
  while p1_score < 3 and p2_score < 3: # CHECK FOR WINNER
    battle()
    os.system("clear")
    if p1_score == 3:
      print(f"{player1} wins! Final Score: Player 1: {p1_score} - Player 2: {p2_score}")
      time.sleep(2)
      print()
    elif p2_score == 3:
      print(f"{player2} wins! Final Score: Player 1: {p1_score} - Player 2: {p2_score}")
      time.sleep(2)
      print()
    else:
      print("Next round coming up.")
      time.sleep(1)

  new_game = input("Would you like to play again? y/n ").strip().lower()
  if new_game == "y":
    contestants = {}
    True
  else:
    break
