import struct
import binascii
path="f.png"
#width 12:16 20:29
#height 12:20 24:29
m = open(path,"rb").read()
for i in range(1024*10):
    c = m[12:20] + struct.pack('>i', i) + m[24:29]
    crc = binascii.crc32(c) & 0xffffffff
    if crc == 0x36B4F5FD:
        print(hex(i))