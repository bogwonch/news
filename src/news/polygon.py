from voxmedia import VoxMedia

class Polygon(VoxMedia):
    url = "https://www.polygon.com"
    name = "polygon.com"

if __name__=="__main__":
    s = Polygon("/tmp/polygon.com")
    for a in s.fetch():
        print("* "+a.headline)
