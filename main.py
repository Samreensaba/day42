title = "MakeBEast"

char = {"Beast Name": None, "Type": None, "special Move": None, "HP": None, "MP": None}

for name, value in char.items():
  char[name] = input(f"{name:}: ").strip().capitalize()



if char["Type"].lower() == "fire":
    print(f"\033[91m", end="")
elif char["Type"].lower() == "water":
    print(f"\033[96m", end="")
elif char["Type"].lower() == "electric":
    print(f"\033[93m", end="")
elif char["Type"].lower() == "earth":
    print(f"\033[32m", end="")
elif char["Type"].lower() == "air":
    print(f"\033[37m", end="")
else:
    print(f"\033[0m", end="")

for name,value in char.items():
    print(f"{name: <15}: {value}")
