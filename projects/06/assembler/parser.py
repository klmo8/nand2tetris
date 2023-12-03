from hack_binary_translator import HackBinaryTranslator
from symbols import Symbols
from instruction_type import InstructionType
import pprint

class Parser():

    def __init__(self):
        self._linecount = 0
        self.hack_binary_translator = HackBinaryTranslator()
        self.symbols = Symbols()
    
    def preprocess(self, file):
        with open(file, 'r') as reader:
            for line in reader:
                line = line.strip()
                print("AFTER STRIP")
                print(line)
                if self.is_instruction(line):
                    instruction_type = InstructionType.get_instruction_type(line)
                    if instruction_type is InstructionType.L_INSTRUCTION:
                        print("SETTING SYMBOLS MAP with symbol: " + Symbols.get_symbol(line, instruction_type))
                        self.symbols.symbols[Symbols.get_symbol(line, instruction_type)] = self._linecount
                    elif instruction_type is InstructionType.A_INSTRUCTION or instruction_type is InstructionType.C_INSTRUCTION:
                        print("INCREMENTING LINE COUNT")
                        self._linecount += 1
                    print("Current line count is: " + str(self._linecount))
        
        print("PRINTING SYMBOLS: ")
        pprint.pprint(self.symbols.symbols)

    def process(self, path):
        with open(path, 'r') as reader, open(self.get_hack_filename(path), "w+") as writer:
            for line in reader:
                print("--DEBUG--")
                print(line)
                print("IT'S AN INSTRUCTION...")
                line = self.clean_line(line)
                if self.is_instruction(line):
                    instruction_type = InstructionType.get_instruction_type(line)
                    binary_code = "" 
                    if instruction_type is InstructionType.A_INSTRUCTION:
                        symbol = Symbols.get_symbol(line, instruction_type)
                        if not self.symbols.symbol_exists(symbol):
                            self.symbols.add_symbol_mapping(symbol)
                        address = self.symbols.get_symbol_mapping(symbol)
                        binary_code = HackBinaryTranslator.convert_decimal_to_binary(address)
                    if instruction_type is InstructionType.C_INSTRUCTION:
                        instruction = self.tokenize(line)
                        print("C INSTRUCTION IS: " + instruction.op_code + " " + instruction.comp + " " + instruction.dest + " " + instruction.jump)
                        binary_code = instruction.convert_to_binary_string()
                    if instruction_type is InstructionType.L_INSTRUCTION:
                        pass
                    
                    print("INSTRUCTION IS: " + binary_code)
                    if binary_code != "":
                        self._linecount += 1
                        writer.write(binary_code + '\n')

        print("Finished parsing file")
    
    def clean_line(self, line):
        stripped_line = line.strip()

        # Split the string at '//' and take the part before it
        part = stripped_line.split('//')[0]

        # Remove all remaining whitespaces
        cleaned = ''.join(part.split())

        return cleaned
    
    def get_hack_filename(self, path):
        file_name = path.split('/')[-1]
        base_name = file_name.split('.')[0]

        print("PRINTING PATH: ")
        print(base_name + ".hack")

        return base_name + ".hack"
    
    def is_instruction(self, line):
        return line != '' and line[0] != ' ' and line[0] != '/' and line[0] != '\n'

    def should_increment_linecount(self, instruction_type):
        return instruction_type in [InstructionType.A_INSTRUCTION, InstructionType.C_INSTRUCTION]

    def tokenize(self, c_instruction):
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
        
        # TODO: this should probably be moved inside of CInstruction conversion method..
        op_code = HackBinaryTranslator.get_op_code_bit(comp)
 
        return Parser.CInstruction(op_code, comp, dest, jump)
        
    class CInstruction():
        
        def __init__(self, op_code, comp, dest, jump):
            self.op_code = op_code
            self.comp = None if comp is None else comp
            self.dest = None if dest is None else dest
            self.jump = jump if jump is None else jump

        def convert_to_binary_string(self):
            print("INSIDE CONVERSION FUNCTION")
            print(self.op_code)
            print(self.comp)
            print(self.dest)
            print(self.jump)
            string_parts = ["111", self.op_code]

            string_parts.append(HackBinaryTranslator.get_op_code(self.comp))
            string_parts.append(HackBinaryTranslator.get_destination_code(self.dest))
            string_parts.append(HackBinaryTranslator.get_jump_code(self.jump))

            print(string_parts)

            return ''.join(string_parts)



    