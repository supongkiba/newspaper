import requests
import json
from bs4 import BeautifulSoup
from helper import keywords, ArticleDownload


def QueryNagalandPage(category):
    extracted_link = []
    for page in range(1, 63):
        url = f'https://nagalandpage.com/category/editorial/{category}/page/{page}/'
        data = requests.get(url).content
        soup = BeautifulSoup(data, 'html.parser')
        
        # List of <div> tags with class="post-title-wrapper"
        linksEle = soup.find_all('div', class_='post-title-wrapper')
        for link in linksEle:
            # Extract the child <a> element
            link = link.findChildren("a")
            # Extract the href attribute value
            print(link[0]['href'])
            extracted_link.append(link[0]['href'])
    return extracted_link
        
    
    
if __name__=="__main__":
    # List of Keyword to look up
    keywords = keywords()
    category = "your-page"
    links = QueryNagalandPage(category)
    print(f'Found {str(len(links))} links')
    contents = ArticleDownload(links, keywords)
    
    # Write result to a file
    with open("nagaland_page_your_page.json", "w", encoding="utf8") as file: 
        json.dump(contents, file, ensure_ascii=False) 
