```md
# CHIP-8 Emulator  
A simple CHIP-8 emulator written in Python.  

## 📌 Features  
- ✅ **Memory & Registers**: Implements CHIP-8 memory model and 16 registers.  
- ✅ **Fetch-Decode-Execute Cycle**: Processes opcodes from ROMs.  
- ✅ **Graphics Support**: Renders a 64x32 display using `pygame`.  
- ✅ **Keyboard Input Handling**: Maps CHIP-8 keys to modern keyboards.  

## 🛠 Installation  
1. Clone the repository:  
   ```sh
   git clone https://github.com/your-username/chip8-emulator.git  
   cd chip8-emulator  
   ```  
2. Install dependencies:  
   ```sh
   pip install -r requirements.txt  
   ```  
3. Run the emulator:  
   ```sh
   python main.py roms/test.ch8  
   ```

## 🎮 Controls  
| CHIP-8 Key | Keyboard Key |  
|------------|-------------|  
| `1 2 3 C`  | `1 2 3 4`   |  
| `4 5 6 D`  | `Q W E R`   |  
| `7 8 9 E`  | `A S D F`   |  
| `A 0 B F`  | `Z X C V`   |  

## 📜 Roadmap  
- [ ] Implement opcode execution  
- [ ] Add sound support  
- [ ] Improve timing accuracy  
- [ ] Save/load state functionality  

## 🤝 Contributing  
Feel free to fork this repo and submit pull requests!  

