#!/usr/bin/python

# this is a good way to use: find . -type f -iname "*.dump" -exec ./bytefind.py 00a0f981 '{}' \; | grep -B 1 [+]
# Will find the bytes in any of the files named *.dump

# good way to find a string in lots of similar files
# find . -type f -iname "*.dump" -exec bash -c "echo {}: ; strings -t x {} | grep 123456789" \;

import sys
import string

helptext = "bytefind V0.1\n\tUSAGE: bytefind BYTES FILE"
helptext += "\n\tFinds the exact bytestream BYTES (in hex) in file FILE."
helptext += "\n\tWill print the offset, in hex, in the file where the bytes are FIRST found"
# helptext += "\n\tIf -a specified, then will list all locations of those bytes"
helptext += "\n\tExample: bytefind DEADBEEF in_hamburger.bin"

# check args
if (len(sys.argv) < 3):
    print helptext
    sys.exit()

# Basically no error checking.  It's V 0.1

# break BYTES into list
to_find_string = sys.argv[1]

# first check to make sure its a possible byte list
# even number of bytes?
if (len(to_find_string) % 2):
    print "[!] Bytes come in hex pairs my friend.."
    sys.exit()

# only hex chars?
if not (all(c in string.hexdigits for c in to_find_string)):
    print "[!] Hex digits are only: {}".format(string.hexdigits)
    sys.exit()

# convert to a list
to_find_bytes = bytearray.fromhex(to_find_string)

fileOffset = 0
byteindex = 0
filename = sys.argv[2]
print "[-] Opening file: {}".format(filename)
with open(filename, 'rb') as f:
    while True:
        byte_s = f.read(1)
        if not byte_s:
            break
        thebyte = bytearray(byte_s)[0]
        if (thebyte == to_find_bytes[byteindex]):
            byteindex += 1
            if (byteindex == len(to_find_bytes)):
                # the last piece was found
                print "[+] Bytes found at offset {}".format(hex(fileOffset - (len(to_find_bytes)-1)))
                #sys.exit()
                byteindex = 0
        else:
            byteindex = 0
        fileOffset += 1
    

# print "[-] Bytes not found"

            
