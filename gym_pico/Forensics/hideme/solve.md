# hideme #
 
## Overview ##
 
Difficulty: Medium
 
## Description ##
 
How about some hide and seek heh? Download this file and find the flag.

## Hint ##

None

## Tool ##
binwalk
 
## Solution ##
At first I thought the flag would be hidden the same so I tried zsteg and found nothing. Another tool that may help is Binwalk.
This tool is for searching binary files like images and audio files for embedded files and data. It can be installed with apt
I used the command:
```bash
binwalk -e flag.png
```
When the extraction is complete, the flag is found in the new folder.
Flag: picoCTF{Hiddinng_An_imag3_within_@n_ima9e_ad9f6587}