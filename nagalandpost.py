import requests
import json
from bs4 import BeautifulSoup
from helper import keywords, ArticleDownload

def QueryNagalandPost(keywords):
    extracted_link = []
    for keyword in keywords:
        print(f'Querying Nagaland Post for "{keyword}"\n')
        keyword = keyword.replace(" ", "%20").lower()
        url = f'http://www.nagalandpost.com/archive_search.aspx?txt={keyword}&catid=14&fd=06/05/2000%2012:00:00%20AM&td=06/05/2020%2012:00:00%20AM'
        data = requests.get(url).content
        soup = BeautifulSoup(data, 'html.parser')
        
        # List of <span> tags with class="nstryspanr"
        linksEle = soup.find_all('span', class_='nstryspanr')
        if len(linksEle) == 0:
            print(f'No results found for "{keyword}"\n')
        else:
            print(f' -Found {str(len(linksEle))} results\n')
            for link in linksEle:
                # Extract the child <a> element
                link = link.findChildren("a" , recursive=False)
                # Extract the href attribute value
                extracted_link.append(f'http://www.nagalandpost.com{link[0]["href"]}')

    # Removing duplicates
    extracted_link = set(extracted_link)
    
    print(f'Found {str(len(extracted_link))} unique Articles!\n\n')
    
    return extracted_link


if __name__=="__main__":
    # List of Keyword to look up
    keywords = keywords()
    links = QueryNagalandPost(keywords)
    contents = ArticleDownload(links, keywords)
    
    # Write result to a file
    with open("nagaland_post.json", "w", encoding="utf8") as file: 
        json.dump(contents, file, ensure_ascii=False) 
