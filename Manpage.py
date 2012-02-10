#!/usr/bin/env python
# encoding: utf-8
"""
Manpage.py

Created by Franck Yelles on 2011-12-16.
"""
import urllib2, re,os,sys
from sqlite3 import dbapi2 as sqlite

from BeautifulSoup import BeautifulSoup as BSoup 
DBlist = list()


def RunConversion():
    global DBlist, DBdict
    path="manpages/"
    dirList=os.listdir(path)
    
    for fname in dirList:
        if fname.endswith(".html"):
            DBdict = dict()
            content = False
            print "\nReading",fname
            newstring='.'.join(fname.split('.')[0:-1])+'.txt'
            f = open(path+fname, 'r')
            content  =  f.read() #NAME
            f.close()
            if content:
#            if content :
                try :
                    content = (re.sub(".*[M|n]an.*converted.*","",content))    
                    content = (re.sub(".*man2html.*","",content))    
                    soup = BSoup(content, convertEntities=BSoup.HTML_ENTITIES)
                    c =  ''.join(soup.body(text=True))
                    f = open(path+newstring, 'w')
                    towrite = c.encode('utf-8')
                    cleandata = re.search("(\w+\(.*)",towrite,re.S).group(1)
                    
                    DBdict['name'] = fname.split('.')[0][:-1] + "(" + fname.split('.')[0][-1:] + ")".strip()
                    DBdict['cleandata'] = cleandata.strip()
                    if re.search("NAME\n(.*)\n",cleandata,re.S):       
                        DBdict['header'] =  re.search("NAME\n(.+?)\n",cleandata,re.S).group(1).strip()
                    else:
                        DBdict['header'] = fname.split('.')[0][:-1]
                    DBlist.append(DBdict)
                    
                    f.write(cleandata)
                    f.close()
                    print newstring, " done !"
                except TypeError, e :
                    print "*"*100, "Error", fname
                    ErrorFile.write(str("\tError " + fname+" - "+ str(e) +"\n"))
                except UnicodeEncodeError, e :
                    print "*"*100, "Error", fname
                    ErrorFile.write(str("\t\tError " + fname+" - "+ str(e) +"\n"))
                except AttributeError, e :
                    print "*"*100, "Error", fname
                    ErrorFile.write(str("\t\t\tError " + fname+" - "+ str(e) +"\n"))

                    # print re.search("NAME\n(.*)\n",cleandata,re.S).group(1)
            else:
                sys.exit()                              
    
def RunDB():
    global DBlist
    conn = sqlite.connect("dbs/manpage.sqlite")
    ErrorFile = open("manpages/_error.log", 'w')


    for a in DBlist :
        print "About to insert",a['name']," !"
        cursor = conn.cursor()
        try :
            SQLQ= "insert into manpage values (null, '%s', '%s', '%s',null)" % (a['name'], a['header'], a['cleandata'])
            cursor.execute(SQLQ)
            conn.commit()
            cursor.close()
        except Exception, e :
            print "Error with ",a['name']
            ErrorFile.write(a['name']+str(e))  
            
        print "Done with",a['name']," !"
        
    conn.close()
    ErrorFile.close()        
def main():
    RunConversion()
    RunDB()


if __name__ == '__main__':
    main()

