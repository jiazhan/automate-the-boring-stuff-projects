#!/usr/bin/env python
# encoding: utf-8
import logging
import requests
logging.disable(logging.CRITICAL)
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(message)s')
logging.debug("debug message")
logging.info("info message")
 url='http://www.google.com'
 while True:
    try:
       time.sleep(2)
       res=requests.get("http://www.google.comd")
       res.raise_for_status()

     except Exception as err:
         print('oops,errror:{}'.format(err))

