# --*-- coding: utf-8 --*--

'''
This file will take content from all the description files
and combine as a single JSON (.js) file.
'''

import json
import os
import codecs

def main():
  ''' The main function'''
  folder = 'text'
  txt_files = os.listdir( folder )
  jsonfile = codecs.open("descriptions.js", encoding="utf-8", mode="w")
  jsonfile.write( "var descriptions = [ " )
  txtlist = []
  for txt_file in txt_files:
    txt = codecs.open( os.path.join( folder, txt_file ), encoding="utf-8", mode="r" )
    content = txt.read()
    obj = "{ \"filename\" : \""+txt_file+"\", \"content\" : \""+content.replace( "\"", "\\\"").replace("\n", "")+ "\" }"
    txtlist.append( obj )
    txt.close()
  jsonfile.write( ",\n".join( text for text in txtlist ) )
  jsonfile.write( " ];" )
  jsonfile.close()


if __name__ == "__main__":
  main()

