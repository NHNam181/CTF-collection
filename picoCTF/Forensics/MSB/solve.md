# MSB #
 
## Overview ##
 
Difficulty: Medium
 
## Description ##
 
This image passes LSB statistical analysis, but we can't help but think there must be something to the visual artifacts present in this image...

## Hint ##

1. What's causing the 'corruption' of the image?

## Tool ##
sigBits.py - Online python file for significant bits image decoder
 
## Solution ##
 
As the description and hint said, I look online for "lsb msb tool". Luckily I found this: https://github.com/Pulho/sigBits.git
All I need to do is to run the python file:
```bash
    $ python3 sigBits.py -t=msb Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png
```    
As the output is a text file, grep the content and the flag should be there.
Flag: picoCTF{15_y0ur_que57_qu1x071c_0r_h3r01c_ee3cb4d8}