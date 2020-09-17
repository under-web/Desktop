# -*- coding: utf-8 -*
from lxml.html import parse

s = u'собака'
dom = parse("http://www.google.ru/search?q=%s" % s).getroot()
links = dom.cssselect('a')

links = iter(links)
for n, l in enumerate(links):
    u = l.text_content()
    # print unicode(u),
    print(unicode(l.values()))
