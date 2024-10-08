def single_root_words(root_word, *other_words): # создаем функицию для поиска однокоренных
    same_words = [] # создаем пустой список для дальнейшей работы
    for i in range(len(other_words)): # цикл длиной кортежа *other_words
        if root_word.lower() in other_words[i].lower() or other_words[i].lower() in root_word.lower(): # проверка на
            # включение задоного слова в i слове из кортежа или наоборот, проверка на однокоренные, при этом все буквы
            #будут в обоих словах в нижнем регистре для проверки
            same_words.append(other_words[i]) # добавляю слово в список
    return same_words # возвращаю список однокоренных

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)