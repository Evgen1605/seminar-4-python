# 25'. Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n. Порядок символов исходной строки не меняется.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

string = input('Введите строку: ').split()

# создаём словарь, куда будем хранить символы как ключи, а кол-во вхождений как значения
d = dict()

for i in string:
    if i in d:
        # если есть символ в словаре, печатаем его и кол-во вхождений
        print(f'{i}_{d[i]}', end=' ')
    else:
        print({i}, end=' ')  # если нету, то один символ
    # Создаём ключ и присваиваем значение 1, если такой ключ есть то увеличиваем значение на 1
    d[i] = d.get(i, 0) + 1



# решения преподавателя 
sequence = 'a a a b c a a d c d d'.split()
letters = {}
result = ''
for i in range(len(sequence)):
    if sequence[i] not in letters.keys():
        letters[sequence[i]] = 1
        result += f'{sequence[i]} '
    else:
        result += f'{sequence[i]}_{letters[sequence[i]]} '
        letters[sequence[i]] += 1
print(result)

# решение через срезы

# result = ''
# for i in range(len(sequence)):
#     if sequence[0:i:].count(sequence[i]) == 0:
#         result += sequence[i]
#     else:
#         result += f'{sequence[i]}_{sequence[0:i].count(sequence[i])}'
#     print(sequence[0:i], result)
# print(result)

# решение через list comprehension и срезы

print(sequence)
result = [(sequence[i] if
            sequence[0:i:].count(sequence[i]) == 0 else
            f'{sequence[i]}_{sequence[0:i:].count(sequence[i])}')
           for i in range(len(sequence))]
print(' '.join(result))
