
#!/usr/bin/env python3
import logging,time,requests
logging.basicConfig(filename='/var/log/pinggoogle.log', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.info('Start of program')
url='http://www.google.com'
count=0
while count<55:
    try:
        logging.debug('trying to connect {}'.format(url))
        time.sleep(5)
        res=requests.get(url)
        res.raise_for_status()
    except Exception as err:
        logging.debug('Oops,Errror:{}'.format(err))
    else:

        logging.debug('Awesome,Got Google')
    finally:
        count+=5
        logging.info('End of program')
