import random
import os
from hangman import HangMan


# Clear terminal window and enter player's name
os.system("cls" if os.name == "nt" else "clear")
print("\nWelcome to HangMan game\n")
name = input("Enter your name: ")

''' [1] Adding your own wordlist '''
words_to_guess = ["firewall","server","router"]

game = HangMan(name)
while(True):
    word = random.choice(words_to_guess)
    game.playHangManGame(word)

    question = input("Do you want to play again? [y=yes, n=no]: ")
    os.system("cls" if os.name == "nt" else "clear")
    while(question.lower() not in ["y", "n"]):
        question = input("Do you want to play again? [y=yes, n=no]: ")
    if(question.lower() != "y"):
        break

print(f"Thank you {name} for playing HangMan game")