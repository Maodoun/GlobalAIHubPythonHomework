#Global Ai Hub Ödev #3--- Game----

char = {"ad": "mete", "power": 100, "weapon": "sword", "hp": 100}

char2 = {"ad": "han", "power": 75, "weapon": "sword", "can": 100}

def attack (vuran: char, vurulan: char2):
    eksilen = vuran["power"]
    vurulan["hp"] = vurulan["hp"] - eksilen

def attack2 (vurulan: char, vuran: char2):
    eksilen = vuran["power"]
    vurulan["hp"] = vurulan["hp"] - eksilen

name = str(input("Please enter your name: "))
print(f"Welcome: ", name,"Game is starting now: ")

print("ilk Karakterin Adı: {}".format(char["ad"]))
print("ilk Karakterin Gücü: {}".format(char["power"]))
print("ikinci Karakterin Adı: {}".format(char2["ad"]))
print("ikinci Karakterin Gücü: {}".format(char2["power"]))

attack(char2,char)
attack2(char, char2)

print("First and second chameteracter attacked each other: ")
print("First character hp is:", char["hp"])
print("Second character hp is: ", char2["can"])
quit