#!/usr/bin/env python
# encoding: utf-8
''' use requests and bs4 module to get the example zip file from nostarch.com'''
import sys,os,requests,bs4,argparse
weburl='https://nostarch.com/'
download_dir='/home/kevin/auto_py/automate-the-boring-stuff-projects/'
print("download example.zip to %s"%download_dir)
get_url=requests.get(weburl+'automatestuff')
get_url.raise_for_status()
bsoup=bs4.BeautifulSoup(get_url.text,features="html.parser")
# select the part of zip link
bselect=bsoup.select('.resources a')
for elem in bselect:
    if 'Download the files used in the book' == elem.getText():
        downloadurl=elem['href']
downloadurl=weburl+downloadurl
get_zip=requests.get(downloadurl)
get_zip.raise_for_status()
download_file=os.path.join(os.path.abspath(download_dir),os.path.basename(downloadurl))
with open(download_file,'wb') as fileob:
    for chunk in get_zip.iter_content(100000):
        fileob.write(chunk)



