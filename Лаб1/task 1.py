numbers =[2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
numbers_1 = numbers[:4] #числа до None
numbers_2 = numbers[5:] #числа после None
summary_1 = sum(numbers_1) #сумма первой части
summary_2 = sum(numbers_2) #сумма второй части
total = summary_1+summary_2
count = len(numbers)
average = total / count
numbers[4] = average
print("Измененный список:", numbers)
