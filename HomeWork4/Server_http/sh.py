from http.server import HTTPServer, BaseHTTPRequestHandler
import pickle
import pandas
from pycorenlp import StanfordCoreNLP


class RequestHeandler(BaseHTTPRequestHandler):
    # функция инициализации заголовков
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    # обработка пришедшего запроса
    def do_POST(self):
        # загружаем размер и data, устанавливаем заголовки согласно протоколу
        size = int(self.headers['Content-Length'])
        data = pickle.loads(self.rfile.read(size))
        self._set_headers()

        order = self.path.lower()
        if order == '/stat':
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
        elif order == '/enti':
            # подключаемся к серверу Stanford coreNLP, формируем стартовый список
            amount = 50
            nlp = StanfordCoreNLP('http://localhost:9000')
            result = ["\nNAMED ENTITIES FOR %d TWEETS:" % amount]
            for i in range(amount):
                # обработка каждого твита на предмет именованных сущностей и запись его в result
                tmp = []
                core = nlp.annotate(data['Tweet content'][i],
                                    properties={'annotators': 'ner', 'outputFormat': 'json', 'timeout': 10000, })
                for word in core['sentences'][0]['tokens']:
                    tmp.append('{} ({})'.format(word['word'], word['pos']))
                result.append(tmp)
        # отправляем результат
        self.wfile.write(pickle.dumps(result))


def run(server_class=HTTPServer, handler_class=RequestHeandler, addr='localhost', port=8999):
    # устанавливаем соединение
    server_adress = (addr, port)
    http = server_class(server_adress, handler_class)
    print("Starting http server on %s:%s" % (addr, port))

    # запускаем "вечный" сервер
    http.serve_forever()


if __name__ == '__main__':
    run()
