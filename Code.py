'''
Translates each field into its corresponding binary value,
and assembles the resulting values
'''


class Code:

    def __init__(self):
        self.jump_dict = {}
        self.comp_dict = {}
        self.dest_dict = {}

    def dest(self, mnemonic):
        return self.dest_dict.get(mnemonic)

    def comp(self, mnemonic):
        return self.comp_dict(mnemonic)

    def jump(self, mnemonic):
        return self.jump_dict(mnemonic)

