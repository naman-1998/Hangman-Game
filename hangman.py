import random
import time


def playGame(count,display,word):
    limit=7
    length=len(word)
    wrongLetters=''
    guess=''
    while True:
        print("Word :"+display)
        while True:
            guess=input("Enter your guess: ")
            if len(guess)==1 and guess.isalpha()==True:
                break
        if guess in word:
            for index in range(len(word)):
                if word[index]==guess:
                    word=word[:index] + "*"+word[index+1:]
                    display=display[:index]+guess+display[index+1:]
            print(display)
        elif guess in wrongLetters:
            print("You have already typed this letter!")
        else:
            wrongLetters=wrongLetters +guess
            count+=1
            if count==1:
                print("Wrong Input. "+str(limit-count)+" guess remaining")
                print("   __________ \n"
                    "   |      |     \n"
                    "   |            \n"
                    "   |            \n"
                    "   |            \n"
                    "   |            \n"
                    " __|__          \n"
                    )
            elif count==2:
                print("Wrong Input. "+str(limit-count)+" guess remaining")
                print("   __________ \n"
                    "   |      |     \n"
                    "   |      O     \n"
                    "   |            \n"
                    "   |            \n"
                    "   |            \n"
                    " __|__          \n"
                    )
            elif count==3:
                print("Wrong Input. "+str(limit-count)+" guess remaining")
                print("   __________ \n"
                    "   |      |     \n"
                    "   |      O     \n"
                    "   |      |     \n"
                    "   |            \n"
                    "   |            \n"
                    " __|__          \n"
                    )
            elif count==4:
                print("Wrong Input. "+str(limit-count)+" guess remaining")
                print("   __________ \n"
                    "   |      |     \n"
                    "   |      O     \n"
                    "   |     /|     \n"
                    "   |            \n"
                    "   |            \n"
                    " __|__          \n"
                    )
            elif count==5:
                print("Wrong Input. "+str(limit-count)+" guess remaining")
                print("   __________ \n"
                    "   |      |     \n"
                    "   |      O     \n"
                    "   |     /|\    \n"
                    "   |            \n"
                    "   |            \n"
                    " __|__          \n"
                    )
            elif count==6:
                print("Wrong Input. "+str(limit-count)+" guess remaining")
                print("   __________ \n"
                    "   |      |     \n"
                    "   |      O     \n"
                    "   |     /|\    \n"
                    "   |     /      \n"
                    "   |            \n"
                    " __|__          \n"
                    )
            elif count==7:
                print("Wrong Input. You are hanged")
                print("   __________ \n"
                    "   |      |     \n"
                    "   |      O     \n"
                    "   |     /|\    \n"
                    "   |     / \    \n"
                    "   |            \n"
                    " __|__          \n"
                    )
                break

        if word== '*'*length:
            print  ("Congrats! You have guessed it successfully...")
            break
        

def pick_word():

    filePath = 'words.txt'
    file = open(filePath, 'r')
    words = []

    for line in file:
        line = line.rstrip('\n')
        if len(line) >= 3:
            words.append(line.lower())

    file.close()

    word = random.choice(words)
    return word


def main():
    gameEnd = False
    
    name=input("What is your name: ")
    print("Welcome "+ name )
    time.sleep(1)
    
    while gameEnd == False:
        word=pick_word();
        count=0
        length=len(word)
        display='*' * length
        playGame(count,display,word)

        while True:
            decision = input('Would you like to play again? (y or n): ').lower()
            if decision == 'y':
                break
            if decision == 'n':
                gameEnd = True
                break

if __name__ == '__main__':
    main()
