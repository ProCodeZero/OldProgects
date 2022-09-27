spisok = {
    "Азаров": "Даниил",
    "Аршинцев": "Игорь",
    "Богданов": "Александр"
}

Surname = input(str('Введите фамилию '))

if Surname in spisok:
    print(spisok[Surname])
else:
    print(str(Surname + " отсутствует"))