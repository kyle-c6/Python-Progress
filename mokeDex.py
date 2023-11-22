import os

mokeDex = {}

def prettyPrint():
  os.system("clear")
  for key, value in mokeDex.items():
    print(key, end=": ")
    for subKey, subValue in value.items():
      print(subKey, subValue, end=" | ")
    print()

def add():
  os.system("clear")
  name = input("mokeBeast Name: ").strip().title()
  element = input("mokeBeast Element: ").strip().title()
  special = input("mokeBeast Special Move: ").strip().title()
  hp = int(input("mokeBeast Starting HP: ").strip())
  ap = int(input("mokeBeast Starting AP: ").strip())
  mokeDex[name] = {"Element":element, "Special":special, "HP":hp, "AP":ap}

while True:
  add()
  more = input("Add another mokeBeast? (y/n): ").strip().lower()
  if more == "y":
    True
  else:
    prettyPrint()
    break
