#
#!/usr/bin/env python3
#

import os, sys, time, re
from myReadLine import myreadline
from myRedirect import redirOut, redirIn
from myPiping import pipeCmd

def main():

    while True: #shell runs forever
        if 'PS1' in os.environ:
            os.write(1,(os.environ['PS1']).encode())
        else:
            os.write(1,("$ ").encode())

        inputBuff = myreadline()

        if len(inputBuff) > 0:
            inputHandler(inputBuff)


def inputHandler(inputBuff):

    if len(inputBuff) == 0:
        return

    if inputBuff == "exit": #user wants to exit shell
        os.write(1("Exiting... Goodbye! \n").encode())
        sys.exit(0)

    args = inputBuff.split(' ')

    if args[0] == "pwd": #print working directory command
        os.write(1,(os.getcwd() + "\n") # os.getcwd returns current working directory

    elif args[0] == "cd":
        try:
            if len(args) < 2: #no args in the cd command
                 return
            else:
                 os.chdir(args[1])
        except
            os.write(1("cd %s: No such file or directory \n" % args[1])

    else:
        rc = os.fork() #return the child's process ID (PID)

        if rc < 0: #fork failed
            os.write(2, ("Fork failed... returning %d\n" % rc).encode())
            sys.exit(1) #unsucccessful termination

        elif rc == 0: #fork successful

            if '<' in args:
                redirIn(args) #redirect into indicator

            elif '>' in args:
                redirOut(args) #redirect out to indicator

            elif '|' in args:
                pipeCmd(args) #pipe

            else:
                doCommand(args)
                sys.exit(0) #successful termination

def doCommand(args):
    for dir in re.split(":", os.environ["PATH"]): #try each directory in path
        program = "%s%s" % (dir, args[0])
        try:
            os.execve(program, args, os.environ) #try to execute the program
        except FileNotFoundError: #expected
            pass #fail quietly

    os.write(2, ("%s: could not execute\n" % args[0]).encode())
    sys.exit(1) #terminate with error

if __name__ == "__main__":
    main()
