import requests
from bs4 import BeautifulSoup
import html.parser


class Scraper:
    '''
    Взагалі не думаю що для тестового треба писати документацію але най буде
    Клас має 3 методи 2 з яких інкапсульовані та викликаються в межах методу parse
    '''

    @staticmethod
    def __parse_data(data):
        soup = BeautifulSoup(data, parser="lxml")
        result = {}
        result["price"] = soup.find(class_="x-bin-price__content").find(class_="x-price-primary").find("span").text
        result["img"] = [img.get('src') for img in soup.find_all("img") if img.get("src")]
        result["title"] = soup.find(class_="x-item-title__mainTitle").find("span").text
        result["shipping"] = " ".join(
            [sh.text for sh in soup.find(class_="ux-labels-values__values-content").find_all("span")[:3]]
        )
        result["seller"] = soup.find(class_="x-sellercard-atf__info__about-seller").find("a").get("href")
        return result

    @staticmethod
    def __get_data(url):
        try:
            response = requests.request("GET", url)
            if response.status_code != 200:
                return None
            return response.text
        except Exception as e:
            print("Something went wrong while fetching data")
            return None

    def parse(self, url):
        data = self.__get_data(url)
        rs = self.__parse_data(data)
        rs["url"] = url
        return rs



url = ["https://www.ebay.com/itm/166866683661?_trkparms=amclksrc%3DITM%26aid%3D777008%26algo%3DPERSONAL.TOPIC%26ao%3D1%26asc%3D20230906152218%26meid%3D57bb9d0bd31340e8b0fae582801f13fc%26pid%3D101817%26rk%3D1%26rkt%3D1%26itm%3D166866683661%26pmt%3D0%26noa%3D1%26pg%3D4375194%26algv%3DPersonalizedTopicsV2WithDynamicSizeRanker%26brand%3DNike&_trksid=p4375194.c101817.m47269&_trkparms=parentrq%3Ad07f8ac41900a45aecf61d7cfffeeea4%7Cpageci%3A89a85070-46a2-11ef-8a3b-66898d62f871%7Ciid%3A1%7Cvlpname%3Avlp_homepage", "https://www.ebay.com/itm/335483645823?_trkparms=amclksrc%3DITM%26aid%3D777008%26algo%3DPERSONAL.TOPIC%26ao%3D1%26asc%3D20230906152218%26meid%3D57bb9d0bd31340e8b0fae582801f13fc%26pid%3D101817%26rk%3D1%26rkt%3D1%26itm%3D335483645823%26pmt%3D0%26noa%3D1%26pg%3D4375194%26algv%3DPersonalizedTopicsV2WithDynamicSizeRanker%26brand%3Dadidas&_trksid=p4375194.c101817.m47269&_trkparms=parentrq%3Ad07f8ac41900a45aecf61d7cfffeeea4%7Cpageci%3A89a85070-46a2-11ef-8a3b-66898d62f871%7Ciid%3A1%7Cvlpname%3Avlp_homepage", "https://www.ebay.com/itm/186490283155?_trkparms=amclksrc%3DITM%26aid%3D777008%26algo%3DPERSONAL.TOPIC%26ao%3D1%26asc%3D20230906152218%26meid%3D57bb9d0bd31340e8b0fae582801f13fc%26pid%3D101817%26rk%3D1%26rkt%3D1%26itm%3D186490283155%26pmt%3D0%26noa%3D1%26pg%3D4375194%26algv%3DPersonalizedTopicsV2WithDynamicSizeRanker%26brand%3DNike&_trksid=p4375194.c101817.m47269&_trkparms=parentrq%3Ad07f8ac41900a45aecf61d7cfffeeea4%7Cpageci%3A89a85070-46a2-11ef-8a3b-66898d62f871%7Ciid%3A1%7Cvlpname%3Avlp_homepage"]
s = Scraper()
for u in url:
    print(s.parse(u))
