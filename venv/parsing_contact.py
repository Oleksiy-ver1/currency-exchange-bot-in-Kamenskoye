import requests
from bs4 import BeautifulSoup # из bs4 вытаскиваем BeautifulSoup

URL="https://obmen24.com.ua/" # адрес который будем парсить
HEADERS={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36', "accept":"*/*"}
#заголовки нужны чтоб сайт воспринемал нас как браузер, а не как бот
HOST ="https://obmen24.com.ua/"

class Contact:
    pass

def get_html(url, params=None):
    r=requests.get(url, headers=HEADERS, params=params)
    return r

def get_phone(html):
    soup=BeautifulSoup(html, 'html.parser') # 'html.parser' - параметр указывающий, что разбераем html-формат
    phone =[]
    items_phone=soup.findAll("div", {"class": "headerdivphone"}) #добываем номера телефонов
    for item in items_phone:
        phone.append(item.find('a').get('href'))

    return phone

def get_addres(html):
    soup = BeautifulSoup(html, 'html.parser')  # 'html.parser' - параметр указывающий, что разбераем html-формат
    addres = soup.find("a", {"href": "#address"}).getText('span').replace('span', '').replace('\n','').strip()  # добываем адрес
    return addres

def get_contact():
    html=get_html(URL)
    if html.status_code== 200:
        contact =Contact()
        contact.phone=get_phone(html.text)
        contact.addres =get_addres(html.text)

    else:
        print ('ERROR')

    return contact


# get_contact()
