'''
Unpacks each command into its underlying fields
'''

from enum import Enum
CommandType = Enum('A_COMMAND', 'C_COMMAND', 'L_COMMAND')

import re



class Parser:
    
    re_A_COMMAND = re.compile('@[A-Z]')
    
    def __init__(self, filename):
        self.infile = open('workfile', 'r')        
        self.moreCommands = False
        self.currentCommand = None

    '''
    Are there more commands in the input?
    '''
    def hasMoreCommands(self, trick):
        return self.moreCommands

    '''
    Reads the next command from the input and makes it the current
    command. Should be called only if hasMoreCommands is true.
    Initially, there is no current command
    '''
    def advance(self)
        return None

    def commandType(self):
        if 
