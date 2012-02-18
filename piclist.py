# --*-- coding: utf-8 --*--

'''
The file collcects the urls of the featured pic pages from the compiled list
at: http://tawp.in/r/2gxd

Note: This may not be very useful.
'''

import urllib2
import codecs

from BeautifulSoup import BeautifulSoup as bs

url = "http://tawp.in/r/2gxd"

def main():
    ''' The main function '''
    # conctruct the url opener
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    req = opener.open(url)
    # Make Soup
    soup = bs(req.read())
    content = soup.find("div", {"class" : "mw-content-ltr"})
    lis = content.findAll("ol")[1].findAll("li")
    # Get a file to save the urls
    holder = codecs.open("pic_page_urls.list", encoding="utf-8", mode="w+")
    for li in lis:
        holder.write(li.a["href"])
        holder.write("\n")
    holder.close()

if __name__ == "__main__":
    main()
