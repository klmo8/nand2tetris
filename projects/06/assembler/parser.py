from hack_binary_translator import HackBinaryTranslator
from symbol_processor import SymbolProcessor
from instruction_type import InstructionType

class Parser():

    def __init__(self):
        self.hack_binary_translator = HackBinaryTranslator()
        self.symbol_processor = SymbolProcessor()
    
    def preprocess(self, file):
        self.linecount = 0
        with open(file, 'r') as reader:
            for line in reader:
                line = line.strip()
                if self.is_instruction(line):
                    instruction_type = InstructionType.get_instruction_type(line)
                    if instruction_type is InstructionType.L_INSTRUCTION:
                        SymbolProcessor.symbols[SymbolProcessor.get_symbol(line, instruction_type)] = self.linecount
                    else:
                        self.linecount += 1

    def process(self, path):
        with open(path, 'r') as reader, open(self.get_hack_filename(path), "w+") as writer:
            for line in reader:
                line = self.clean_line(line)
                if self.is_instruction(line):
                    instruction_type = InstructionType.get_instruction_type(line)
                    binary_code = "" 
                    if instruction_type is InstructionType.A_INSTRUCTION:
                        symbol = SymbolProcessor.get_symbol(line, instruction_type)
                        if not SymbolProcessor.symbol_exists(symbol):
                            self.symbol_processor.add_symbol_mapping(symbol)
                        address = SymbolProcessor.get_symbol_mapping(symbol)
                        binary_code = HackBinaryTranslator.convert_decimal_to_binary(address)
                    if instruction_type is InstructionType.C_INSTRUCTION:
                        instruction = Parser.tokenize(line)
                        binary_code = instruction.convert_to_binary_string()
                    if instruction_type is InstructionType.L_INSTRUCTION:
                        continue
                    
                    writer.write(binary_code + '\n')
    
    @staticmethod
    def clean_line(line):
        stripped_line = line.strip()
        part = stripped_line.split('//')[0]
        cleaned_line = ''.join(part.split())

        return cleaned_line
    
    @staticmethod
    def get_hack_filename(path):
        file_name = path.split('/')[-1]
        base_name = file_name.split('.')[0]

        return base_name + '1' + ".hack"
    
    @staticmethod
    def is_instruction(line):
        return line != '' and line[0] != ' ' and line[0] != '/' and line[0] != '\n'

    @staticmethod
    def tokenize(c_instruction):
        comp_and_jump_parts = c_instruction.split(';')
        dest_and_comp_parts = c_instruction.split('=')
        comp = ''
        dest = ''
        jump = ''

        if len(comp_and_jump_parts) > 1:
            comp = comp_and_jump_parts[0]
            jump = comp_and_jump_parts[1]
        elif len(dest_and_comp_parts) > 1:
            dest = dest_and_comp_parts[0]
            comp = dest_and_comp_parts[1]
 
        return Parser.CInstruction(comp, dest, jump)
        
    class CInstruction():
        
        def __init__(self, comp, dest, jump):
            self.comp = comp
            self.dest = dest
            self.jump = jump

        def convert_to_binary_string(self):
            string_parts = ["111", HackBinaryTranslator.get_op_code_bit(self.comp)]

            string_parts.append(HackBinaryTranslator.get_op_code(self.comp))
            string_parts.append(HackBinaryTranslator.get_destination_code(self.dest))
            string_parts.append(HackBinaryTranslator.get_jump_code(self.jump))

            return ''.join(string_parts)
