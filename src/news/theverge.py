from voxmedia import VoxMedia

class TheVerge(VoxMedia):
    url = "https://www.theverge.com"
    name = "theverge.com"

    def __init__(self, cache):
        self.cache = cache

if __name__=="__main__":
    s = TheVerge("/tmp/theverge.com")
    for a in s.fetch():
        print("* "+a.headline)
