import random

HANGMAN_PICS = ['''
+---+
    |
    |
    |
   ===''', '''
+---+
 0  |
    |
    |
   ===''', '''
 +---+
 0   |
 |   |
     |
    ===''', '''
  +---+
  0   |
 /|   |
      | 
     ===''', '''
 +---+
  0  |
 /|\ |
     |
    ===''', '''
 +---+
 0   |
/|\  |
/    |
    ===''', '''
 +---+
 0   |
/|\  |
/ \  |
    ===''', '''
 +---+
[0   |
/|\  |
/ \  |
    ===''', '''
 +---+
[0]  |
/|\  |
/ \  |
    ==='''
]



words = '''аист красный оранжевый желтый зеленый синий голубой фиолетовый белый черный коричневый акула бабуин баран 
барсук бобр бык верблюд волк воробей ворон выдра голубь гусь жаба зебра змея индюк кит кобра коза козел койот корова 
кошка кролик крыса курица лама ласка лебедь лев лиса лосось лось лягушка медведь моллюск моль мул муравей мышь норка 
носорог обезьяна овца окунь олень орел осел панда паук питон попугай пума семга скунс собака сова тигр тритон тюлень 
утка форель хорек черепаха ястреб ящерица зебра тюлень машина'''.split()

def getWord(wordList):
    wordIndex = random.randint(0, len(wordList) - 1)
    return (wordList[wordIndex])

def display (missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Неправильные буквы: ', end='')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i + 1:]

    for letter in blanks:
        print(letter, end='')
    print()


def getGuess(alreadyGuessed):
    while True:
        print("Введите букву: ")
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Пожалуйта введите одну букву')
        elif guess in alreadyGuessed:
            print("Вы уже называли эту букву, назовите другую.")
        elif guess not in "абвгдеежзийклмнопрстуфхцчшщъыьэюя":
            print("Пожалуйста введите БУКВУ.")
        else:
            return guess

def playAgain():
    print('Хотите ли вы сыграть еще?')
    return input().lower().startswith('д')

print("В И С Е Л И Ц А")
missedLetters = ''
correctLetters = ''
secretWord = getWord(words)
gameIsDone = False

while True:
    display(missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Да, секретное слово - ' + secretWord)
            gameIsDone = True

    else:
        missedLetters = missedLetters + guess

        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            display(missedLetters, correctLetters, secretWord)
            print('Вы исчерпали все попытки!\nНе угадано букв: ' + str(len(missedLetters)) + ' и угадано букв: ' + str(len(correctLetters)) + '. Было загадано слово "' + secretWord + '".')
            gameIsDone =True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            secretWord = getWord(words)
            gameIsDone = False
        else:
            break