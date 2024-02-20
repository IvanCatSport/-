import random
toCode = "0йцукенгшщзхъэжддлорпавыфячсмитьбю1234567890AQWETYIO1234567890PASqwertyuioplkjhgfdsazxcvbnmGHJKLMNBCXZЙЦ1234567890УКЕНГШЩЗХЪЭЖДЛОРПВЫФЯЧСМИТЬЮ"
st =input("Ввидите текст для зашифровки: ")
strh = ""
key = ""
t=0 
for i in range(len(st)): # проганяем каждый символ написаного текста
	count = random.randint(0, 100) # Создаем значения для определения количества дабавления символов в strh
	for j in range(count): # сверху все описано
		strh += toCode[random.randint(0, len(toCode)-1)] # дабавляем разные симоволы в strh для запутывания кода)
	if( True ) :
		strh += "U"
	if(random.randint(0,10 == 1)):
		strh += "V"
	if(random.randint(0,10 == 1)):
		strh +=	"D"
	if(random.randint(0,10 == 1)):
		strh += "F"		
	strh += st[i] # В пустую строку дабавлется значение пользователя

print(f"Зашифрованая строчка: {strh}")

s = input("Ввидите шифр: ")
print("")
x = 0
y = 0
f = ""
while x < len(s):
		if s[x] == "U" or s[x] == "V" or s[x] == "D" or s[x] == "F":
			f += s[x + 1]
			x += 2
		else:
			x += 1		
print(f"Расшифрованный текст: {f} ", end="")

sfff = input("Ввидите шифр: ")

	
