import binascii
import socket
import struct
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 10000)
sock.connect(server_address)

try:
    values = (1, 0, 3, 0, 0, 90, 2)
    packer = struct.Struct('>B f f f f f f')
    packed_data = packer.pack(*values)
    # print(type(binascii.hexlify(packed_data)))
    print(f"packer1.size: {packer.size} data.len: {len(packed_data)}")
    # Send data
    # print >> sys.stderr, 'sending "%s"' % binascii.hexlify(packed_data), values
    sys.stderr.write('sending1 "%s"\n' % binascii.hexlify(packed_data))
    sock.sendall(packed_data)

    # ----------------------------------
    values = (3, 96, 37)
    packer = struct.Struct('>B I I')
    packed_data = packer.pack(*values)
    print(f"packer2.size: {packer.size} data.len: {len(packed_data)}")
    # Send data
    sys.stderr.write('sending2 "%s"\n' % binascii.hexlify(packed_data))
    sock.sendall(packed_data)
finally:
    # print >> sys.stderr, 'closing socket'
    sys.stderr.write('closing socket\n')
    sock.close()