import codecs
import shutil
import re
import os
import chardet

def convert_encoding(filename):
    # Backup the origin file.
    # convert file from the source encoding to target encoding
    content2b = codecs.open(filename, 'rb').read()
    source_encoding = chardet.detect(content2b)['encoding']
    if source_encoding != None:
        content = content2b.decode(encoding = source_encoding, errors = 'ignore')
        if source_encoding != 'utf-8':
            print(source_encoding, filename)
            codecs.open(filename, 'w', encoding='utf-8').write(content)

filename=input('\n')
convert_encoding(filename)