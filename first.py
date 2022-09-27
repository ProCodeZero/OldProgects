spisok = [1, 2, 34]


def loh():
    slovar = {
        "One": "1"
    }

    print(slovar['One'])

    a = input()
    if a == slovar.keys():
        print("Yes")
    else:
        print("No")

