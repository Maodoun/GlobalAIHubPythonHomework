#Global Ai Hub Ödev #3--- Game----
#Önce ödevde serbestsiniz denince bunu yapmıştım ama aşağıda kelime tahmini olarak yapabildim.

#char = {"ad": "mete", "power": 100, "weapon": "sword", "hp": 100}
#char2 = {"ad": "han", "power": 75, "weapon": "sword", "can": 100}

#def attack (vuran: char, vurulan: char2):
    #eksilen = vuran["power"]
    #vurulan["hp"] = vurulan["hp"] - eksilen

#def attack2 (vurulan: char, vuran: char2):
    #eksilen = vuran["power"]
    #vurulan["hp"] = vurulan["hp"] - eksilen

#name = str(input("Please enter your name: "))
#print(f"Welcome: ", name,"Game is starting now: ")

#print("ilk Karakterin Adı: {}".format(char["ad"]))
#print("ilk Karakterin Gücü: {}".format(char["power"]))
#print("ikinci Karakterin Adı: {}".format(char2["ad"]))
#print("ikinci Karakterin Gücü: {}".format(char2["power"]))

#attack(char2,char)
#attack2(char, char2)

#print("First and second chameteracter attacked each other: ")
#print("First character hp is:", char["hp"])
#print("Second character hp is: ", char2["can"])
#quit

#HANGMAN-GUESSİNG WORD-First Try, Learning from the google :D
import random,time

words = ['sandbox', 'computer', 'science', 'programming', 'python', 'mathematics', 'player', 'condition', 'artificial', 'machine', 'board', 'geeks']
word = random.choice(words)

name = input("Please enter your name: ")
print(f"Welcome, {name}","Game is starting soon")
time.sleep(2)

print("Guess the characters")

guesses = ''
turns = 7

while turns > 0:
    failed = 0
    for x in word:
        if x in guesses:
            print(x)
        else:
            print("_")
            failed += 1
    if failed == 0:
        print("You win the Game")
        print("The word is: ", word) 
        break
    guess = input("guess a word:")
    guesses += guess
    if guess not in word:
        turns -= 1
        print("Wrong!")
        print("You have", + turns, "more guesses")
        if turns == 0:
            print("You Lost!")
