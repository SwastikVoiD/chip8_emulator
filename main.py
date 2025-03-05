import time
import sys
from chip8 import Chip8

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <ROM_FILE>")
        sys.exit(1)

    rom_path = sys.argv[1]

    chip8 = Chip8()
    chip8.load_rom(rom_path)

    # Main loop
    while True:
        chip8.emulate_cycle()
        chip8.update_timers()
        time.sleep(1 / 500)  # Control execution speed (adjust if needed)

if __name__ == "__main__":
    main()
