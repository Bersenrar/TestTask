import requests


class Spider:
    def __init__(self, url):
        self.__url = url

    def __get_data(self):
        try:
            response = requests.request("GET", self.__url)
            if response.status_code != 200:
                return None
            return response.json()
        except Exception as e:
            print("Something went wrong while fetching data")
            return None

    @staticmethod
    def __parse_data(data):
        '''
        Столиці у вигляді масиву можно було би створювати рядок методом .join але вирішив залишити список
        '''
        print("Назва країни\tНазва столиці\tПосилання на флаг\t")
        for jd in data:
            print(f"{jd.get('name', None).get('official', None)}\t{jd.get('capital', None)}\t{jd.get('flags', None).get('png', None)}")

    def run(self):
        data = self.__get_data()
        self.__parse_data(data)


if __name__ == "__main__":
    sp = Spider("https://restcountries.com/v3.1/all")
    sp.run()
