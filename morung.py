import requests
import json
from bs4 import BeautifulSoup
from helper import keywords, ArticleDownload
from newspaper import Article


def getLinks(category):
    extracted_link = []
    for pageNum in range(1, 29):
        url = f'https://morungexpress.com/category/{category}?page={pageNum}'
        data = requests.get(url).content
        soup = BeautifulSoup(data, 'html.parser')
        linksEle = soup.find_all('li', class_='view-list-item m-md-3 p-3')
        for link in linksEle:
            link = link.findChildren("a")
            extracted_link.append(link[0]['href'])
            print(link[0]['href'])
    return extracted_link


if __name__ == '__main__':
    category = "editorial"
    keywords = keywords()
    links = getLinks(category)
    print(len(links))
    contents = ArticleDownload(links, keywords)
    
    # Write result to a file
    with open("morung.json", "w", encoding="utf8") as file: 
        json.dump(contents, file, ensure_ascii=False) 