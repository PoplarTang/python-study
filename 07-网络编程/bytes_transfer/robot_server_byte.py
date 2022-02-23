import binascii
import socket
import struct
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 10000)
sock.bind(server_address)
sock.listen(1)

packer_head = struct.Struct('>B')
while True:
    # print >> sys.stderr, '\nwaiting for a connection'
    sys.stderr.write('waiting for a connection\n')
    connection, client_address = sock.accept()
    try:
        while True:
            # unpacker = struct.Struct('I f f f f f f')
            # data = connection.recv(unpacker.size)
            # sys.stderr.write('received "%s"' % binascii.hexlify(data) + "\n")
            # unpacked_data = unpacker.unpack(data)
            # sys.stderr.write('unpacked:{}\n'.format(unpacked_data))

            data = connection.recv(1)
            head_unpack = packer_head.unpack(data)
            sys.stderr.write(f"received {data} - ascii {binascii.hexlify(data)} - head_unpack {head_unpack}\n")
            if 1 == head_unpack[0]:
                # print >> sys.stderr, 'received "%s"' % binascii.hexlify(data)
                unpacker = struct.Struct('>f f f f f f')
                data1 = connection.recv(unpacker.size)
                unpacked_data = unpacker.unpack(data1)
                sys.stderr.write('unpacked:{} \n'.format(unpacked_data))
            elif 3 == head_unpack[0]:
                unpacker = struct.Struct('>I I')
                data1 = connection.recv(unpacker.size)
                unpacked_data = unpacker.unpack(data1)
                sys.stderr.write('unpacked:{} \n'.format(unpacked_data))
    except Exception as e:
        print(e)