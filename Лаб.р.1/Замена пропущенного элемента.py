numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
list = numbers[:4] + numbers[5:]
int1 = sum(list)
int2 = len(numbers)
numbers[4] = round(int1 / int2, 2)
print("Измененный список:", numbers)
