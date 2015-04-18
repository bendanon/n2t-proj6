class SymbolTable:
    """
    Keeps a correspondence between symbolic
    labels and numeric addresses.
    """
    def __init__(self):

        self.table = {}

        for i in range(0, 16):
            self.table['R'+str(i)] = i

        self.table['SCREEN'] = 16384
        self.table['KBD'] = 24576
        self.table['SP'] = 0
        self.table['LCL'] = 1
        self.table['ARG'] = 2
        self.table['THIS'] = 3
        self.table['THAT'] = 4

    def addEntry(self, symbol, address):
        self.table[symbol] = address

    def contains(self, symbol):
        return symbol in self.table

    def GetAddress(self, symbol):
        return self.table[symbol]


def Test():
    st = SymbolTable()
    print st.contains('KBD')
    print st.GetAddress('ARG')
    st.addEntry('Ben', 80)
    print st.GetAddress('Ben')
