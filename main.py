word = input("Введите слово из 5 букв ")
# word = 'ккооо'
today_word = 'кошка'
# result
if word == today_word:
    print(word + " - верное")
else:
    print("Слово не угадано! Но в загаданном слове есть буквы:")
    for i in word:
        if i in today_word:
            print(i)
