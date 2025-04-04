# Buffer starting address

In GDB: 0xffffd05b 
Outside GDB: 0xffffd01b

# Buffer offset

Buffer is located at: `ebp - 0x6d`
Return address is at: `ebp + 0x4`

So,

Buffer offset from frame pointer = 0x6d = 109 bytes

Buffer offset to return address = 113 bytes

# # Return address

Return Address = 0xffffd0d0

Found via exp-shellcode.py

# First assembly instruction at return address

this will be the nop instruction due to the nop sled that appears at the start of the injected code.

