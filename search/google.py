import time
import urllib.request

from selenium import webdriver
from selenium.webdriver.common.by import By
from googlesearch import search
from .models import SearchBox
from .serializers import ValueSearchSerializer

class BotSearch:
    def connect(host='http://google.com'):
        try:
            urllib.request.urlopen(host)  # Python 3.x
            return True
        except:
            return False

    def search_results(query, number, advanced=True):
        data_search = SearchBox.objects.all().values()
        last_data = data_search[::-1][0]
        data_title = last_data['Text_box']
        titles = []
        urls = []
        prices = []
        result = {'title': data_title}

        for title in search(query, num_results=number, advanced=advanced):
            titles.append(title.title)
            urls.append(title.url)
        """ 
        ادرس المنت سایت ها
        """
        zoomit = '//a[@class="summary-product--price fa-num hidden-xs hidden-sm"]/span/span'
        digikala = '//span[@class="text-h4 ml-1 color-800"]'
        torob = '//div[@class="jsx-478367150 price"]//div[@class="jsx-478367150"]'
        elmaz = '//h2[@itemscope="itemscope"]//strong[@style="color: #1AA603;"]'

        url_data = []
        title_data = []
        for num in range(len(urls)):
            if 'zoomit' in urls[num]:
                url_data.append(urls[num])
                title_data.append(titles[num])

            if 'digikala' in urls[num]:
                url_data.append(urls[num])
                title_data.append(titles[num])

            if 'torob' in urls[num]:
                url_data.append(urls[num])
                title_data.append(titles[num])

            if 'emalls' in urls[num]:
                url_data.append(urls[num])
                title_data.append(titles[num])


        def get_data():
            driver = webdriver.Chrome(r"D:/myself/web_burger/similar-products/venv/chromedriver.exe")
            time.sleep(1)
            for value in url_data:
                time.sleep(3)
                if 'zoomit' in value:
                    try:
                        driver.get(value)
                        price = driver.find_element(By.XPATH, zoomit)
                        prices.append('زومیت '+price.text)
                        time.sleep(5)
                    except:
                        prices.append('زومیت:اعطلاعات موجودنیست! خطایی رخ داده.')
                        continue

                if 'digikala' in value:
                    try:
                        driver.get(value)
                        time.sleep(15)
                        price = driver.find_element(By.XPATH, digikala)
                        prices.append('دیجی کالا '+price.text)
                        time.sleep(2)
                    except:
                        prices.append('دیجی کالا :اعطلاعات موجودنیست! خطایی رخ داده.')
                        continue


                if 'torob' in  value:
                    try:
                        driver.get(value)
                        price = driver.find_element(By.XPATH, torob)
                        prices.append('ترب '+price.text)
                        time.sleep(5)
                    except:
                        prices.append('ترب :اعطلاعات موجودنیست! خطایی رخ داده.')
                        continue

                if 'emalls' in value:
                    try:
                        driver.get(value)
                        price = driver.find_element(By.XPATH, elmaz)
                        prices.append('ایلماز'+price.text)
                        time.sleep(5)
                    except:
                        prices.append('ایلماز :اعطلاعات موجودنیست! خطایی رخ داده.')
                        continue

            for num in range(len(url_data)):
                result['titles'] = title_data[num]
                result['urls'] = url_data[num]
                result['price'] = prices[num]
                # desrializers data
                serializer = ValueSearchSerializer(data=result)
                serializer.is_valid(raise_exception=True)
                serializer.validated_data
                serializer.save()
            return serializer
        get_data()

