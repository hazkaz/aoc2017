import string


class Computer:
    def __init__(self, program):
        self.registers = dict([(reg, 0) for reg in string.ascii_lowercase])
        self.pc = 0
        self.program = program
        self.program_length = len(self.program)
        self.running = True
        self.last_played = None

    def __deref(self, operand):
        if operand[0] in string.ascii_lowercase:
            return self.registers[operand]
        else:
            return int(operand)

    @staticmethod
    def __preprocess(inst):
        return list(map(str.lower, inst))

    def __perform_instruction(self, inst):
        operation = Computer.__dict__[inst[0]].__get__(self)
        op1 = inst[1]
        if len(inst) > 2:
            op2 = inst[2]
            operation(op1, op2)
            return
        operation(op1)

    def __exec_single_line(self, instruction):
        self.pc += 1
        instruction = self.__preprocess(instruction)
        self.__perform_instruction(instruction)

    def add(self, op1, op2):
        op1_val = self.__deref(op1)
        op2_val = self.__deref(op2)
        self.registers[op1] = op1_val + op2_val

    def set(self, op1, op2):
        op2 = self.__deref(op2)
        self.registers[op1] = op2

    def mul(self, op1, op2):
        op1_val = self.__deref(op1)
        op2_val = self.__deref(op2)
        self.registers[op1] = op1_val * op2_val

    def snd(self, op1):
        op1 = self.__deref(op1)
        self.last_played = op1

    def mod(self, op1, op2):
        op1_val = self.__deref(op1)
        op2_val = self.__deref(op2)
        self.registers[op1] = op1_val % op2_val

    def rcv(self, op1):
        self.registers[op1] = self.last_played

    def jgz(self, op1, offset):
        op1_val = self.__deref(op1)
        offset = self.__deref(offset)
        if op1_val > 0:
            self.pc += (offset - 1)
            if self.pc < 0 or self.pc >= self.program_length:
                self.running = False

    def exec(self):
        while self.running and 0 <= self.pc < self.program_length:
            instruction_to_execute = self.program[self.pc]
            if instruction_to_execute[0] == 'rcv' and self.__deref(instruction_to_execute[1]) != 0:
                print(self.last_played)
                break
            self.__exec_single_line(instruction_to_execute)


with open('input.txt') as file:
    instructions = []
    for line in file:
        instructions.append(line.strip().split(' '))

comp = Computer(instructions)
comp.exec()
