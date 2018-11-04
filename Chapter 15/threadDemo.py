import threading, time
print('Start of program.')

def takeANap():
    time.sleep(5)
    print('Wake up!')
def print_name(*args,**kwargs):
    print( "this is ",args)
    print( "that is ",kwargs)
#threadObj = threading.Thread(target=takeANap)
#threadObj.start()
threadObj = threading.Thread(target=print_name,args=('tom','jerry'),kwargs={"sep":'&'})
threadObj.start()
print('End of program.')
