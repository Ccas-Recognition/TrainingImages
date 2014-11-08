from os import listdir, remove
from os.path import isfile, join, splitext, isfile
import re
import xml.etree.ElementTree as ET

mypath = './bg/'
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]


removeFiles = []
for file in onlyfiles:
    fileName, fileExtension = splitext(file)
    if(fileExtension != '.xml'):
        continue
    print(fileName)
    index = 0
    xml_file = mypath + file
    tree = ET.parse( xml_file )
    text = tree.getroot().find('images').text;
    #images = re.findall(r"[\w\.]+", text)
    images = []
    for s in text.split(' '):
        if s.strip():
            for s1 in s.split('\n'):
                if s1.strip():
                    startIndex = 0
                    endIndex = len(s1)
                    if s1[0] == '"':
                        startIndex = 1
                        endIndex = endIndex - 1
                    images.append(s1[startIndex:endIndex])
    save_files = []
    remove_files = []
    for image in images:
        if (index % 7) == 0:
            save_files.append(image)
        else:
            if isfile( mypath + image ):
                remove_files.append(image)
                remove( mypath + image )
        index += 1
    output_text = '\n'
    index = 0
    #print(len(save_files))
    #print(len(remove_files))
    for saved_file in save_files:
        output_text += '"' + saved_file + '"'
        output_text += ' '
        if index % 2 == 1:
            output_text += '\n'
        index += 1
    tree.getroot().find('images').text = output_text
    tree.write( xml_file );
    
#mypath = './fg/'
#onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]

