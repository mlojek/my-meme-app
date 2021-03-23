import os


class Meme:
    def __init__(self, path: str):
        self.name = os.path.basename(path)
        self.path = path

    def add_text(self, text: str):
        self.text = text
        self.words = text.split()


memuch = Meme(r'dir\file.png')
memuch.add_text('przeczytany tekst z obrazka')
print(os.path.basename(memuch.path))
