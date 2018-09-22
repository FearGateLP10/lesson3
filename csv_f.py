
# Создайте список словарей:
#     [
#     {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
#     {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
#     {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
# ]
# Запишите содержимое списка словарей в файл в формате csv


import csv


my_dict = [
	{'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
	{'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
	{'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
]

with open('my_file.csv', 'w', encoding='utf-8') as f:
	fields = ['name', 'age', 'job']
	writer = csv.DictWriter(f, fields)
	writer.writeheader()
	for user in my_dict:
		writer.writerow(user)
