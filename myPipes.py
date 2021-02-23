#! /usr/bin/env python3
#
#

def hasPipes(args):
    if '|' in args:
        return True
    return False

def splitCommands(args): #splits the commands at the pipe and returns it
    leftArg = [] #holds the left side
    rightArg = [] #holds the right side

    for i in range (len(args)): #finds the pipe symbol
        if (args[i] == '|'):
            leftArg = args[:i]
            rightArg = args[i+1:]
            break;

    return leftArg, rightArg

def validPipes(args): #to make sure the syntax ofthe pipes are valid
    leftArgPos = 0; #holds the position of the first pipe symbol
    rightArgPos = 0; #holds the position of the last pipe symbol

    if(args[0] == '|' or args[-1] == '|'): #if there is a pipe symbol in the first/last arg
        return False

    for i in range(len(args)): #find the position of the pipe symbol
        if (args[i] == '|'): #the first pipe symbol

            if (args[i+1] == '|'): # a second consecutive pipe symbol
                return False
            
            if (leftArgPos == 0):
                leftArgPos = i;
            rightArgPos = i;

    for i in range(len(args)): #check if the redirect syntax in pipes is valid
        if (i < leftArgPos):
            if(args[i] == '>'): #can't have output redirect in first sub command
                return False
        elif(i > rightArgPos): #can't have input redirect on last sub command
            if (args[i] == '<'):
                return False
        else:
            if args[i] == '>' or args[i] == '<':
                return False

    return True
