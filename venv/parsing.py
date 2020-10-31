import requests
from bs4 import BeautifulSoup # из bs4 вытаскиваем BeautifulSoup

URL="https://obmen24.com.ua/" # адрес который будем парсить
HEADERS={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36', "accept":"*/*"}
#заголовки нужны чтоб сайт воспринемал нас как браузер, а не как бот
HOST ="https://obmen24.com.ua/"



def get_html(url, params=None):
    r=requests.get(url, headers=HEADERS, params=params)
    return r

def creating_dictionary1 (items):
    k=[]
    half_dic=[]
    for item in items:
        k.append(item.text.strip())
    for elem in range(2, len(k),2):
        half_dic.append(str(k[elem])+'/'+str(k[elem+1]))
    return half_dic

def creating_dictionary2(items_currency):
    half_dic = []
    for item in items_currency:
       half_dic.append(item.text.strip().replace(' ','').replace('\n','/'))
    half_dic=half_dic[1:]
    return half_dic

def combine_dic(items, items_currency):
    kurs={}
    half_dic1 = []
    half_dic2 = []
    half_dic1 = creating_dictionary1(items)
    half_dic2 = creating_dictionary2(items_currency)
    kurs=dict(zip(half_dic2,half_dic1))
    return kurs

def get_content(html):
    soup=BeautifulSoup(html, 'html.parser') # 'html.parser' - параметр указывающий, что разбераем html-формат
    items_currency=soup.findAll("span", {"class": "indexspancurrency"})
    items=soup.findAll("span", {"class": "indexspanbuy"})
    kurs={} #создаем словарь c курсами
    kurs=combine_dic(items,items_currency)
    return kurs

def parse():
    html=get_html(URL)
    if html.status_code== 200:
        kurs=[] # пустой список
        kurs=get_content(html.text) #дополняем список данными

    else:
        print ('ERROR')

    return kurs


# parse()