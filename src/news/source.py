import os.path
import time
import urllib.request

class Source(object): 
    url = None
    cache = None
    data = None
    articles = None
    expires = 6*60*60

    def needs_update(self):
        """Determine if we need to update the cache.""" 
        try:
            return (time.time() - os.path.getmtime(cache)) > self.expires
        except Exception:
            return True
        
    def fetch(self, refresh=False): 
        if refresh or self.needs_update():
            self.fetch_from_url()
        else:
            self.fetch_from_cache()

        if not (self.data == None):
            self.extract_articles()

        return self.articles

    def fetch_from_url(self):
        with urllib.request.urlopen(self.url) as response:
            self.data = response.read().decode()
            with open(self.cache, 'w+') as f:
                f.write(self.data)

    def fetch_from_cache(self):
        with open(self.cache) as f:
            self.data = f.read()

    def extract_articles(self):
        pass
