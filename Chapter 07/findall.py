# -*- coding: utf-8 -*-
import re
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
findall_lists = re.findall(r'([\w\.-]+)@([\w\.-]+)', str)
print findall_lists  ## [('alice', 'google.com'), ('bob', 'abc.com')]
for tuple in findall_lists:
    print tuple[0]  ## username
    print tuple[1]  ## host
