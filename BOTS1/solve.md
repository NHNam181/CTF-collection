# Boss of the SOC Version 1 (2015) #
 
## Overview ##
Blue Team Lab. Really enjoyed.
 
## Description ##  

Today is Alice's first day at the Wayne Enterprises' Security Operations Center. Lucius sits Alice down and gives her first assignment: A memo from Gotham City Police Department (GCPD). Apparently GCPD has found evidence online (http://pastebin.com/Gw6dWjS9) that the website www.imreallynotbatman.com hosted on Wayne Enterprises' IP address space has been compromised. The group has multiple objectives... but a key aspect of their modus operandi is to deface websites in order to embarrass their victim. Lucius has asked Alice to determine if www.imreallynotbatman.com. (the personal blog of Wayne Corporations CEO) was really compromised.

## Hint ##  
- Some. I don't really remember XD

## Tool ##
- Splunk
- VirusTotal

## Solution ##
1. What is the likely IPv4 address of someone from the Po1s0n1vy group scanning imreallynotbatman.com for web application vulnerabilities?  
Let’s see what type of data that we can start with:
```bash
|metadata index="botsv1" type=sourcetypes 
| stats values(sourcetype)
```
Here we have the result:  
<div style="text-align: center;">
  <img src="image/image.png" alt="Cool" style="width: 50%;" />
</div>

From the sourcetype, let’s start with the Fortigate firewall:  
```bash
index="botsv1" sourcetype=fgt_* imreallynotbatman.com 
|table src_ip dst_ip
|stats count by src_ip dst_ip
```  




