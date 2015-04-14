'''
Unpacks each command into its underlying fields
'''
import re

class CommandType:
    A = 1
    C = 2
    L = 3

class Parser:
   
    dest="(?:M=|D=|MD=|A=|AM=|AD=|AMD=)?"
    jump="(?:;JGT|;JEQ|;JGE|;JLT|;JNE|;JLE|;JMP)?"
    comp="(?:[AMD][+-]1|[AM]-D|D[&+-][AM]|D\\|[AM]|[01]|[-!]?[AMD])"
 
    re_A_COMMAND = re.compile("@[A-Za-z]*|@[0-9]*")
    re_C_COMMAND = re.compile(dest + comp + jump)
    re_L_COMMAND = re.compile("([A-Za-z]*)")

    re_comment = re.compile('//|/*')
    
    
    def __init__(self, filename):
        self.infile = open(filename, 'r')        
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
        self.currentCommand = self.infile.readline()
        cleanCommand()

        while len(self.currentCommand) == 0:
            self.currentCommand = self.infile.readline()
            if not self.currentCommand: break
            cleanCommand()

    '''
    Removes whitespace and comments
    '''
    def cleanCommand(self):
        self.currentCommand = re_comment.split(self.currentCommand.strip())[0]

    def commandType(self):

        if re_A_COMMAND.findall(currentCommand)[0] == currentCommand:
            return CommandType.A
        elif re_C_COMMAND.findall(currentCommand)[0] == currentCommand:
            return CommandType.C
        elif re_L_COMMAND.findall(currentCommand)[0] == currentCommand:
            return CommandType.L



