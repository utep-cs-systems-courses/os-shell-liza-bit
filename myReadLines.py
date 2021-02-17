#
#! /usr/bin/env python3
#

import os, sys, re


buffer = os.read(0,100)
next = 0
limit = 0

def mygetchar():
    
    #the buffer is empty
    if next == limit: 
        next = 0
        
        #the call to read for mygetchar
        limit = os.read(0,100)

        #EOF if read brought us nothing or ctrl d
        if limit == 0:
            return EOF

        #if buffer did have chars, pluck the first one
        c = buffer(next)

        # pluck the next char
        next++

        #return the chars we plucked from read
        return c

def myreadlines():

    #keep track of the number of lines we get
    numLines = 0

    #calling mygetchar to fill the buffer with chars
    inLine = stdin.mygetchar()

    #while there are chars to read in the buffer
    while len(inLine):

        #split at the new line character
        myLine = inLine.split('\n')

        #print the line that we got from the buffer
        os.write(1,f"### <{str(myLine)}> ### \n".encode())

        
