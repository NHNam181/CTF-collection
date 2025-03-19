# Bitlocker-1 #
 
## Overview ##
 
Score: 200
Category: Forensics
 
## Description ##  

Jacky is not very knowledgable about the best security passwords and used a simple password to encrypt their BitLocker drive. See if you can break through the encryption!  

## Hint ##  

- Hash cracking

## Tool ##
- bitcracker

## Solution ##
I was given a .dd file and it's encrypted with BitLocker. Looking online for any tools that can help decrypting, I found this: https://github.com/e-ago/bitcracker?tab=readme-ov-file  
Before starting the decryption, we need to extract the hash describing the image:  
```bash
└─$ ./bitcracker_hash -o hash -i ../../bitlocker-1.dd
```  
When the execution is complete, it produces 2 files: 
- hash_user_pass.txt: This will be used to crack the password.  
- hash_recv_pass.txt: This will be used to use Recovery Password attack mode.  
To unlock Jacky's drive, use the hash_user_pass.txt hash to crack the password with the rockyou wordlist:  
```bash
└─$ ./bitcracker_cuda -f ../../hash_user_pass.txt -d ../../rockyou.txt -t 1 -b 1 -g 0 -u
================================================
CUDA attack completed
Passwords evaluated: 1024
Password found: jacqueline
================================================
```
We found the password! It's **jacqueline**.  
Finally, mount the disk drive:  
```bash
└─$ sudo losetup -Pf bitlocker-1.dd 
```
And we got the flag!  
Flag: picoCTF{us3_b3tt3r_p4ssw0rd5_pl5!_3242adb1}  