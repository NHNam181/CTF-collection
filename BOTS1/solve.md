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
```text
|metadata index="botsv1" type=sourcetypes 
| stats values(sourcetype)
```
Here we have the result:  
<p align="center">
  <img src="image/image.png" alt="Cool" width="50%" />
</p>


From the sourcetype, let’s start with the Fortigate firewall:  
```text
index="botsv1" sourcetype=fgt_* imreallynotbatman.com 
|table src_ip dst_ip
|stats count by src_ip dst_ip
```  
This query will find activities where the domain **imreallynotbatman** appears:  
![Cool](image/image1.png)   
**Answer: 40.80.148.42**  

2. What company created the web vulnerability scanner used by Po1s0n1vy? Type the company name.  
Follow the 40.80.148.42 IP, view the attack event and we can find the vuln scanner:   
![Cool](image/Picture2.png)  
**Answer: Acunetix**  

3. What content management system is imreallynotbatman.com likely using?  
Look at the event table and the CMS should be there:  
![Cool](image/Picture3.png)  
**Answer: joomla**  

4. What is the name of the file that defaced the imreallynotbatman.com website? Please submit only the name of the file with extension.  
Defacing means the image or graffiti that ruins the surface of something. Maybe an image extension can help in this situation. Since we already know the Web Server IP is **192.168.250.70**. Let’s dive more into this IP:
```text
index="botsv1" sourcetype="stream:http" "192.168.250.70"
| search uri=*
| where like(uri, "%.jpg") OR like(uri, "%.jpeg")
| table _time src_ip dst_ip uri
```



