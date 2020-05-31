from hangman_parts import parts
import random
import time
import pyinputplus as pypi 


print("Hi there, Let's play Hangman!")
print("Kindly note that the game is case sensitive.")

def wait():
    for i in range(4):
        print(".", end = '')
        time.sleep(.5)
    print("\n")
ready = pypi.inputYesNo("Are you ready? yes/No: \n")
if "y" in ready:
    print("Great. Lemmie look for a word!")
    wait()
elif "n" in ready:
    print("Oh snap. Well then see you later")
    exit()
words = ["Rick", "Morty", "awesome"]
random_word = random.choice(words)

print('''Foundit! \n
The word contains {} letters. Your goal is to guess 
the right word from them.\nLet's goo!''' .format(len(random_word)))

right_list = ['-'] * len(random_word)
wrong_list = []
print('''The game starts as shown below. But each time you guess
incorrectly, it increases in length''')
parts(len(wrong_list))

def updateList():
    for i in right_list: 
        print(i, end = ' ')

print("\n")
def play():
    trials_left = 6
    while True:
        user_guess = input("Guess a Letter: ")
        if user_guess in random_word and trials_left > 0:
            index = 0
            for each in random_word:
                if each == user_guess:
                    right_list[index] = user_guess
                index += 1  
            print(f"{user_guess} is in the word")
            updateList()
            print()
        elif trials_left > 0:
            if user_guess in wrong_list:
                print("You already guessed that letter.")
            else:
                wrong_list.append(user_guess)
                parts(len(wrong_list))
                print("\n")
                print(f"{user_guess} is not in the word")
                print(f"Hint: {random.choice(random_word)} is a member of that word")
                trials_left -= 1
        elif trials_left <= 0:   
            print("Sorry, but you have run out of trials")
            print(f"I picked {random_word}")
            break
        if "-" not in right_list:
            print("You guessed all of them correct. You win")
       
#def main():
play()
    
       
       
        
            
    

    




