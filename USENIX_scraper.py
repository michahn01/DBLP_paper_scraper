import requests
from bs4 import BeautifulSoup

def scrape(URL, num):
    response = requests.get(URL)

    soup = BeautifulSoup(response.content, 'html.parser')

    main_div = soup.find('div', id='main')
    uls = main_div.find_all('ul', class_='publ-list')

    i = 0
    works = []
    for ul in uls:
        if i > num:
            break
        lis = ul.find_all('li', class_='entry inproceedings')
        for li in lis:
            if i > num:
                break
            try:
                data_div = li.find('cite', class_='data tts-content')
                # find the title
                title_div = data_div.find('span', class_='title')
                # find the link to abstract
                link = li.find('nav', class_='publ').find('ul').find('li').find('div', class_='head').find('a')

                works.append([title_div.text, getAbstract(link['href'])])
                i += 1
            except:
                print("error at:", link)
            

    return works




def getAbstract(url):
    res = requests.get(url)
    sub_soup = BeautifulSoup(res.content, 'html.parser')

    p_elements = sub_soup.find('body').find('div').find('main').find('section', id='content').find('div', class_='block-content').find('div', class_='field field-name-field-paper-description field-type-text-long field-label-above').find('div', class_='field-items').find_all('p')

    return ' '.join([p.text for p in p_elements])
    # print(abstract)
    

if __name__ == "__main__":
    # pass your url here in the argument to scrape()
    works = scrape('https://dblp.org/db/conf/uss/uss2023.html', 423)
    for work in works:
        print("Title:", work[0])
        print("Abstract:", work[1])
        print()

    # for work in works:
    #     print("Title:", work[0], "Abstract:", work[1])