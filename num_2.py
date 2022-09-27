slovar = {
    'one': 1,
    'one_': 1
}

print(slovar)

slovar['one_'] = 100


print(slovar)

slovar['two'] = 2
print(slovar)
print()
print()
print("Значение 1-го ключа: " + str(slovar['one']))
print("Значение 2-го ключа: " + str(slovar['one_']))
print("Значение 3-го ключа: " + str(slovar['two']))