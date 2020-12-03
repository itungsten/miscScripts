import struct
import binascii
path="f.png"

m = open(path,"rb").read()
for i in range(1024):
    c = m[12:16] + struct.pack('>i', i) + m[20:29]
    crc = binascii.crc32(c) & 0xffffffff
    if crc == 0x932f8a6b:
        print(hex(i))