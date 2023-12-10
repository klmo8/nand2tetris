class HackBinaryTranslator():

    _op_code_0_set = ('0', '1', '-1', 'D', 'A', '!D', '!A', 'D+1', 'A+1', 'D-1', 'A-1', 'D+A', 'D-A', 'A-D', 'D&A', 'D|A')
    _op_code_1_set = ('M', '!M', '-M', 'M+1', 'M-1', 'D+M', 'D-M', 'M-D', 'D&M', 'D|M')

    _op_code_map = {
        '0' : '101010',
        '1' : '111111',
        '-1': '111010',
        'D' : '001100',
        'A' : '110000',
        'M' : '110000',
        '!D': '001101',
        '!A': '110001',
        '!M': '110001',
        '-D': '001111',
        '-A' : '110011',
        '-M' : '110011',
        'D+1' : '011111',
        'A+1': '110111',
        'M+1': '110111',
        'D-1': '001110',
        'A-1': '110010',
        'M-1' : '110010',
        'D+A' : '000010',
        'D+M' : '000010',
        'D-A' : '010011',
        'D-M' : '010011',
        'A-D': '000111',
        'M-D': '000111',
        'D&A' : '000000',
        'D&M' : '000000',
        'D|A' : '010101',
        'D|M' : '010101'
    }

    _destination_map = {
        '' : '000',
        'M': '001',
        'D': '010',
        'DM': '011',
        'MD': '011',
        'A': '100',
        'AM': '101',
        'MA': '101',
        'AD': '110',
        'DA': '110',
        'ADM': '111',
        'DAM': '111',
        'DMA': '111',
        'MDA': '111',
        'MAD': '111',
        'AMD': '111',
    }

    _jump_map = {
        '': '000',
        'JGT': '001',
        'JEQ': '010',
        'JGE': '011',
        'JLT': '100',
        'JNE': '101',
        'JLE': '110',
        'JMP': '111'
    }

    @staticmethod
    def convert_decimal_to_binary(instruction):
        decimal_number = int(instruction)  # Convert string to integer
        binary_string = format(decimal_number, '016b')   # Convert integer to binary string
        return binary_string
    
    @staticmethod
    def get_op_code_bit(comp):
        return '0' if comp in HackBinaryTranslator._op_code_0_set else '1'
    
    @staticmethod
    def get_jump_code(jump):
        return HackBinaryTranslator._jump_map[jump]
    
    @staticmethod
    def get_destination_code(jump):
        return HackBinaryTranslator._destination_map[jump]
    
    @staticmethod
    def get_op_code(comp):
        return HackBinaryTranslator._op_code_map[comp]