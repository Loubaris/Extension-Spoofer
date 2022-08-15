<p align="center"><img src="https://media.discordapp.net/attachments/1007581332727148615/1008769366420115538/extension-de-fichier.png" style="text-align: center" width="150px" height="150px"></p>

<h3 align="center">ExtSpoof</h3>

<br>
<p align="center">ExtSpoof is a framework that let you spoof your payloads<br>extensions into anothers using differents methods</p>


```python

Modules needed: subprocess, base64
Usage: python extspoof.py

#Example running extspoof.py
Method 1: Right To Left Spoofing
(ExtSpoof)>rlt <filename|payload> <new_extension>
Ex:
(ExtSpoof)>rlt stealer.exe jpg

Method 2: Python In-File Spoofing
(ExtSpoof)>ctm <filename|payload.py> <fake_file_to_open.pdf|png|etc>
Ex:
(ExtSpoof)>ctm chromestealer.py homework.pdf

#Example importing ExtSpoof
from extspoof import rlt

rlt("rlt <filename|payload> <new_extension>")
Ex:
rlt("rlt stealer.exe png")

```
