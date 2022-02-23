arr = [
    0x1234, 0xeeff, 0xabcd
]

array = []
for a in arr:
    array.extend([ a >> 8, a & 0xff])

# print(array)
# print(bytearray(array))
def to_hex_str(bytes_arr):
    return ':'.join(["{:02x}".format(i) for i in bytes_arr])

print(to_hex_str(bytes([1, 2, 3, 44])))