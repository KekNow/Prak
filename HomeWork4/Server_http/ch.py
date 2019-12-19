import pandas
import pickle
import requests

order = input("Enter command (stat, enti): ")
# проверяем команду
if order.upper() == 'STAT' or order.upper() == 'ENTI':
    # загружаем файл с помощью pandas
    data = pandas.read_csv('dataSet.csv', sep=';', encoding='latin1')

    # отправляем order и data
    r = requests.post('http://localhost:8999/' + order, data=pickle.dumps(data))

    # получаем данные и печатаем
    result = pickle.loads(r.content)
    print(*result, sep='\n')
else:
    print("ERROR COMMAND")
    exit(2)
