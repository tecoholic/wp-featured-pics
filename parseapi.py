# --*-- coding:utf-8 --*--

''' 
This function collects the picture page url and the description for the
picture. The urls are taken from the pic_page_urls.list
'''

import os
import urllib, urllib2
import codecs
import json

from BeautifulSoup import BeautifulSoup as bs
from BeautifulSoup import NavigableString as ns

baseurl = "http://ta.wikipedia.org/w/api.php?action=parse&format=json&page="
invalid = ["a", "b", "i", "u"]

''' From http://stackoverflow.com/questions/1765848/remove-a-tag-using-beautifulsoup-but-keep-its-contents '''
def strip_tags(soup, invalid_tags):
    '''Returns html free text. params (BeautifulSoup Object , invalid_tags List)'''
    for tag in soup.findAll(True):
        if tag.name in invalid_tags:
            s = ""
            for c in tag.contents:
                if not isinstance(c, ns):
                    c = strip_tags(c, invalid_tags)
                s += unicode(c)
            try:
                tag.replaceWith(s)
            except AttributeError:
                pass
    return soup

def main():
    ''' The main function '''
    if not os.path.isdir("text"):
        os.mkdir("text")
    opener = urllib2.build_opener()
    opener.addheaders = [("User-agent", "Tecoholic")]
    urlfile = codecs.open("pic_page_urls.list", encoding="utf-8", mode="r+")
    imageurlsfile = codecs.open("image_urls.list", encoding="utf-8", mode="w+")
    filecount = 1
    for url in urlfile.readlines():
        filecount += 1
        if filecount > 48:
            print "Opening: "+url.strip().replace("/wiki/", "")
            theurl = (baseurl+url.strip().replace("/wiki/", "")).encode("UTF-8")
            apireq = opener.open(theurl)
            response = json.loads(apireq.read())
            images = response["parse"]["images"]
            for image in images:
                imageurlsfile.write(image)
            text = response["parse"]["text"]["*"]
            soup = bs(text).find("p")
            print soup
            imagedesc = strip_tags(soup, invalid)
            textfile = codecs.open(os.path.join("text", "text_%03d.txt"%filecount),
                                   encoding="utf-8", mode="w+")
            print "Writing to : text_%03d.txt\n"%filecount
            textfile.write(unicode(imagedesc))
            textfile.close()
        if filecount > 50:
            break # Clear this Mr.Logic :)
    imageurlsfile.close()


if __name__ == "__main__":
    main()
