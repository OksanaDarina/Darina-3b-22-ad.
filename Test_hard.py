#Написать программу, которая находит все уникальные комбинации
#элементов заданного списка, таких, что их сумма равна заданному числу.
# Основная функция поиск комбинаций.
def find_combinations(original, num):
    results = []  # список, в который будут добавляться верные комбинации
    find_rec(original, num, [], results)  # Первый вызов рекурсивной функции
    return results


def find_rec(original, num, current, results):
    if sum(current) > num:  # Стоп рекурсии, когда сумма текущего набора чисел больше, чем нужно
        return 1
    if sum(current) == num:  # Стоп рекурсии, когда сумма текущего набора чисел равна искомой сумме
        results.append(list(current))
        return 1

    # Перебрать элементы списка
    # Рекурсивно вызвать функцию с обновленными аргументами
    # Удалить последний добавленный элемент из текущей комбинации.
    for i in range(len(original)):
        current.append(original[i])
        find_rec(original[i+1:], num, current, results)
        current.pop()


nums = input("Введите числа через пробел: ").split(" ")
for i in range(len(nums)):
    nums[i] = int(nums[i])
flag = int(input("Введите число: "))
result = find_combinations(nums, flag)
print(result)