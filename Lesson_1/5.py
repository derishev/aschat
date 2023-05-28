#5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и 
#преобразовать результаты из байтовового в строковый тип на кириллице.

import subprocess


ping_resurs = ['ping', 'yandex.ru']


ping_process = subprocess.Popen(ping_resurs, stdout=subprocess.PIPE)

i = 0

for line in ping_process.stdout:

    if i<5:
        print(line)
        line = line.decode('cp866').encode('utf-8')
        print(line.decode('utf-8'))
        i += 1
    else:
            break