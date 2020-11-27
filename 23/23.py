import string
from queue import Queue, Empty
from threading import Thread, Event, Lock
import time

mul_count = 0


class Computer(Thread):
    def __init__(self, program, pid, main_lock):
        super(Computer, self).__init__()
        self.registers = dict([(reg, 0) for reg in string.ascii_lowercase])
        self.registers['a']=1
        self.pid = pid
        self.registers['p'] = pid
        self.partner = None
        self.pc = 0
        self.program = program
        self.program_length = len(self.program)
        self.running = True
        self.message_q = Queue()
        self.waiting = Event()
        self.waiting.clear()
        # self.lock = Lock()
        self.send_count = 0
        self.lock = main_lock

    def connect(self, partner):
        self.partner = partner

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

    def sub(self, op1, op2):
        op1_val = self.__deref(op1)
        op2_val = self.__deref(op2)
        self.registers[op1] = op1_val - op2_val

    def set(self, op1, op2):
        op2 = self.__deref(op2)
        self.registers[op1] = op2

    def mul(self, op1, op2):
        global mul_count
        op1_val = self.__deref(op1)
        op2_val = self.__deref(op2)
        self.lock.acquire()
        mul_count += 1
        self.lock.release()
        self.registers[op1] = op1_val * op2_val

    def snd(self, op1):
        op1 = self.__deref(op1)
        self.partner.message(op1)
        self.send_count += 1
        # print(f'program id {self.pid} - send val {op1} - send count - {self.send_count}')

    def message(self, val):
        self.lock.acquire()
        # print(f"pid {self.partner.pid} - acquired send lock")
        # print(f"sending {val}")
        self.message_q.put(val)
        # print(f"pid {self.partner.pid} - releasing send lock")
        self.lock.release()

    def mod(self, op1, op2):
        op1_val = self.__deref(op1)
        op2_val = self.__deref(op2)
        self.registers[op1] = op1_val % op2_val

    def rcv(self, op1):
        try:
            self.lock.acquire()
            # print(f"pid {self.pid} - acquired rcv lock")
            self.registers[op1] = self.message_q.get(block=False)
            # print(f"pid {self.pid} - releasing rcv lock - first try")
            self.lock.release()

        except Empty:
            if self.partner.waiting.is_set() and self.partner.message_q.empty():
                # print(f"pid {self.pid} - releasing rcv lock - ending")
                self.lock.release()
                self.running = False
                self.partner.message(None)
                return
            self.waiting.set()
            # print(f"pid {self.pid} - releasing rcv lock - waiting")
            self.lock.release()
            self.registers[op1] = self.message_q.get()
            self.lock.acquire()
            self.waiting.clear()
            self.lock.release()
        finally:
            if self.registers[op1] is None:
                self.running = False
                return
        # print(f'program id {self.pid} - received val {self.registers[op1]}')

    def jgz(self, op1, offset):
        op1_val = self.__deref(op1)
        offset = self.__deref(offset)
        if op1_val > 0:
            self.pc += (offset - 1)
            if self.pc < 0 or self.pc >= self.program_length:
                self.running = False

    def jnz(self, op1, offset):
        op1_val = self.__deref(op1)
        offset = self.__deref(offset)
        if op1_val != 0:
            self.pc += (offset - 1)
            if self.pc < 0 or self.pc >= self.program_length:
                self.running = False

    def run(self):
        while self.running and 0 <= self.pc < self.program_length:
            instruction_to_execute = self.program[self.pc]
            self.__exec_single_line(instruction_to_execute)
        print(f'$$$program id {self.pid} - send count - {self.send_count}')


with open('input.txt') as file:
    instructions = []
    for line in file:
        instructions.append(line.strip().split(' '))
lock = Lock()
comp1 = Computer(instructions, 0, lock)
# comp2 = Computer(instructions, 1, lock)
# comp1.connect(comp2)
# comp2.connect(comp1)
comp1.start()
# comp2.start()
# comp2.join()
comp1.join()
print(mul_count)
print(comp1.registers['h'])