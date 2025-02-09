# Keeper_Finder #
 
## Overview ##
 
Score:
 
## Description ##
 
Given a weird image.

## Hint ##

None

## Tool ##
Foremost
Steghide
 
## Solution ##
I was given an image. I used foremost to extract the hidden files within the image:
```bash
$ foremost -i file
```
Check the output folder, I have three folders: jpg, png and wav.  
The jpg picture:  
![JPG picture](extracted_data/00000144.jpg)

```bash
binwalk -e flag.png
```
When the extraction is complete, the flag is found in the new folder.
Flag: picoCTF{Hiddinng_An_imag3_within_@n_ima9e_ad9f6587}