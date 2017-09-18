from article import Article
from source import Source
from pyquery import PyQuery as Query

class VoxMedia(Source):
    def __init__(self, cache):
        self.cache = cache
        self.name = None

    def add_headline(self, headline):
        url = headline.attr('href')
        title = headline.text()
        article = Article(url, title, self.name)
        if not url in [a.url for a in self.articles]:
            self.articles.append(article)
        

    def extract_articles(self):
        query = Query(self.data)
        articles = query("a[data-analytics-link='article']").items()
        features = query("a[data-analytics-link='feature']").items()
        self.articles = []
        for headline in articles:
            self.add_headline(headline)
        for headline in features:
            self.add_headline(headline)
            
if __name__=="__main__":
    s = TheVerge("/tmp/theverge.com")
    for a in s.fetch():
        print("* "+a.headline)
