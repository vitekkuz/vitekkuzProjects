import requests
from bs4 import BeautifulSoup as bs

headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}

base_url = 'https://belgorod.hh.ru/search/vacancy?search_period=7&area=17&text=python&page=0'

def hh_parse(base_url, headers):
    session = requests.Session() #создаем сессию, будто зашел один пользователь и просматривает вакансии
    request = session.get(base_url, headers= headers) #Эмулируем открытие страницы в браузере
    if request.status_code == 200: #проверяем, что сервер передал нам данные
        soup = bs(request.content, 'html.parser')
        divs = soup.find_all('div', attrs={'data-qa': 'vacancy-serp__vacancy'})
        for div in divs:
            title = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-title'}).text
            href = div.find('a', attrs={'data-qa': 'vacancy-serp__vacancy-title'})['href']
            content = title + '\n' + href
            print(content)
    else:
        print('ERROR')


hh_parse(base_url, headers)
