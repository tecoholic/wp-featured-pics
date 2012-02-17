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

baseurl = "http://ta.wikipedia.org/w/api.php?action=parse&format=json&page="

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
        theurl = (baseurl+url.strip().replace(" ", "_")).encode("UTF-8")
        apireq = opener.open(theurl)
        response = json.loads(apireq.read())
        images = response["parse"]["images"]
        for image in images:
            imageurlsfile.write(image)        
        break # Clear this Mr.Logic :)
    imageurlsfile.close()


if __name__ == "__main__":
    main()
