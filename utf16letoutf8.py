#!/usr/bin/python

import sys
import re
import glob
import codecs


input_filename = 'utf16le.txt'
input_file = open(input_filename, 'r')

for line in input_file:
    filename = re.sub(r'[\n|\r]',r'',line)
    f = codecs.open(filename, 'r', 'utf-16-le')
    
    # get the file name
    file_name = re.sub(r'\.txt',r'',f.name)
    file_name = re.sub(r'\.TXT',r'',file_name)

    # get file path
    matches = re.findall('[\w\s]+\/', file_name)
    path = ''
    for m in matches:
        path = path + m

    #path = path + "normed/"

    file_name = re.sub(r'[\w\s]+\/',r'',file_name)

    # output file name
    output_file_name = path + file_name + ".txt"
    print(output_file_name)


    u = f.read()   # now the contents have been transformed to a Unicode string
    out = codecs.open(output_file_name, 'w', 'utf-8')
    out.write(u)
    out.close()
    
