import pytesseract as tess
from PIL import Image
import os
from meme import Meme
import re
import random
import shutil

tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

print("Przetwarzanie danych...")

# meme_list = [Meme(os.path.join('memes', filename)) for filename in os.listdir('memes')]
# for meme in meme_list:
#     img = Image.open(meme.path)
#     text_read = tess.image_to_string(img, lang='eng+pol')
#     text_read = text_read.lower()
#     text_read = re.sub(r'[^\w\s]', '', text_read)
#     meme.add_text(text_read)
#     # print(meme.path, end='\t')
#     # print(meme.words)

# query = input(">>")
# for meme in meme_list:
#     if query in meme.words:
#         print(meme.path)
#         print(meme.words)


# Random image from zwała:

files = os.listdir('memes')
chosen = os.path.join('memes', random.choice(files))
img0 = Image.open(chosen)

images = [
    img0,
    img0.convert('L'),
    img0.resize(tuple([2*x for x in img0.size])),
    img0.resize(tuple([2*x for x in img0.size])).convert('L'),
    img0.resize(tuple([x//2 for x in img0.size])),
    img0.resize(tuple([x//2 for x in img0.size])).convert('L'),
    img0.resize(tuple([x//4 for x in img0.size])),
    img0.resize(tuple([x//4 for x in img0.size])).convert('L'),
]

text_read = []

for img in images:
    text = tess.image_to_string(img, lang='eng+pol')
    text = text.lower()
    text = text.split()
    print(images.index(img), end='\t')
    print(text)

# text_read = tess.image_to_string(img0, lang='eng+pol')
# text_read += tess.image_to_string(img1, lang='eng+pol')
# text_read += tess.image_to_string(img2, lang='eng+pol')
# text_read += tess.image_to_string(img3, lang='eng+pol')
# text_read += tess.image_to_string(img4, lang='eng+pol')
# text_read += tess.image_to_string(img5, lang='eng+pol')
# text_read = text_read.lower()
# text_read = re.sub(r'[^\w\s]', '', text_read)
# words_list = sorted(set(text_read.split()))

# print(words_list)
img0.show()
if input('Put in BAD folder? [y]: ') == 'y':
    shutil.move(chosen, 'bad')
else:
    shutil.move(chosen, 'good')
