#1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате
# и проверить тип и содержание соответствующих переменных. 
#Затем с помощью онлайн-конвертера преобразовать строковые представление 
#в формат Unicode и также проверить тип и содержимое переменных.
 
str1 = str('разработка')
str2 = str('сокет')
str3 = 'декоратор'
 
print(type(str1))
print(str2)
print(type(str3))
 
# применим https://symbl.cc/ru/tools/decoder/
# получим следующие строки
str1 = b'\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
str2 = b'\u0441\u043e\u043a\u0435\u0442'
str3 = b'\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
 
print(type(str1))
print(str2)
print(type(str3))