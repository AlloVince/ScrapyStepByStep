from pyquery import PyQuery
import pprint
import types
from urlparse import urlparse

def p(v):
    if type(v) is types.ClassType:
        pprint.pprint(vars(v))
    else:
        pprint.pprint(v)

'''
dom = PyQuery(url='http://avnpc.com/')
res = []
for post in dom.items('h3 a'):
    res.append({
        "title" : post.text(),
        "url" : post.attr("href")
    })

print res
'''

url = urlparse("http://avnpc.com/pages/c-pointer/".rstrip('/'))
filename = 'index.html' if url.path == '/' else url.path.split("/")[-1] + '.html'
print filename
