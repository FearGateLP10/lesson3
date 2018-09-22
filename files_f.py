
# Скачайте файл по ссылке
# Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
# Подсчитайте количество слов в тексте
# Замените точки в тексте на восклицательные знаки
# Сохраните результат в файл referat2.txt


with open('referat.txt', 'r', encoding='utf-8') as f:
	text = f.read()
	print(len(text))
	print(len(text.split()))
	text_2 = text.replace('.', '!')

	with open('referat2.txt', 'w', encoding='utf-8') as file:
		file.write(text_2)
