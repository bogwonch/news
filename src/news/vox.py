from voxmedia import VoxMedia

class Vox(VoxMedia):
    url = "https://www.vox.com"
    name = "vox.com"

if __name__=="__main__":
    s = Vox("/tmp/vox.com")
    for a in s.fetch():
        print("* "+a.headline)
