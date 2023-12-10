from enum import Enum

class InstructionType(Enum):
    A_INSTRUCTION = 0
    C_INSTRUCTION = 1
    L_INSTRUCTION = 2

    @staticmethod
    def get_instruction_type(instruction):
        first_char = instruction[0]
        if first_char == '@':
            return InstructionType.A_INSTRUCTION
        elif first_char == '(':
            return InstructionType.L_INSTRUCTION
        else:
            return InstructionType.C_INSTRUCTION