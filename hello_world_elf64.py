import struct
import os

BASE_ADDR = 0x400000
ENTRY_OFFSET = 0x80
ENTRY_VADDR = BASE_ADDR + ENTRY_OFFSET

def build_elf():
    msg = b"Hello, budi!\n"
    msg_len = len(msg)

    # Machine code (45 bytes)
    code = b''.join([
        b'\x48\xc7\xc0\x01\x00\x00\x00',                # mov rax, 1 (sys_write)
        b'\x48\xc7\xc7\x01\x00\x00\x00',                # mov rdi, 1 (stdout)
        b'\x48\xbe' + struct.pack('<Q', ENTRY_VADDR + 45),  # mov rsi, addr msg (after code)
        b'\x48\xc7\xc2' + struct.pack('<I', msg_len),   # mov rdx, len
        b'\x0f\x05',                                    # syscall
        b'\x48\xc7\xc0\x3c\x00\x00\x00',                # mov rax, 60 (exit)
        b'\x48\x31\xff',                                # xor rdi, rdi
        b'\x0f\x05'                                     # syscall
    ])

    full_code = code + msg
    code_size = len(full_code)

    elf = b''

    # ELF Header (64 bytes)
    elf += b'\x7fELF'                                   # Magic
    elf += b'\x02'                                      # 64-bit
    elf += b'\x01'                                      # Little endian
    elf += b'\x01'                                      # ELF version
    elf += b'\x00' * 9                                  # OS/ABI + ABI version + padding
    elf += struct.pack('<H', 2)                         # Executable type
    elf += struct.pack('<H', 0x3e)                      # x86_64 machine
    elf += struct.pack('<I', 1)                         # ELF version
    elf += struct.pack('<Q', ENTRY_VADDR)               # Entry point
    elf += struct.pack('<Q', 64)                        # Program header offset
    elf += struct.pack('<Q', 0)                         # Section header offset
    elf += struct.pack('<I', 0)                         # Flags
    elf += struct.pack('<H', 64)                        # ELF header size
    elf += struct.pack('<H', 56)                        # Program header size
    elf += struct.pack('<H', 1)                         # Number of program headers
    elf += struct.pack('<H', 0)                         # Section header size (unused)
    elf += struct.pack('<H', 0)                         # Number of section headers
    elf += struct.pack('<H', 0)                         # Section header string index

    # Program Header (56 bytes)
    file_size = ENTRY_OFFSET + code_size
    elf += struct.pack('<I', 1)                         # PT_LOAD
    elf += struct.pack('<I', 5)                         # RX flags
    elf += struct.pack('<Q', 0)                         # Offset in file
    elf += struct.pack('<Q', BASE_ADDR)                 # Virtual address
    elf += struct.pack('<Q', BASE_ADDR)                 # Physical address
    elf += struct.pack('<Q', file_size)                 # File size
    elf += struct.pack('<Q', file_size)                 # Memory size
    elf += struct.pack('<Q', 0x1000)                    # Alignment

    # Pad to entry point offset
    elf += b'\x00' * (ENTRY_OFFSET - len(elf))

    # Append code and message
    elf += full_code

    return elf

def save_executable(filename:str="hello_world_x86"):
    with open(f"./{filename}", "wb") as f:
        f.write(build_elf())
    os.chmod(filename, 0o755)
    print(f"ELF file created: ./{filename}")

if __name__ == "__main__":
    save_executable()
