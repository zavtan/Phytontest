numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
new_numbers = numbers
numbers_ = len(numbers)
del new_numbers[4]
new_numbers_ = sum(new_numbers) / numbers_
numbers.insert(4, new_numbers_)

# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
