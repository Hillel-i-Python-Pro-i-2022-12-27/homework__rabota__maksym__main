player1 = input('Введите имя игрока 1: ')
player2 = input('Введите имя игрока 2: ')

list_words = []

while True:
    word = input('Введите слово: ').lower()
    if word == 'Останови игру':
        break
    if not list_words:
        list_words.append(word)
    else:
        if list_words[-1].endswith(word[0]):
            if word not in list_words:
                list_words.append(word)
            else:
                print('Слово уже было!')
        else:
            print('Введено некоректное слово')

print(list_words)
