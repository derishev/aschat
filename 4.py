#4. Преобразовать слова «разработка», «администрирование», «protocol», 
#«standard» из строкового представления в байтовое и выполнить обратное 
#преобразование (используя методы encode и decode).

my_list = ['разработка', 'администрирование', 'protocol', 'standard']
for line in my_list:
    a = line.encode('utf-8')
    print(a, type(a))
    b = bytes.decode(a, 'utf-8')
    print(b, type(b))