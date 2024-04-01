# python

import csv

maxi = 0
with open('history_mirror.csv', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',', quotechar='"')
    answer = list(reader)[1:]
    result = []
    for row in answer:
        if row[2] == 'Победа над смертью':
            result.append([row[0], row[1]])
            print(f'Сообщение было зафиксировано: {row[0]} у пользователя {row[1]}<Фамилия И.О.>')

with open('mirror_error.csv', 'w', newline='', encoding='utf-8') as file:
    w = csv.writer(file)
    w.writerow(['date', 'username'])
    w.writerows(result)