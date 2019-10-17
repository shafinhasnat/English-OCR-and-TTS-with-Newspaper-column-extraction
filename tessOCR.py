import pytesseract
from PIL import Image
import glob


def Detect():
    text_list=[]
    files=glob.glob('columns/*.jpg')
    for f in files:
##        print(f)
        img=Image.open(f)
##    img = img.transpose(Image.FLIP_TOP_BOTTOM).transpose(Image.FLIP_LEFT_RIGHT)
        txt=pytesseract.image_to_string(img,lang="eng")
        text_list.append(txt)
    return text_list
def EmptyList():
    l=Detect()
    l.clear()

