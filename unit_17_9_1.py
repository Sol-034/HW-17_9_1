# поиск индекса элемента меньше введенного пользователем числа
def search_index(array, search_element):
    left = 0
    right = len(array)-1

    while left <= right:
        middle = (left + right) // 2
        middle_element = array[middle]
        previous_index = middle - 1
        if search_element == middle_element:
            return previous_index
        elif search_element > middle_element:
            left = middle + 1
        else:
            right = middle - 1
    else:
        if search_element > middle_element:
            return middle
        else:
            return previous_index


# Преобразование введённой последовательности в список
array = list(map(float,input('Введите последовательность чисел через пробел:').split(' ')))

# запрос у пользователя любого числа
user_number = float(input('Введите любое число'))

# Решаем проблему с дублирующими значениями в последовательности
array = list(set(array))

# Сортировка списка по возрастанию элементов в нем
array.sort()

# предварительная проверка пользовательского числа на вхождение в последовательность чисел
if user_number == "":
    print(f'Ошибка ввода. Вместо любого числа выполнен пустой ввод')
elif user_number <= array[0]:
    print(f'Ошибка ввода. В последовательности нет числа, меньше введённого {user_number}.')
elif user_number > array[-1]:
    print(f'Ошибка ввода. В последовательности нет числа, больше введённого {user_number}.')
else:
    print(search_index(array,user_number))
