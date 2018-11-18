#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re
words={"ADJECTIVE":"pls input an adj:","NOUN":"pls input noun:","VERB":"pls input an verb:",}
newfileObj= open ('/home/kevin/new_silly','w')
with open ('/home/kevin/silly') as fileObj:
    for line in fileObj.readlines():
        for i in line.split():
            i=i.strip(' |.')
            if i  in words:
                user_input=raw_input(words[i])
                pat=re.compile(i)
                line=pat.sub(user_input,line,count=1)
        newfileObj.writelines(line)
newfileObj.close()

