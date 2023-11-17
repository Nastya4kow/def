#  Задача
# Напишите функцию, которая:
# - принимает на вход строку
# - возвращает количество гласных букв в строке.
# В строке используются только латинские символы
# Регистр букв может быть любой.

def count_vowels(str):
    dictionary={}
    vowels=['e','o','a','u','i','y']
    count=0          #количество гласных
    for item in str:
        if item.lower() in vowels:
            count+=1
            dictionary.update({item.lower():count})
    #result=','.join(dictionary)
    return dictionary
data=input("введите строку")
print(count_vowels(data))