#
#! /usr/bin/env python3
#
# part one of lab1
# shout out to Manuel Ruvalcaba

def hasRedirect(args): # see if there is a redirect
    if "<" in args or ">" in args:
        return True
    return False

def validateRedirection(args): # validates the redirect
    numInput = 0 # stores number of redirects, only one
    numOutput = 0
    normalArgs = []; #stores other normal arguments
    inputArg = "" # stores "goess into" argument
    output = "" #stores output redirection argument
    i = 0

    while (i < len(args)):
        if (args[i] == ">" or args[i] == "<"): # if there is a redirect

            if (i+1 >= len(args)): #if there are no more args, can't do anything 
                return False, "","",[]
            
            if (args[i] == "<"): # if it is input redirect
                numInput +=1 # count a redirect    
                if (numInput > 1): # if there are more than one redirect symbols, can't do anything
                    return False, "", "", []
                inputArg = args[i+1] # valid redirect, store the argument for the input
                i+=1 # skip stored argument
                
            if (args[i] == ">"): #if it is an output redirect
                numOutput +=1 # count a redirect
                if (numOutput > 1): # if there are more than one redirect symbol can't do anything
                    return False, "", "", []
                outputArg = args[i+1] #valid redirect, store the arg for output
                i+=1 # skip stored arg

    return True, inputArg, outputArg 

                

