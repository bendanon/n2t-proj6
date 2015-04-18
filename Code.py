'''
Translates each field into its corresponding binary value,
and assembles the resulting values
'''


class Code:

    def __init__(self):
        self.jump_dict = {None: 0, "JGT": 1, "JEQ": 2, "JGE": 3, "JLT": 4,
                          "JNE": 5, "JLE": 6, "JMP": 7}
        self.dest_dict = {None: 0, "M": 1, "D": 2, "MD": 3, "A": 4, "AM": 5,
                          "AD": 6, "AMD": 7}
        self.comp_dict = {"0": 0b101010, "1": 0b111111, "-1": 0b111010,
                          "D": 0b001100, "A": 0b110000, "M": 0b110000,
                          "!D": 0b001101, "!A": 0b110001, "!M": 0b110001,
                          "-D": 0b001111, "-A": 0b110011, "-M": 0b110011,
                          "D+1": 0b011111, "A+1": 0b110111, "M+1": 0b110111,
                          "D-1": 0b001110, "A-1": 0b110010, "M-1": 0b110010,
                          "D+A": 0b000010, "D+M": 0b000010, "D-A": 0b010011,
                          "D-M": 0b010011, "A-D": 0b000111, "M-D": 0b000111,
                          "D&A": 0b000000, "D&M": 0b000000, "D|A": 0b010101,
                          "D|M": 0b010101}

    def dest(self, mnemonic):
        if not mnemonic.isdigit():
            mnemonic = self.dest_dict[mnemonic]
        return format(mnemonic, '03b')

    def jump(self, mnemonic):
        if not mnemonic.isdigit():
            mnemonic = self.jump_dict[mnemonic]
        return format(mnemonic, '03b')

    def comp(self, mnemonic):
        comp = self.comp_dict[mnemonic]
        comp = format(comp, '06b')
        if 'A' in mnemonic:
            return '0' + comp
        else:
            return '1' + comp
