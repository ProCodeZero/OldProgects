import random
import time

def intro():
    print("Вы прибыли сюда.... есть две пещеры, в одной норм, а в другой нет, куда вы попадете решает рандом")
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Какую пещеру предпочитаешь?')
        cave = input()

    return cave

def chekCave(chosenCave):
    print('Вы приближаетесь к пещере...')
    time.sleep(2)
    print('Иии...')
    time.sleep(2)
    print('перед вами огромный дракон который...')
    time.sleep(2)
    print()

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('отдает вам все свое барахло')
    else:
        print("Хавает вас")



playAgain = 'да'
while playAgain == 'да':
    intro()
    caveNumber= chooseCave()
    chekCave(caveNumber)

    print('еще будешь траить? (да/нет)')
    playAgain = input()
