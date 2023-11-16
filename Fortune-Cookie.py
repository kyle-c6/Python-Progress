import random

luckyNumber = random.randint(1,99)

fortune = random.randint(1,3)

fortuneText = ""

if fortune == 1:
  fortuneText = "You will have a great day!"
if fortune == 2:
  fortuneText = "You will be a tough but rewarding day!"
if fortune == 3:
  fortuneText = "You will have an inspiring day!"


print(f"{fortuneText} Your Lucky Number is: {luckyNumber}")
