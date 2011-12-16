#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Franck Yelles on 2011-12-16.
Copyright (c) 2011 __MyCompanyName__. All rights reserved.
"""
#'/Users/fyelles/Desktop/man-html-20111120/htmlman1/head.1.html'
import urllib2, re,os
from BeautifulSoup import BeautifulSoup as BSoup 

# f = open('/Users/fyelles/Desktop/man-html-20111120/htmlman1/chroot.1.html', 'r')
# content  =  f.read() 
# f.close()
# 
# 
# soup = BSoup(content, convertEntities=BSoup.HTML_ENTITIES) 
# # only the text nodes between body tags. 
# a =  ''.join(soup.body(text=True))
# 
# f = open('2.txt', 'w')
# f.write((re.sub('\n{3,}','\n\n',a)).encode('utf-8')) 
# #f.write(a.replace('\n{3,}', '\n').encode('utf-8')) 
# 
# f.close()
for i in range(1,9):
    if i is not 6 :
        path="/Users/fyelles/Desktop/man-html-20111120/htmlman%s/"% ( str(i))  # insert the path to the directory of interest
        dirList=os.listdir(path)
        for fname in dirList:
            if fname.endswith(".html"):
                content = False
                print "\nReading",fname
                newstring='.'.join(fname.split('.')[0:-1])+'.txt'
                f = open(path+fname, 'r')
                content  =  f.read() 
                f.close()    
                soup = BSoup(content, convertEntities=BSoup.HTML_ENTITIES)
                c =  ''.join(soup.body(text=True))
                f = open(path+newstring, 'w')
                f.write((re.sub('\n{3,}','\n\n',c)).encode('utf-8')) 
                f.close()
                print newstring, " done !"

def main():
    pass


if __name__ == '__main__':
    main()

