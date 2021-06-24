from abc import *
from dataclasses import dataclass
import numpy as np
from PIL import Image
from matplotlib import font_manager, rc
import platform
from wordcloud import WordCloud, STOPWORDS


@dataclass
class FileDTO(object):

    context: str
    filename: str


    @property
    def context(self) -> str: return self._context

    @context.setter
    def context(self, context): self._context = context

    @property
    def filename(self) -> str: return self._filename

    @filename.setter
    def filename(self, filename): self._filename = filename


class ReaderBase(metaclass=ABCMeta):

    @abstractmethod
    def newfile(self):
        pass

    @abstractmethod
    def text(self):
        pass

    @abstractmethod
    def img(self):
        pass


class Reader(ReaderBase):

    def newfile(self, file) -> str:
        return file.context + file.filename

    def text(self, file) -> object:
        return open(f'{self.newfile(file)}.txt').read()

    def img(self, file) -> object:
        return np.array(Image.open(f'{self.newfile(file)}.png'))











