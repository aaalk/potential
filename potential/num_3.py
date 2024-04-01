# python
import csv

with open('history_mirror.csv', encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    data = sorted(reader, key=lambda x: x['date'])
a = input()
# ввод имени и отчества через пробел, записываем в переменную а

while ('stop' not in a):
    for el in data:
        if a in el['username']:
            # итерируемся по каждой строчке, если такое имя и отчество есть в таблице, то с помощью метода split раделяем ячейку с фио на отдельные фамилию,  имя и отчество, записываем в переменные

            surname, name, fath = el["username"].split()
            print(f'Предсказание для {surname} {name[0]}.{fath[0]}. - {el["verdict"]}')
            # вывод через f string как просят в задании
            break
    else:
        print('Вас не нашлось в записях')
    a = input()
    # ввод данных повторно