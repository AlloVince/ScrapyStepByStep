#coding=utf-8
from readability.readability import Document
import urllib
import jieba
import jieba.analyse
from optparse import OptionParser
from HTMLParser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


USAGE = "usage: python article.py [url]"

parser = OptionParser(USAGE)
opt, args = parser.parse_args()
url = args[0] if args and args[0] else 'http://wallstreetcn.com/node/76461'

html = urllib.urlopen(url).read()
readable_article = Document(html).summary()
readable_title = Document(html).short_title()

tags = jieba.analyse.extract_tags(strip_tags(readable_article), 10)
print ",".join(tags)
