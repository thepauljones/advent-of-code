with open('test-data.dat') as file:
    data = [line.strip() for line in file][0]

total_version = 0

# This is a fucking pain, leading zeroes.
# In this case I prepend a '1' to the hex value
# and just strip it from the result again
# https://newbedev.com/converting-from-hex-to-binary-without-losing-leading-0-s-python
def hex_to_binary_string(hex_value):
    hex_base = 16
    result = ''.join(bin(int(c, hex_base))[2:].zfill(4) for c in hex_value)
    return result


def parse(packet):
    global total_version

    ver = int(packet[0:3], 2)
    pid = int(packet[3:6], 2)

    print(ver, pid)

    total_version += ver

    if pid == 4:
        literal_packet = packet[6:]
        num = ''
        if literal_packet[0] == '1':
            while literal_packet[0] == '1':
                literal_packet = literal_packet[1:]
                num += literal_packet[:4]
                literal_packet = literal_packet[4:]
                if not literal_packet[0] == '1':
                    num += literal_packet[1:5]
        else:
            num += literal_packet[1:5]

        return int(num, 2)
    else:
        if packet[6] == '0':
            length = int(packet[7:22], 2)
            return parse(packet[22:])



binary = hex_to_binary_string(data)
result = parse(binary)

print(result)
    


