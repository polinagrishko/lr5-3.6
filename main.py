text = open('text.txt', 'r', encoding="utf-8") #Открытие файла text.txt для чтения с помощью режима 'r', кодировки utf-8 и присваивание его переменной text
str1 = text.read().split(" ") #Создание списка, содержащего слова текста из файла
words = open('output.txt', 'w', encoding="utf-8") #Открытие файла output.txt для записи с помощью режима 'w', кодировки utf-8 и присваивание его переменной words
str2 = set() #Создание пустого множества уникальных слов
for word in str1: #Цикл for для перебора элементов(word) в списке str1
    str2.add(word) #Добавление элемента(word) в список str2
for word in str2:#Цикл для перебора
    words.write(word +'\n')#запись каждого слова с новой строки
words.close()# закрытие файла
text.close()# закрытие файла