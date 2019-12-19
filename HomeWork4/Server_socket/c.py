import socket
import pandas
import pickle


order = input("Enter command (stat, enti): ")
# проверяем команду
if order.upper() == 'STAT' or order.upper() == 'ENTI':
    # загружаем файл с помощью pandas и считаем его размер
    data = pandas.read_csv('dataSet.csv', sep=';', encoding='latin1')
    size = str(sum(data.memory_usage(deep=True)))

    # открываем сокет
    with socket.socket() as sock:
        sock.connect(('localhost', 8999))

        # отправляем команду, размер и data
        sock.send(pickle.dumps([order, size]))
        sock.send(pickle.dumps(data))

        # получаем данные и печатаем
        result = pickle.loads(sock.recv(65536))
        print(*result, sep='\n')
else:
    print("ERROR COMMAND")
    exit(2)
