from article import Article
from source import Source
from pyquery import PyQuery as Query

class TheGuardian(Source):
    url = "https://www.theguardian.com/"

    def __init__(self, cache):
        self.cache = cache

    def extract_articles(self):
        query = Query(self.data)
        headlines = query("a.js-headline-text").items()
        self.articles = []
        for headline in headlines:
            url = headline.attr('href')
            title = headline.text()
            article = Article(url, title, "theguardian.com")
            self.articles.append(article)

if __name__=="__main__":
    g = TheGuardian("/tmp/guardian.html")
    for a in g.fetch():
        print("* "+a.url)
        
    
