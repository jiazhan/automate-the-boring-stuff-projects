#!/usr/bin/env python
# encoding: utf-8
import os,re,shutil
pat=re.compile(r'(^Chapter)\s(\d{2})')

for i in os.listdir('.'):
    if os.path.isdir(i):
        g=pat.search(i)
        if g:
            newname=g.group(1)+g.group(2)
            shutil.move(i,newname)


