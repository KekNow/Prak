import socket
import pickle
import pandas
import multiprocessing
import threading
from pycorenlp import StanfordCoreNLP


def HANDLER(conn, addr):
    print("Connect with:", addr)
    with conn:
        # загружаем команду, размер и data
        dataFrame = pickle.loads(conn.recv(4096))
        order, size = dataFrame[0], int(dataFrame[1])
        data = pickle.loads(conn.recv(size))

        if order.upper() == 'STAT':
            amount = len(data['Tweet Id'])
            poptweets = []
            words = {}
            authors = {}
            countries = {}

            # формируем список для популярных твитов и словари для всех слов, авторов, стран
            j = kol = 0
            while kol < 10:
                if not pandas.isna(data['RTs'][j]):
                    poptweets.append([int(data['RTs'][j]), data['Nickname'][j], data['Tweet Url'][j]])
                    kol += 1
                j += 1
            poptweets.sort(key=lambda x: x[0], reverse=True)
            for i in range(amount):
                for word in data['Tweet content'][i].split():
                    if word in words:
                        words[word] += 1
                    else:
                        words[word] = 1
                popular = data['RTs'][i]
                if not pandas.isna(popular):
                    author = data['Nickname'][i]
                    if author in authors:
                        authors[author] += popular
                    else:
                        authors[author] = popular
                country = data['Country'][i]
                if not pandas.isna(country):
                    if country in countries:
                        countries[country] += 1
                    else:
                        countries[country] = 1

            # отбираем необходимые топ10 с помощью сортировок
            for i in range(j, amount):
                if poptweets[9][0] < data['RTs'][i]:
                    poptweets[9] = [int(data['RTs'][i]), data['Nickname'][i], data['Tweet Url'][i]]
                    poptweets.sort(key=lambda x: x[0], reverse=True)
            words = sorted(words.items(), key=lambda x: x[1], reverse=True)
            authors = sorted(authors.items(), key=lambda x: x[1], reverse=True)
            countries = sorted(countries.items(), key=lambda x: x[1], reverse=True)

            # формируем итоговый результат
            result = (["\nTOP10 POPULAR TWEETS [RTs, Nickname, Tweet Url]:"] + poptweets +
                      ["\nTOP10 POPULAR WORDS (Word, Quantity):"] + words[:10] +
                      ["\nTOP10 POPULAR AUTHORS (Nickname, Quantity RTs):"] + authors[:10] +
                      ["\nTOP10 POPULAR COUNTRIES (Country, Quantity):"] + countries[:10])
        elif order.upper() == 'ENTI':
            # подключаемся к серверу Stanford coreNLP, формируем стартовый список
            amount = 50
            nlp = StanfordCoreNLP('http://localhost:9000')
            result = ["\nNAMED ENTITIES FOR %d TWEETS:" % amount]
            for i in range(amount):
                # обработка каждого твита на предмет именованных сущностей и запись его в result
                tmp = []
                core = nlp.annotate(data['Tweet content'][i], properties={'annotators': 'ner', 'outputFormat': 'json', 'timeout': 10000, })
                for word in core['sentences'][0]['tokens']:
                    tmp.append('{} ({})'.format(word['word'], word['pos']))
                result.append(tmp)
        # отправляем результат
        conn.send(pickle.dumps(result))


def WORKER(sock):
    print("Server start")
    while True:
        # ждём запроса на подключение
        conn, addr = sock.accept()

        # запускаем обработчик с помощью треда
        th = threading.Thread(target=HANDLER, args=(conn, addr))
        th.start()


if __name__ == '__main__':
    # открываем сокет
    with socket.socket() as sock:
        sock.bind(('', 8999))
        sock.listen(3)

        # распараллеливаем на 3 процесса
        workers_list = [multiprocessing.Process(target=WORKER, args=(sock,)) for _ in range(3)]
        for w in workers_list:
            w.start()
        for w in workers_list:
            w.join()
