from itertools import product
import random
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
real_number = input("Введите вещественное число: ")
sum1 = 0

for i in range(0, len(real_number)):
    if real_number[i].isdigit():
        sum1 += int(real_number[i])
print(f"Сумма цифр в числе: {sum1}")

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
num = int(input("Введите N: "))
list_product = []
all_product = 1

for i in range(1,num + 1):
    all_product *= i
    list_product.append(all_product)
print(list_product)

# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
def func (x):
    return (1 + 1/x)**x

n = int(input("Введите число N: "))
n_list = []

for i in range(1,n-1):
    result_func = func(i)
    n_list.append(result_func)
print(f"Сумма чисел последовательности: {sum(n_list)}")

# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в 
# одной строке одно число.
n = int(input("Введите кол-во элементов списка: "))
list_ns = list(random.randint(-n,n) for i in range(0,n))
print(list_ns)
pr = 1

with open("file.txt") as ind_f:
    for i in ind_f:
        indx = int(i.replace(" ", ""))
        if indx > len(list_ns)-1:
            continue
        pr *= list_ns[indx]
print(f"Произведение выбранных элементов = {pr}")       

# Реализуйте алгоритм перемешивания списка
def new_shuffle (list):
    for i in range(0,len(list)-1):
        ind = random.randint(i+1,len(list)-1)
        list[ind], num_list[i] = list[i],list[ind]
    return list

num_list = list(range(1,30,2))
print(f"Список до перемешивания:    {num_list}")
print(f"Список после перемешивания: {new_shuffle(num_list)}")
