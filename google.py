import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from googlesearch import search

def search_results(query, number, advanced=True):

    titles = []
    urls = []
    prices = []

    for title in search(query, num_results=number, advanced=advanced):
        titles.append(title.title)
        urls.append(title.url)
    """ 
    ادرس المنت سایت ها
    """
    zoomit = '//a[@class="summary-product--price fa-num hidden-xs hidden-sm"]/span/span'
    digikala = '//div[@class="d-flex ai-center jc-start"]//span[@class="text-h4 ml-1 color-800"]'
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
                    prices.append('زومیت :محصول موجود نمی باشد ')
                    continue

            if 'digikala' in value:
                try:
                    driver.get(value)
                    time.sleep(5)
                    price = driver.find_element(By.XPATH, digikala)
                    prices.append('دیجی کالا '+price.text)
                except:
                    prices.append('دیجی کالا :محصول موجود نمی باشد ')
                    continue


            if 'torob' in  value:
                try:
                    driver.get(value)
                    price = driver.find_element(By.XPATH, torob)
                    prices.append('ترب '+price.text)
                    time.sleep(5)
                except:
                    prices.append('ترب : محصول موجود نمی باشد ')
                    continue

            if 'emalls' in value:
                try:
                    driver.get(value)
                    price = driver.find_element(By.XPATH, elmaz)
                    prices.append('ایلماز'+price.text)
                    time.sleep(5)
                except:
                    prices.append('ایلماز :محصول موجود نمی باشد ')
                    continue
    get_data()

search_results('قیمت گوشی a52', 4)
