
#!/usr/bin/env python3
#

import re,os

def myreadline():

    global buf

    buf = ""
    
    while 1:

        buf = os.read(0,1500)
        ibuf = buf.decode()
        sbuf = re.split('\n',ibuf,1)
        
        if (len(sbuf)==2):  #new line in sbuf

            buf = sbuf[1] # everything after new line
           # os.write(1,f"### <{str(sbuf[0])}> ###\n".encode())
            
            return sbuf[0]  # return everything before the new line
    

        else:

            rbuf = os.read(0,1500)
            
            if (len(rbuf) == 0): # check for EOF
                retVal = buf # return last bit
                buf = "" # clear buffer
                return retVal
            
            buf = buf + rbuf.decode() #

        

myreadline()


