#
#!/usr/bin/env python3
#

import os, re

def redirOut(args):
    os.close(1) #remove fd 1 to screen

    out_indicate = args.index('>')+1

    os.open(args[out_indicate], os.O_WRONLY | os.O_CREAT) #out file
    os.set_inheritable(1,True)

    args.remove(args[out_indicate]) #remove argument from args, already used it, don't need
    args.remove('>') #remove output indicator, same reason

    execute_redir(args)

def redirIn(args):
    os.close(0) #remove fd 0 from keyboard

    in_indicate = args_index('<')+1

    os.open(args[in_indicate]), os.O_RDONLY) #in file
    os.set_inheritable(0,True)

    args.remove(args[in_indicate]) #remove, already used, don't need anymore
    args.remove('<') # remove, same reason

    execute_redir(args)

def execute_redir(args):
    for dir in re.split(":", os.environ["PATH"]): #try each directory in path
        program = "%s/%s" % (dir, args[0])

        try:
            os.execve(program, args, os.environ) # try to execute the problem

        except FileNotFoundError: #... expected
            pass #... fail quietly
