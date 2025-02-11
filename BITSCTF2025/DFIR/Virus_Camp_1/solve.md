# Virus Camp 1 #
 
## Overview ##
 
Score: 212
 
## Description ##
 
Alice was just hired as a junior dev and she is absolutely obsessed with light themes. While customizing her work laptop she suddenly found out that their top secret flag was encrypted. Can you figure out how this happened and unconver a few flags in the process?

## Hint ##
None

## Tool ##
FTK Imager
 
## Solution ##
I was given a .ad1 file. Mounted it with FTK Imager and I had folders which are often saved in the C disk. Looking around I found flag.enc in Desktop. The file is encrypted so what I must do now is to find the key to decrypt this. In all of the folders, the .vscode stood out the most.  
Lookinginto the extension.js, I have this base64 encoded. Decrypt it and we have the flag:
```bash
echo VGhlIDFzdCBmbGFnIGlzOiBCSVRTQ1RGe0gwd19jNG5fdlNfYzBkM19sM3RfeTB1X3B1Ymwxc2hfbTRsMWNpb3VzX2V4NzNuc2kwbnNfU09fZWFzaWx5Pz9fNWE3YjMzNmN9 | base64 --decode
```  
Flag: BITSCTF{H0w_c4n_vS_c0d3_l3t_y0u_publ1sh_m4l1cious_ex73nsi0ns_SO_easily??_5a7b336c}