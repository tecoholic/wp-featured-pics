# --*-- coding:utf-8 --*--

''' 
This function collects the picture page url and the description for the
picture. The urls are taken from the pic_page_urls.list
'''

import os
import urllib, urllib2
import codecs

from BeautifulSoup import BeautifulSoup as bs

baseurl = "http://ta.wikipedia.org/w/api.php?action=query&prop=revisions&\
format=xml&rvprop=content&rvlimit=1&rvdir=older&titles="

def main():
    ''' The main function '''
    if not os.path.isdir("text"):
        os.mkdir("text")
    opener = urllib2.build_opener()
    opener.addheaders = [("User-agent", "Tecoholic")]
    urlfile = codecs.open("pic_page_urls.list", encoding="utf-8", mode="r+")
    #imageurlsfile = codecs.open("image_urls.list", encoding="utf-8", mode="w+")
    filecount = 1
    for url in urlfile.readlines():
        theurl = (baseurl+url.strip().replace(" ", "_")).encode("UTF-8")
        descpage = opener.open(theurl)
        soup = bs(descpage.read())
        content = soup.find("rev")
        # image page url
        #imageurl = 
        # image description
        # ---- FIXME -----
        imagedesc = content.text
        textfile = codecs.open(os.path.join("text", "text_%03d.txt"%filecount),
                               encoding="utf-8", mode="w+")
        textfile.write(imagedesc)
        textfile.close()
        filecount += 1
        break # remove this @logic :D
    #imageurlsfile.close()


if __name__ == "__main__":
    main()
