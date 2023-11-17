#  Задача
# Вывести на экран:
# - сумму всех элементов списка
# - среднее арифметическое всех элементов списка
# - максимальное значение списка
# - минимальное значение списка
def info(arr):
    summ=sum(arr)
    dr=sum(arr) / len(arr)
    print(f'Сумма: {summ} ')
    print(f'Среднее арифметическое: {dr} ')
    print(f'Минимальное значение: {min(arr)}')
    print(f'Максимальное значение: {max(arr)}')
    return summ,dr
'''
first_arr=[]
for i in range(10):
    num=int(input(f"Введите {i} элемент:"))
    first_arr.append(num)
info(first_arr)
'''

second_arr=[12,5,456,-15,64,54,-24]
info(second_arr)
res=info(second_arr)[0]
res1=info(second_arr)[1]
print(res)
print(res1)