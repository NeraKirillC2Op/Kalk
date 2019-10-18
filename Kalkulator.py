a = input("Выберите:1-Сложение,2-умножение,3-деление,4-вычитание,5-ЕП,6-ОП:")
if a == "1" :
	b = int(input("Введите Первое Число:"))
	d = int(input("Введите Второе Число:"))
	s = b + d
	print(str(b)+"+"+str(d)+"="+str(s))
	print("Ответ:"+str(s))
elif a == "2":
	b = int(input("Введите Первое Число:"))
	d = int(input("Введите Второе Число:"))
	s = b * d
	print(str(b)+"*"+str(d)+"="+str(s))
	print("Ответ:"+str(s))
elif a == "3":
	b = int(input("Введите Первое Число:"))
	d = int(input("Введите Второе Число:"))
	s = b / d
	print(str(b)+"/"+str(d)+"="+str(s))
	print("Ответ:"+str(s))
elif a == "4":
	b = int(input("Введите Первое Число:"))
	d = int(input("Введите Второе Число:"))
	s = b - d
	print(str(b)+"-"+str(d)+"="+str(s))
	print("Ответ:"+str(s))
elif a == "5":
	b = int(input("Введите Число Рождаемости:"))
	d = int(input("Введите Число Смертности:"))
	s = b - d
	print(str(b)+"-"+str(d)+"="+str(s))
	print("Ответ:"+str(s))
elif a == "6":
	b = int(input("Введите Естественный прирост:"))
	d = int(input("Введите Миграционный прирост:"))
	s = b + d
	print(str(b)+"+"+str(d)+"="+str(s))
	print("Ответ:"+str(s))