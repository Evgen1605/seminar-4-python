# 27'. Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов или символами конца строки.Определите, сколько различных
# слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells

# string = input('Введите строку: ').split()
# new_set = set()
# for word in string:
#     new_set.add(word.lower().strip('.,?!\n'))
# print(len(new_set))

# Решение преподавателя 
sequence = "She sells, sea shells on the sea shore. The shells\
 that she sells are sea shells! I'm sure So if she sells sea \
shells on the sea shore? I'm sure that\n the shells are sea \
shore shells"
result = [i.strip('.,?!\n').lower() for i in sequence.split()]
result = set(result)
print(result)
print(len(result))
