'''
Translates each field into its corresponding binary value,
and assembles the resulting values
'''


class Code:

    def __init__(self):
        self.jump_dict = {None: "000", "JGT": "001", "JEQ": "010",
                          "JGE": "011", "JLT": "100", "JNE": "101",
                          "JLE": "110", "JMP": "111"}
        self.dest_dict = {None: "000", "M": "001", "D": "010", "MD": "011",
                          "A": "100", "AM": "101", "AD": "110", "AMD": "111"}
        self.comp_dict = {}

    def dest(self, mnemonic):
        return self.dest_dict.get(mnemonic)

    def comp(self, mnemonic):
        return self.comp_dict(mnemonic)

    def jump(self, mnemonic):
        return self.jump_dict(mnemonic)
