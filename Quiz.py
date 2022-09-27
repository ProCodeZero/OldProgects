# Quiz

import random

dictionary = {
    'Square from 4?': '2',
    'The best genre music?': 'Metal',
    'How many suits in Card deck?': '4',
    'Family on English?': 'Family',
    'The color, opposite white?': 'Black',

}


length = len(dictionary.keys())


def ToDo():
    points = 0
    answers = 0
    print('Your points: ' + str(points))
    for i in range(length):
        a = len(dictionary)
        randomChoise = random.randint(0, a - 1)
        key = list(dictionary.keys())[randomChoise]
        value = list(dictionary.values())[randomChoise]
        print('Question: ' + key)
        answer = input('Input your answer: ')
        dictionary.pop(key)
        if answer == value:
            points += 1
            print('Your points: ' + str(points))
            answers += 1
        else:
            print('\nIt\'s wrong answer, right answer is: ' + value)
            print('Sorry, but you\'r lose, your points: ' + str(points) + '\nWould you like to play again?')
            break
    if answers == length:
        print('You win!')
    else:
        print()


again = 'Yes'
print('Hello, nice to meet you my friend, let\'s start the quiz\n')
while again.startswith('Y'):
    ToDo()
    print('\nWould you like to play again?')
    again = input('Yes or No \n')
    again = again.upper()
print('Bye and see you later')
