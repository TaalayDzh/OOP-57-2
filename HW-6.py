def sum_of_numbers(list_of_numbers, target):

    choices = {}
    for i, num in enumerate(list_of_numbers):
        second_number_for_target = target - num
        if second_number_for_target in choices:
            return [choices[second_number_for_target], i]
        choices[num] = i
    return "Нет подходящих чисел!!!"

list_of_numbers = [1, 3, 7, 12, 6, 44, 5, 9, 21]
target = 50

result = sum_of_numbers(list_of_numbers, target)
print(result)
