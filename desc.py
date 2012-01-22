# --*-- coding:utf-8 --*--

''' Ths function collects the picture page url and the description for the
picture. The urls are taken from the pic_page_urls.list
'''

import os
import urllib2
import codecs

from BeautifulSoup import BeautifulSoup as bs

def main():
    ''' The main function '''
    if not os.path.isdir("text"):
        os.mkdir("text")
    opener = urllib2.build_opener()
    opener.addheaders = [("User-agent", "Mozilla/5.0")]
    urlfile = open("pic_page_urls.list", "r")
    imageurlsfile = codecs.open("image_urls.list", encoding="utf-8", mode="w+")
    filecount = 1
    for url in urlfile.readlines():
        descpage = opener.open(url)
        soup = bs(descpage.read())
        content = soup.find("div", {"class" : "mw-content-ltr"})
        tds = content.findAll("td")
        # image page url
        imageurl = tds[0].a["href"]
        imageurlsfile.write(imageurl+"\n")
        # image description
        imagedesc = tds[1].text.strip()
        textfile = codecs.open(os.path.join("text", "text_%03d.txt"%filecount),
                               encoding="utf-8", mode="w+")
        textfile.write(imagedesc)
        textfile.close()
        filecount += 1
        break # remove this @logic :D
    imageurlsfile.close()


if __name__ == "__main__":
    main()
