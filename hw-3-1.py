min_num = int(input('Введите min'))
d = {}
try:
    with open('cities.txt', 'r') as text_file:
        with open('filtered_cities.txt', 'w') as txt_file:
            for line in text_file:
                city, num = line.strip().split(':')
                num2 = int(num)
                if num2 > min_num:
                    d[city] = num2
            for i in sorted(d):
                txt_file.write(i + ':' + str(d[i]) + '\n')
except FileNotFoundError:
    print('This file does not exist, please come back later')