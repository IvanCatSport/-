print("Привет польватель")
print("Хотите войте в почту или браузер?")
print("выберете каманду для входа")
print("1 - Google", "2 - Outlook", "3 - Яндекс")
a = int(input("Ввидите каманду: "))
if 0<a<2 :
	print ("Вы выбрали Гугол ")
	name = input("Ввидите логин: ")
	p = input("Ввидите Пороль: ")
	if name=="1111" and p =="1111":
		print("Привет 1111!")
		print("Вы вошли")
		import webbrowser
		webbrowser.open("https://www.Google.ru/")
	else :
		print("Неизвесный логин или пороль")	
if 1<a<3 :
	print ("Вы выбрали Outlook ")
	name = input("Ввидите логин: ")
	p = input("Ввидите Пороль: ")
	if name=="1111" and p =="1111":
		print("Привет 1111!")
		print("Вы вошли")
		import webbrowser
		webbrowser.open("https://Outlook.live.com/")
	else :
		print("Неизвесный логин или пороль")
if 2<a<4 :
	print ("Вы выбрали Яндекс ")
	name = input("Ввидите логин: ")
	p = input("Ввидите Пороль: ")
	if name=="1111" and p =="1111":
		print("Привет 1111!")
		print("Вы вошли")
		import webbrowser
		webbrowser.open("https://yandex.ru/")	
	else :
		print("Неизвесный логин или пороль")			
		
	import math