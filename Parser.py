import re


class Parser:
    """
    Encapsulates access to the input code. Reads an assembly
    command, parses it, and provides convenient access to the
    command's components (fields and symbols). In addition,
    removes all white spaces and comments.
    """
    def __init__(self, filename):
        self.commands = [self.cleanCommand(line)
                         for line in open(filename).readlines()]
        self.commands = filter(lambda c: c != "", self.commands)

        self.current_index = 0
        self.currentCommand = self.commands[self.current_index]
        self.current_type = self.ParseCommandType(self.currentCommand)

    def hasMoreCommands(self):
        '''
        Are there more commands in the input?
        This method runs to the next meaningful line, and returns true
        if one exists (false otherwise).
        '''
        return self.current_index < len(self.commands)

    def advance(self):
        '''
        Reads the next command from the input and makes it the current
        command. Should be called only if hasMoreCommands is true.
        '''
        self.current_index += 1
        if self.hasMoreCommands():
            self.currentCommand = self.commands[self.current_index]
            self.current_type = self.ParseCommandType(self.currentCommand)

    def commandType(self):
        return self.current_type

    def symbol(self):
        if self.current_type == CommandType.A:
            return self.currentCommand.split("@")[1]

        if self.current_type == CommandType.L:
            return self.currentCommand.split("(")[1].split(")")[0]

    def dest(self):
        if self.current_type == CommandType.C:
            dest = max(re_dest.findall(self.currentCommand), key=len)
            if(dest is not None and dest != ''):
                return dest.split("=")[0]
        return None

    def comp(self):
        if self.current_type == CommandType.C:
            if self.dest() is not None:
                comp = max(re_comp.findall(self.currentCommand.split("=")[1]),
                           key=len)
            else:
                comp = max(re_comp.findall(self.currentCommand), key=len)
            return comp
        return None

    def jump(self):
        if self.current_type == CommandType.C:
            jump = max(re_jump.findall(self.currentCommand), key=len)
            if(jump is not None and jump != ''):
                return jump.split(";")[1]
        return None

    def cleanCommand(self, command):
        '''
        Removes whitespace and comments
        '''
        return command.split('/')[0].strip()

    def ParseCommandType(self, command):
        aCmd = re_A_COMMAND.findall(command)
        if len(aCmd) > 0 and aCmd[0] == command:
            return CommandType.A

        cCmd = re_C_COMMAND.findall(command)
        if len(cCmd) > 0 and cCmd[0] == command:
            return CommandType.C

        lCmd = re_L_COMMAND.findall(command)
        if len(lCmd) > 0 and lCmd[0] == command:
            return CommandType.L

        return CommandType.E


class CommandType:
    E = 0  # Empty
    A = 1  # A-Instruction
    C = 2  # C-Instruction
    L = 3  # Label

dest = "(?:M=|D=|MD=|A=|AM=|AD=|AMD=)?"
jump = "(?:;JGT|;JEQ|;JGE|;JLT|;JNE|;JLE|;JMP)?"
comp = "(?:[AMD][+-]1|[AM]-D|D[&+-][AM]|D\\|[AM]|[01]|[-!]?[AMD1])"
legalCharsInLabel = "[A-Za-z_0-9\.\$]*"

re_A_COMMAND = re.compile("@"+legalCharsInLabel)
re_dest = re.compile(dest)
re_jump = re.compile(jump)
re_comp = re.compile(comp)
re_C_COMMAND = re.compile(dest + comp + jump)
re_L_COMMAND = re.compile("\(" + legalCharsInLabel + "\)")

def Test():
    p = Parser("/home/ben/CS/Master/Nand2Tetris/projects/06/Assembler/stam")
    if(p.hasMoreCommands()):
        p.advance()
        print p.commandType()
        print p.comp()
        print p.dest()
        print p.jump()

