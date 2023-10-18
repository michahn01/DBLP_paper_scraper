import requests
from bs4 import BeautifulSoup

# URL = 'https://dblp.org/db/conf/uss/uss2023.html'
# response = requests.get(URL)

# soup = BeautifulSoup(response.content, 'html.parser')

# main_div = soup.find('div', id='main')
# uls = main_div.find_all('ul', class_='publ-list')

# works = []
# for ul in uls:
#     lis = ul.find_all('li', class_='entry inproceedings')
#     for li in lis:
#         row = []
#         data_div = li.find('cite', class_='data tts-content')
#         if data_div:
#             title_div = data_div.find('span', class_='title')
#             if title_div:
#                 row.append(title_div.text)
#         # publ = li.find('nav', class_='publ')
#         # if publ:
#         #     ul = publ.find('ul')
#         #     drop_down = ul.find('li')
#         #     inner = drop_down.find('div', class_='head')
#         #     link = inner.find('a')
#         #     linked_page_response = requests.get(BASE_URL + link['href'])
#         #     linked_page_soup = BeautifulSoup(linked_page_response.content, 'html.parser')

#         #     link_main = linked_page_soup.find('main')
            



# print(len(works))

def subLinkFetch(url):
    res = requests.get(url)
    sub_soup = BeautifulSoup(res.content, 'html.parser')
    sub_body = sub_soup.find('body')
    if not sub_body:
        # print('body not found')
        return
    outermost_div = sub_body.find('div')
    if not outermost_div:
        # print('outermost div not found')
        return
    main_div = outermost_div.find('main')
    if not main_div:
        # print("main not found")
        return
    content = main_div.find('section', id='content')
    if not content:
        # print('content not found')
        return 
    block_content = main_div.find('div', class_='block-content')
    if not block_content:
        # print('block content not found')
        return 
    outer_div = block_content.find('div', class_='field field-name-field-paper-description field-type-text-long field-label-above')
    if not outer_div:
        # print('outer div not found')
        return
    field_items = outer_div.find('div', class_='field-items')
    if not field_items:
        # print('field items not found')
        return
    p_elements = field_items.find_all('p')
    abstract = ' '.join([p.text for p in p_elements])
    print(abstract)
    

subLinkFetch('https://www.usenix.org/conference/usenixsecurity23/presentation/wu-xinghui')