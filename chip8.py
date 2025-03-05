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
        x = (opcode & 0x0F00) >> 8
        y = (opcode & 0x00F0) >> 4
        n = opcode & 0x000F
        nn = opcode & 0x00FF
        nnn = opcode & 0x0FFF

        if opcode == 0x00E0:  # CLS - Clear the screen
            self.display.fill(0)

        elif opcode == 0x00EE:  # RET - Return from subroutine
            self.PC = self.stack.pop()

        elif first_nibble == 0x1:  # JP addr - Jump to address NNN
            self.PC = nnn

        elif first_nibble == 0x2:  # CALL addr - Call subroutine at NNN
            self.stack.append(self.PC)
            self.PC = nnn

        elif first_nibble == 0x3:  # SE Vx, byte - Skip next if Vx == NN
            if self.V[x] == nn:
                self.PC += 2

        elif first_nibble == 0x4:  # SNE Vx, byte - Skip next if Vx != NN
            if self.V[x] != nn:
                self.PC += 2

        elif first_nibble == 0x5 and n == 0:  # SE Vx, Vy - Skip next if Vx == Vy
            if self.V[x] == self.V[y]:
                self.PC += 2

        elif first_nibble == 0x6:  # LD Vx, byte - Load NN into Vx
            self.V[x] = nn

        elif first_nibble == 0x7:  # ADD Vx, byte - Add NN to Vx
            self.V[x] = (self.V[x] + nn) & 0xFF  # Ensure it stays within 8 bits

        else:
            print(f"Unknown opcode: {opcode:04X}")


    def update_timers(self):
        if self.delay_timer > 0:
            self.delay_timer -= 1
        if self.sound_timer > 0:
            self.sound_timer -= 1
