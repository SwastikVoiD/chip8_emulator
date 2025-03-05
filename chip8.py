class Chip8:
    def __init__(self):
        # CHIP-8 has 4KB memory
        self.memory = [0] * 4096
        
        # 16 general-purpose 8-bit registers (V0 - VF)
        self.V = [0] * 16
        
        # Index register and program counter
        self.I = 0
        self.pc = 0x200  # Programs start at 0x200
        
        # Stack and stack pointer
        self.stack = []
        
        # Display (64x32 pixels)
        self.display = [[0] * 64 for _ in range(32)]
        
        # Keyboard input (16 keys)
        self.keys = [0] * 16
        
        # Timers
        self.delay_timer = 0
        self.sound_timer = 0

    def load_rom(self, rom_path):
        with open(rom_path, "rb") as f:
            rom_data = f.read()
            for i, byte in enumerate(rom_data):
                self.memory[0x200 + i] = byte

    def cycle(self):
        """Fetch-Decode-Execute Cycle"""
        opcode = (self.memory[self.pc] << 8) | self.memory[self.pc + 1]
        print(f"Executing opcode: {opcode:04X}")
        self.pc += 2  # Move to next instruction (most instructions are 2 bytes)

if __name__ == "__main__":
    chip8 = Chip8()
    chip8.load_rom("roms/test.ch8")  # Load a test ROM
    while True:
        chip8.cycle()  # Run emulation cycle
