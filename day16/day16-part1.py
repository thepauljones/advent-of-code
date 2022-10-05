with open('test-data.dat') as file:
    data = [line.strip() for line in file][0]

def hex_to_binary(data):
    h_size = len(data) * 4
    return (bin(int(data, 16))[2:]).zfill(h_size)


def bin_to_decimal(binary):
    result = int(str(binary), 2)
    return result


def parse_literal_packet(data):
    LITERAL_PACKET_HEADER_LENGTH = 6
    pos = 0
    parts = []
    while(data[pos:pos+1] == '1'):
        curr = data[pos + 1:pos + 5]
        parts.append(curr)
        pos += 5

    curr = data[pos + 1:pos + 5]
    parts.append(curr)
    pos += 5

    result = ''.join(parts)

    answer = bin_to_decimal(result)

    return [pos + LITERAL_PACKET_HEADER_LENGTH, answer]

def parse_packet(packet):
    if len(packet) < 6:
        exit()

    ver = bin_to_decimal(packet[0:3])
    type = bin_to_decimal(packet[3:6])

    if (type == 4):
        [literal_packet_length, literal_packet_result] = parse_literal_packet(
            packet[6:])
        pos = literal_packet_length

        return pos, ver

    mode = packet[6:7]

    if mode == '0':
        length_of_bits = bin_to_decimal(packet[7:22])
        curr = 0
        sum_ver = ver
        while (curr < length_of_bits):
            pos, ver = parse_packet(packet[curr + 22:])
            curr += pos
            sum_ver += ver

        return 22 + length_of_bits, sum_ver

    else:
        num_sub_packets = bin_to_decimal(packet[7 :18])
        subs = 0
        total_pos = 0
        sum_ver = ver
        while (subs < num_sub_packets):
            pos, ver = parse_packet(packet[total_pos + 18:])
            total_pos += pos
            sum_ver += ver
            subs += 1

        return 18 + total_pos, sum_ver

pos, ver = parse_packet(hex_to_binary(data))
print(ver)

