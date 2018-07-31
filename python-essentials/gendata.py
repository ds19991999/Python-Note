# coding=utf-8
# 创建随机数据，然后将生成的数据输出到屏幕
from random import randrange, choice
from string import ascii_lowercase as lc
from sys import maxint
from time import ctime

tlds = ( 'com', 'edu', 'net', 'org', 'gov' )

for i in xrange(randrange(5, 11)):
    dtint = randrange(maxint)	# pick date
    dtstr = ctime(dtint)	# date string
    llen = randrange(4, 7)	# login is shorter
    login = ''.join(choice(lc) for j in range(llen))
    dlen = randrange(llen, 13)	# domain is longer
    dom = ''.join(choice(lc) for j in xrange(dlen))
    print '%s::%s@%s.%s::%d-%d-%d' % (dtstr, login,
	dom, choice(tlds), dtint, llen, dlen)