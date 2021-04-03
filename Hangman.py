#Hangman
# To Do Build out Hangman View
# Add ability to save score with a passwor
# More testing
# Add to Git 

import urllib.request, urllib.parse, urllib.error
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

def getWordDef():
    url = 'https://www.randomword.com'
    req = Request(url , headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(req).read()

    soup = BeautifulSoup(page, 'html.parser')
    random_Word = soup.find("div", {"id": "random_word"})
    random_Word_Def = soup.find("div", {"id": "random_word_definition"})
    random_Word = random_Word.text
    random_Word_Def = random_Word_Def.text
    return (random_Word, random_Word_Def)

# Global Variables
newWord = getWordDef()
word = newWord[0]
wordDef = newWord[1]
guessed_Letters = []
wrong_Letters = []
correct_Letters = []
num_Incorrect = 6
letIndex = None
guessedWord = "_" * len(word)
gameCount = 0
name = ""
wins = 0
loss = 0

def newGame():
    global gameCount, word, wordDef, guessed_Letters, wrong_letters, num_Incorrect, guessedWord
    if gameCount == 0:
        name = input('Enter your name: ')
        print('Welcome', name)
    newWord = getWordDef()
    word = newWord[0]
    wordDef = newWord[1]
    guessed_Letters.clear()
    wrong_Letters.clear()
    correct_Letters.clear()
    num_Incorrect = 6
    letIndex = None
    guessedWord = "_" * len(word)
    gameCount += 1
    
def userScore(result):
    global wins, loss
    if result == 1:
        wins += 1
    else:
        loss += 1

def correctLetter():
    global word, correct_Letters, guessedWord
    print('Correct!')
    correct_Letters.append(letter)
    splitWord = list(word)
    splitGuessed = list(guessedWord)
    indexCount = 0
    for i in splitWord:
        if i.lower() == letter.lower():
            letIndex = indexCount 
            splitGuessed[letIndex] = letter
            guessedWord = "".join(splitGuessed)
        indexCount += 1

def incorrectLetter():
    global wrong_letters, num_Incorrect
    num_Incorrect -= 1
    print('Incorrect - guesses left:', num_Incorrect)
    wrong_Letters.append(letter)
    
newGame()

while num_Incorrect > 0:
    if guessedWord == word:
        userScore(1)
        print('Congrats', name, 'You''ve won!')
        print('The word', word, 'means:', wordDef)
        print('Current score. Wins:', wins, 'Losses: ', loss)
        playAgain = input('Play Again? (Y/N)')
        if playAgain == 'Y':
            newGame()
        if playAgain == 'N':
            num_Incorrect = 0
            quit()
    print(guessedWord)
    if len(correct_Letters) > 0:
        print('Current correct letters: ', correct_Letters)
    if len(wrong_Letters) > 0:
        print('Current wrong letters: ', wrong_Letters)
    print('The actual word is: ', word)
    letter = input('Enter letter: ')
    if len(letter) > 1:
        print('Please only enter one letter!')
        continue
    if letter in guessed_Letters:
        print("You've already guessed that letter")
        continue
    guessed_Letters.append(letter)
    if letter.lower() in word.lower():
        correctLetter()
    if letter.lower() not in word.lower():
        incorrectLetter()
        if num_Incorrect == 0:
            userScore(0)
            print("You've used all your guesses!")
            print('The word was', word, 'and it means:', wordDef)
            print('Current score. Wins:', wins, 'Losses: ', loss)
            playAgain = input('Play Again? (Y/N)')
            if playAgain == 'Y':
                newGame()
                continue
            if playAgain == 'N':
                  num_Incorrect = 0
                  continue
        continue
    print('\n' * 100)



