from konlpy.tag import Kkma
from icecream import ic
from common.moldels import FileDTO, Reader
from wordcloud import WordCloud, STOPWORDS
import numpy as np
import matplotlib.pyplot as plt
import platform
from matplotlib import font_manager, rc
from PIL import Image


class Service(Reader):

    def __init__(self):
        self.f = FileDTO()
        self.r = Reader()

    def pltshow(self):
        f = self.f
        r = self.r
        f.context = './data/'
        f.filename = '09. alice_mask'
        alice_mask = r.img(f)
        path = "c:/Windows/Fonts/Calibri.ttf"
        if platform.system() == 'Darwin':
            rc('font', family='AppleGothic')
        elif platform.system() == 'Windows':
            font_name = font_manager.FontProperties(fname=path).get_name()
            rc('font', family=font_name)
        else:
            print('Unknown system... sorry~~~~')


    def setwc(self):
        f = self.f
        r = self.r
        f.context = './data/'
        f.filename = '09. alice'
        text = r.text(f)
        alice_mask = r.img(f)
        stopwords = set(STOPWORDS)
        stopwords.add("said")
        wc = WordCloud(background_color='white', max_words=2000, mask=alice_mask,
                       stopwords=stopwords)
        wc = wc.generate(text)
        wc.words_

    def printwc(self):
        plt.figure(figsize=(8, 8))
        plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
        plt.axis('off')
        plt.show()


if __name__ == '__main__':
    s = Service()
    s.pltshow()
    s.setwc()



