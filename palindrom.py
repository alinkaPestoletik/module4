def palindrom(word):
    print(True if word == word[::-1] else False)

palindrom('лепсспел')
palindrom('helloworld')

# Срез последовательности с “[::-1]” позволяет создать перевернутую копию строки.
# При использовании конструкции if-else мы сравниваем исходное слово и его обратную версию и выводим результат, показывающий является ли слово палиндромом или нет.