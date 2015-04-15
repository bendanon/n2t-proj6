'''
Unpacks each command into its underlying fields
'''
import re

class CommandType:
    E = 0
    A = 1
    C = 2
    L = 3
    
dest="(?:M=|D=|MD=|A=|AM=|AD=|AMD=)?"
jump="(?:;JGT|;JEQ|;JGE|;JLT|;JNE|;JLE|;JMP)?"
comp="(?:[AMD][+-]1|[AM]-D|D[&+-][AM]|D\\|[AM]|[01]|[-!]?[AMD])"

re_A_COMMAND = re.compile("@[A-Za-z]*|@[0-9]*")
re_dest = re.compile(dest)
re_jump = re.compile(jump)
re_comp = re.compile(comp)
re_C_COMMAND = re.compile(dest + comp + jump)
re_L_COMMAND = re.compile("([A-Za-z]*)")

re_comment = re.compile('//|/*')

class Parser:
    
    def __init__(self, filename):
        self.infile = open(filename, 'r')        
        self.moreCommands = False
        self.currentCommand = ''
        self.nextCommand = ''
        self.currentCommandType = CommandType.E
        self.nextCommandType = CommandType.E        


    '''
    Removes whitespace and comments
    '''
    def cleanCommand(self, command):
        return re_comment.split(command.strip())[0]

    def getCommandType(self, command):
        aCmd = re_A_COMMAND.findall(command)
        if len(aCmd) > 0 and aCmd[0] == command:
            return CommandType.A

        cCmd = re_C_COMMAND.findall(command)
        if len(cCmd) > 0 and cCmd[0] == command:
            return CommandType.C
        
        lCmd = re_L_COMMAND.findall(command)
        if len(lCmd) > 0 and Cmd[0] == command:
            return CommandType.L
        
        return CommandType.E
    
    '''
    Are there more commands in the input?
    This method runs to the next meaningful line, and returns true
    if one exists (false otherwise). It sets nextCommand with it.
    And sets nextCommandType with its type
    '''
    def hasMoreCommands(self):
        rawLine = self.infile.readline()
        while len(rawLine) != 0:
            cleanLine = self.cleanCommand(rawLine)
            if(len(cleanLine) != 0):
                cmdType = self.getCommandType(cleanLine)
                if(cmdType != CommandType.E):
                    self.nextCommand = cleanLine
                    self.nextCommandType = cmdType
                    return True
            rawLine = self.infile.readline()

        return False

    '''
    Reads the next command from the input and makes it the current
    command. Should be called only if hasMoreCommands is true.
    Initially, there is no current command
    '''
    def advance(self):
        self.currentCommand = self.nextCommand
        self.currentCommandType = self.nextCommandType 

    def commandType(self):
        return self.currentCommandType

    def symbol(self):
        if self.currentCommandType == CommandType.A:       
            return self.currentCommand.split("@")[1]
    
        if self.currentCommandType == CommandType.L:
            return self.currentCommand.split("(")[1].split(")")[0]

    def dest(self):
        if self.currentCommandType == CommandType.C:            
            dest = max(re_dest.findall(self.currentCommand), key=len)
            if(dest != None):
                return dest.split("=")[0]
        return None

    def comp(self):
        if self.currentCommandType == CommandType.C:
            comp = max(re_comp.findall(self.currentCommand), key=len)
            return comp
        return None

    def jump(self):
        if self.currentCommandType == CommandType.C:
            jump = max(re_jump.findall(self.currentCommand), key=len)
            if(jump != None):
                return jump.split(";")[1]
        return None


def Test():
    p = Parser("/home/ben/CS/Master/Nand2Tetris/tools/test.asm")
    
    if(p.hasMoreCommands()):
        p.advance()
        print "dest is " + p.dest()
        print "comp is " + p.comp()
        print "jump is " + p.jump()
    else:
        print "no more commands"


Test()

