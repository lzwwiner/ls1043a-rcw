#!/usr/bin/env python
"""
Swap the 4/8 bytes endian except for PBI CRC
2016-10-9: Initial version

Usage:
	./byte_swap.py <file_name> <byte>
"""
import sys

try:
    file_name = sys.argv[1]
    byte = int(sys.argv[2])
except:
    print("Usage: ./byte_swap.py <file_name> <byte>")
    print("E.g.: ./byte_swap.py rcw_1600.bin 8\n")
    exit

with open(file_name,'rb') as file:
    tmp = file.read()
file.close()

with open(file_name + '.swapped','wb') as file:
    for i in range(0, len(tmp) - 1, byte):
	if(tmp[i:i+4].encode('hex')) == "08610040":
	    #print("PBI CRC command")
	    file.write(tmp[i:i+8])
	    break
	file.write(tmp[i:i+byte][::-1])
file.close()

print("Swapped file: " + file_name + '.swapped')
