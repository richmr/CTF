#!/bin/bash
# below is a great way to use.  Just replace "tyro" with the name of your process.  super awesome
# ps aux | grep tyro | grep -v grep | cut -d " " -f 7 | { read pid; ./pid-memdump.sh $pid; } 

grep rw-p /proc/$1/maps | sed -n 's/^\([0-9a-f]*\)-\([0-9a-f]*\) .*$/\1 \2/p' | while read start stop; do gdb --batch --pid $1 -ex "dump memory $1-$start-$stop.dump 0x$start 0x$stop"; done
