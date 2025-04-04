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

to find the return address, I go to the ret instruction inside process_comment and see which address is popped into the eip instruction upon its execution, which will be the address of the shellcode.

(gdb) disas process_comment
Dump of assembler code for function process_comment:
   0x08049838 <+0>:     push   %ebp
   0x08049839 <+1>:     mov    %esp,%ebp
   0x0804983b <+3>:     push   %ebx
   0x0804983c <+4>:     sub    $0x74,%esp
   0x0804983f <+7>:     call   0x8049680 <__x86.get_pc_thunk.bx>
   0x08049844 <+12>:    add    $0xc37bc,%ebx
   0x0804984a <+18>:    lea    0x132f(%ebx),%eax
   0x08049850 <+24>:    mov    %eax,0x2330(%ebx)
   0x08049856 <+30>:    sub    $0x8,%esp
   0x08049859 <+33>:    lea    -0x6d(%ebp),%eax
   0x0804985c <+36>:    push   %eax
   0x0804985d <+37>:    lea    -0x37fb9(%ebx),%eax
   0x08049863 <+43>:    push   %eax
   0x08049864 <+44>:    call   0x8052180 <printf>
   0x08049869 <+49>:    add    $0x10,%esp
   0x0804986c <+52>:    mov    0x2330(%ebx),%eax
   0x08049872 <+58>:    sub    $0x8,%esp
   0x08049875 <+61>:    push   %eax
   0x08049876 <+62>:    lea    -0x6d(%ebp),%eax
   0x08049879 <+65>:    push   %eax
   0x0804987a <+66>:    call   0x8049028
   0x0804987f <+71>:    add    $0x10,%esp
   0x08049882 <+74>:    nop
   0x08049883 <+75>:    mov    -0x4(%ebp),%ebx
=> 0x08049886 <+78>:    leave
   0x08049887 <+79>:    ret

From the disassembled process_comment, we see the current step at just before ret.

I perform the command: x/wx $esp:

0xffffd050:     0x08113f40

This is the value about to be popped into eip.

Next, I step into the ret instruction by: si



# First assembly instruction at return address

T

