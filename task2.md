# Buffer starting address

In GDB: 0xffffd05b 
Outside GDB: 0xffffd01b

# Buffer offset

Buffer is located at: `ebp - 0x6d`
Return address is at: `ebp + 0x4`

So,

Buffer offset from frame pointer = 0x6d = 109 bytes

Buffer offset to return address = 113 bytes

# Return address

In GDB: 
return address = 0xffffd05b + 109 + 8 =  0xffffd0c0

Outside GDB: 
return address = 0xffffd01b + 109 + 8 = 0xffffd088

