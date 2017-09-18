from article import Article
from source import Source
from pyquery import PyQuery as Query

class TheVerge(Source):
    url = "https://www.theverge.com"

    def __init__(self, cache):
        self.cache = cache

    def extract_articles(self):
        query = Query(self.data)
        headlines = query("a[data-analytics-link='article']").items()
        self.articles = []
        for headline in headlines:
            print(str(headline))
            url = headline.attr('href')
            title = headline.text()
            article = Article(url, title, "theverge.com")
            if not url in [a.url for a in self.articles]:
                self.articles.append(article)

            
if __name__=="__main__":
    s = TheVerge("/tmp/theverge.com")
    for a in s.fetch():
        print("* "+a.headline)
