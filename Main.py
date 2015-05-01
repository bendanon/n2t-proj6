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
        command_type = p.commandType()
        if(command_type == CommandType.L):
            symbol_table.add_entry(p.symbol(), n)
        else:
            n += 1
        p.advance()
    return symbol_table


def second_pass(path, symbol_table):
    p = Parser(path)
    code = Code()
    ram_address = 16
    hack = []
    while(p.hasMoreCommands()):
        command_type = p.commandType()
        if (command_type == CommandType.L):
            p.advance()
            continue
        elif (command_type == CommandType.C):
            dest = code.dest(p.dest())
            comp = code.comp(p.comp())
            jump = code.jump(p.jump())
            command = int("111" + comp + dest + jump, 2)
        else:  # command_type == CommandType.A
            symbol = p.symbol()
            if symbol.isdigit():
                address = int(symbol)
            else:
                if not symbol_table.contains(symbol):
                    symbol_table.add_entry(symbol, ram_address)
                    ram_address += 1
                address = symbol_table.get_address(symbol)
            command = address
        command = format(command, '016b')
        hack.append(command)
        p.advance()
    return hack


def main():
    asm_file_path = "Input/rect/Rect.asm"
    hack_file_path = "Input/rect/Rect.hack"
    symbol_table = first_pass(asm_file_path)
    hack = second_pass(asm_file_path, symbol_table)
    with open(hack_file_path, 'w') as output:
        for line in hack:
            output.write(line + "\n")

if __name__ == '__main__':
    main()
