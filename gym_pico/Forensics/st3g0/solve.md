# St3g0 #
 
## Overview ##
 
Difficulty: Medium
 
## Description ##
 
Download this image and find the flag.

## Hint ##

1. We know the end sequence of the message will be $t3g0.

## Tool ##
zsteg
 
## Solution ##
I downloaded the image. Firstly I check with exiftool for any helpful metadata and found none. As the hint said, I tried to find the message in HexEd.it and found nothing. Then I google for "stenography tool" and I found zsteg to detect stegano-hidden data in PNG & BMP.
Github: https://github.com/zed-0xff/zsteg
I ran the command with -a as "try all known methods":    
```bash
zsteg -a pico.flag.png
```
Flag: picoCTF{7h3r3_15_n0_5p00n_a1062667}
