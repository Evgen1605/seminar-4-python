# Задача №29. Решение в группах Ваня и Петя поспорили, кто быстрее решит следующую задачу: “Задана последовательность неотрицательных целых чисел. Требуется определить значение наибольшего элемента последовательности, которая завершается первым встретившимся нулем(число 0 не входит в последовательность)”. Однако 2 друга оказались не такими смышлеными. Никто из ребят не смог до конца сделать это задание. Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор. За помощью товарищи обратились к Вам, студентам.

# # Ваня:
# n = int(input())
# max_number = 1000       ошибка
# while n != 0:
#     n = int(input())
#     if max_number > n:  ошибка
#         max_number = n
# print(max_number)

# Петя:
# n = int(input())
# max_number = -1
# while n < 0:           ошибка
#     n = int(input())
#     if max_number < n: ошибка
#         n = max_number
# print(n)               ошибка


n = int(input())
max_number = 0
while n != 0:
    if n > max_number:
        max_number = n
n = int(input())
print(max_number)

nn = input().split()
new_max = 0
for i in nn:
    if int(i) == 0:
        break
if new_max < int(i):
    new_max = int(i)
print(new_max)
