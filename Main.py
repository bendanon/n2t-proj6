'''
Initializes I/O files and drives the show.
'''
from Parser import Parser, CommandType
from SymbolTable import SymbolTable
from Code import Code


def first_pass(path):
    p = Parser(path)

    symbol_table = SymbolTable()
    n = 0
    while(p.hasMoreCommands()):
        p.advance()
        command_type = p.commandType()
        if(command_type == CommandType.L):
            symbol_table.add_entry(p.symbol(), n)
        else:
            n += 1
    return symbol_table


def second_pass(path, symbol_table):
    p = Parser(path)
    code = Code()
    ram_address = 16
    while(p.hasMoreCommands()):
        p.advance()
        command_type = p.commandType()
        if (command_type == CommandType.L):
            continue
        elif (command_type == CommandType.C):
            dest = code.dest(p.dest())
            comp = code.comp(p.comp())
            jump = code.jump(p.jump())
            binary = bin("111" + comp + dest + jump)
        else:  # command_type == CommandType.A
            symbol = p.symbol()
            if symbol.isdigit():
                address = int(symbol)
            else:
                if not symbol_table.contains(symbol):
                    symbol_table.add_entry(symbol, ram_address)
                    ram_address += 1
                address = symbol_table.get_address(symbol)
            binary = address
        print format(binary, '016b')


def main():
    ams_file_path = "Input/max/Max.asm"
    symbol_table = first_pass(ams_file_path)
    second_pass(ams_file_path, symbol_table)
    return

if __name__ == '__main__':
    main()
