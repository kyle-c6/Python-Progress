import random

bingoCard = []

BNumbers = []
INumbers = []
NNumbers = []
GNumbers = []
ONumbers = []

while len(BNumbers) < 5:
  number = random.randint(1,15)
  if number in BNumbers:
    number = random.randint(1,15)
  else:
    BNumbers.append(number)

while len(INumbers) < 5:  
  number = random.randint(16,30)
  if number in INumbers:
    number = random.randint(16,30)
  else:
    INumbers.append(number)

while len(NNumbers) < 4:
  number = random.randint(31,45)
  if number in NNumbers:
    number = random.randint(31,45)
  else:
    NNumbers.append(number)

while len(GNumbers) < 5:
  number = random.randint(46,60)
  if number in GNumbers:
    number = random.randint(46,60)
  else:
    GNumbers.append(number)

while len(ONumbers) < 5:
  number = random.randint(61,75)
  if number in ONumbers:
    number = random.randint(61,75)
  else:
    ONumbers.append(number)

def pretty():
  for row in bingoCard:
    print(f"{row[0]:^5}{row[1]:^3}{row[2]:^5}{row[3]:^3}{row[4]:^5}{row[5]:^3}{row[6]:^5}{row[7]:^3}{row[8]:^5}")
    print("-------------------------------------")

bingoCard = [
["B"," | ","I"," | ","N"," | ","G"," | ","O"],
[BNumbers[0]," | ",INumbers[0]," | ",NNumbers[0]," | ",GNumbers[0]," | ",ONumbers[0]],
[BNumbers[1]," | ",INumbers[1]," | ",NNumbers[1]," | ",GNumbers[1]," | ",ONumbers[1]],
[BNumbers[2]," | ",INumbers[2]," | ","BINGO"," | ",GNumbers[2]," | ",ONumbers[2]],
[BNumbers[3]," | ",INumbers[3]," | ",NNumbers[2]," | ",GNumbers[3]," | ",ONumbers[3]],
[BNumbers[4]," | ",INumbers[4]," | ",NNumbers[3]," | ",GNumbers[4]," | ",ONumbers[4]]
]

pretty()
