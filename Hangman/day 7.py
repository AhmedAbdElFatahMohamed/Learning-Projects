import random
import os
from hangman_art import stages,logo
from hangman_words import word_list

word=random.choice(word_list)
length=len(word)
display=[]
used_letters=[]
lives=6
print(logo)

for letter in word:                                             #display under score for each letter
    display+="_"

end_game=False

while not end_game:
    guess=input("guess a letter: ").lower()
    os.system('clear')

    if guess in used_letters:
        print(f"you already used this letter\nused letters {used_letters}")

    else:
        used_letters+=guess
        for index in range(length):                                 #replace underscore with the letter
            letter=word[index]                                      #get the letter variable
            if guess== letter:
                display[index]=letter
        if guess not in word:
            lives=lives-1
            print(f"'{guess}' is not in the word, you have {lives} lives left")
            if lives == 0:
                end_game=True
                print("you have no more lives, you lost")
                print(f"the word was '{word}'")
    print(f"{' '.join(display)}")                              #display as better visuals instead of list

    print(stages[lives])

    if "_" not in display and lives>0:
        end_game = True
        print("You win.")


