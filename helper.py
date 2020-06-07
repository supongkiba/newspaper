from newspaper import Article

def keywords():
    words = ['nnc',
             'Naga National Council',
             'Naga National movement',
             'simon commission',
             'naga political history',
             'naga independence',
             'Armed forces act',
             '1958',
             'AFSPA',
             'disturbed areas',
             '1963',
             'article 370',
             'naga nationlaist',
             'Rani Gaidinliu',
             'az phizo',
             'Naga Club',
             'Formation of Nagaland',
             'nationalism']
    return words

def ArticleDownload(links, keywords):
    newsContent = {'data': []}
    for url in links:
        print(f'-Downloading "{url}"')
        article = Article(url)
        article.download()
        article.parse()
        if [word for word in keywords if(word.lower() in article.text.lower())]:
            newsContent['data'].append({'title': article.title, 'url': url, 'text_content': article.text})
    return newsContent