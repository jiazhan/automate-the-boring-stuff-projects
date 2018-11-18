#!/usr/bin/env python
# mcb.pyw - Saves and loads pieces of text to the clipboard

# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
import shelve, pyperclip, sys
def usage():
    print """
    Usage:
        py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
        py.exe mcb.pyw list - Loads all keywords to clipboard.
        """
    sys.exit(1)
if len(sys.argv) <= 1:
    usage()
mcb_shelf = shelve.open('mcb')

# TODO: Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
if len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    if sys.argv[2] in mcb_shelf:
        print ("deleted the value of key %s"%(sys.argv[2]))
        mcb_shelf.pop(sys.argv[2])
    else:
        print ("error: pls input a valid key in the file")
elif len(sys.argv) == 2:
    # TODO: List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcb_shelf.keys())))
        if len(mcb_shelf.keys()) !=0:
            print ("the file %r has following keys and values" %(__file__))
            for key,value  in mcb_shelf.iteritems():
                print ("key---> %s value--->%s" %(key,value))
            print ("all keys of file %s copied, pls paste it in clipboard to check"%(__file__))
        else:
            print ("the file %s is empty!"%(__file__))
    elif sys.argv[1].lower() == 'dall':
        mcb_shelf.clear()
        print('All keywords and associated contents have been deleted')
    elif sys.argv[1] in mcb_shelf:
        print ("copied the value of key %s, pls paste it in clipboard"%(sys.argv[1]))
        pyperclip.copy(mcb_shelf[sys.argv[1]])
    else:
        print ("the keyword %s does not exist in file %s" %(sys.argv[1],__file__))


mcb_shelf.close()
