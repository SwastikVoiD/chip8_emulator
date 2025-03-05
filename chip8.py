import numpy as np

class Chip8:
    def __init__(self):
        self.memory = np.zeros(4096, dtype=np.uint8)
        self.V = np.zeros(16, dtype=np.uint8)
        self.I = 0
        self.PC = 0x200
        self.stack = []
        self.SP = 0
        self.delay_timer = 0
        self.sound_timer = 0
        self.display = np.zeros((32, 64), dtype=np.uint8)
        self.keys = np.zeros(16, dtype=np.uint8)
        self.load_fontset()

    def load_fontset(self):
        fontset = [
            0xF0, 0x90, 0x90, 0x90, 0xF0,  # 0
            0x20, 0x60, 0x20, 0x20, 0x70,  # 1
            0xF0, 0x10, 0xF0, 0x80, 0xF0,  # 2
            0xF0, 0x10, 0xF0, 0x10, 0xF0,  # 3
            0x90, 0x90, 0xF0, 0x10, 0x10,  # 4
            0xF0, 0x80, 0xF0, 0x10, 0xF0,  # 5
            0xF0, 0x80, 0xF0, 0x90, 0xF0,  # 6
            0xF0, 0x10, 0x20, 0x40, 0x40,  # 7
            0xF0, 0x90, 0xF0, 0x90, 0xF0,  # 8
            0xF0, 0x90, 0xF0, 0x10, 0xF0,  # 9
            0xF0, 0x90, 0xF0, 0x90, 0x90,  # A
            0xE0, 0x90, 0xE0, 0x90, 0xE0,  # B
            0xF0, 0x80, 0x80, 0x80, 0xF0,  # C
            0xE0, 0x90, 0x90, 0x90, 0xE0,  # D
            0xF0, 0x80, 0xF0, 0x80, 0xF0,  # E
            0xF0, 0x80, 0xF0, 0x80, 0x80   # F
        ]
        self.memory[0x50:0x50 + len(fontset)] = fontset

    def load_rom(self, rom_path):
        with open(rom_path, "rb") as rom:
            rom_data = rom.read()
            self.memory[0x200:0x200 + len(rom_data)] = np.frombuffer(rom_data, dtype=np.uint8)

    def fetch_opcode(self):
        opcode = (self.memory[self.PC] << 8) | self.memory[self.PC + 1]
        self.PC += 2
        return opcode

    def emulate_cycle(self):
        opcode = self.fetch_opcode()
        print(f"Executing opcode: {opcode:04X}")
        self.decode_opcode(opcode)

def decode_opcode(self, opcode):
    """Decode and execute an opcode."""
    first_nibble = (opcode & 0xF000) >> 12
    addr = opcode & 0x0FFF
    vx = (opcode & 0x0F00) >> 8
    vy = (opcode & 0x00F0) >> 4
    byte = opcode & 0x00FF

    if opcode == 0x00E0:  # 00E0 - CLS (Clear screen)
        self.display.fill(0)
    elif opcode == 0x00EE:  # 00EE - RET (Return from subroutine)
        self.PC = self.stack.pop()
    elif first_nibble == 0x1:  # 1NNN - JP addr (Jump to address NNN)
        self.PC = addr
    elif first_nibble == 0x2:  # 2NNN - CALL addr (Call subroutine at NNN)
        self.stack.append(self.PC)
        self.PC = addr
    elif first_nibble == 0x3:  # 3XNN - SE Vx, NN (Skip next if Vx == NN)
        if self.V[vx] == byte:
            self.PC += 2
    elif first_nibble == 0x4:  # 4XNN - SNE Vx, NN (Skip next if Vx != NN)
        if self.V[vx] != byte:
            self.PC += 2
    elif first_nibble == 0x5 and (opcode & 0x000F) == 0x0:  # 5XY0 - SE Vx, Vy
        if self.V[vx] == self.V[vy]:
            self.PC += 2
    elif first_nibble == 0x6:  # 6XNN - LD Vx, NN (Set Vx = NN)
        self.V[vx] = byte
    elif first_nibble == 0x7:  # 7XNN - ADD Vx, NN (Set Vx = Vx + NN)
        self.V[vx] = (self.V[vx] + byte) & 0xFF
    else:
        print(f"Unknown opcode: {opcode:04X}")



    def update_timers(self):
        if self.delay_timer > 0:
            self.delay_timer -= 1
        if self.sound_timer > 0:
            self.sound_timer -= 1
