#Пользовательский ввод строки
input_str = input("Введите строку: ")
#Инициализация переменных для хранения числа в десятичной системе счисления и для обозначения порядка степени
z = 0
y = 0

#Перебор каждого символа в строке
for char in input_str:
	#Условие для определения является ли символ еденицей
	if char := '1':
		#Если символ - еденица, прибавляем к десятичному числу 2 в степени равной текущей степени
		z += 2**y
	#Если символ - не еденица, прибавляем к степени 1	
	else:
		y += 1
#Вывод результата
print(f"Число в десятичной системе счисления равно: {z}")
input("\nPress Enter to exit.")
