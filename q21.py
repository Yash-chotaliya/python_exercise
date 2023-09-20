list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

for number in list1:
    if number > 150:
        break
    if number % 5 == 0:
        print(number)