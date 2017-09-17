from article import Article
from source import Source
from pyquery import PyQuery as Query

class BBC(Source):
    url = "https://www.bbc.co.uk/news"

    def __init__(self, cache):
        self.cache = cache

    def extract_articles(self):
        query = Query(self.data)
        headlines = query("a.gs-c-promo-heading").items()
        self.articles = []
        for headline in headlines:
            url = headline.attr('href')
            title = headline.text()
            article = Article(url, title, "bbc.co.uk/news")
            if not url in [a.url for a in self.articles]:
                self.articles.append(article)

            
if __name__=="__main__":
    s = BBC("/tmp/guardian.html")
    for a in s.fetch():
        print("* "+a.headline)
