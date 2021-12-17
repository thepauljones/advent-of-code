with open('test-data.dat') as file:
    data = [line.strip() for line in file][0]

ParsedData = {}

total_version = 0

def hex_to_binary_string(hex_value):
    hex_scale = 16
    return bin(int(hex_value, hex_scale))[2:].zfill(4)

def get_version(binary, playhead):
    length = 3
    binary_version = binary[:length]
    return (int(binary_version, 2), playhead + length)

def get_packet_type_id(binary, playhead):
    length = 3
    binary_packet_type_id = binary[playhead:length + playhead]
    print('INVALID:', binary[playhead:length + playhead], '<- INVALID', binary_packet_type_id, playhead)
    print('total len', len(binary))
    print('total version', total_version)
    return (int(binary_packet_type_id, 2), min(len(binary), playhead + length))

def get_packet_value(binary, current_piece):
    current_piece = binary[:5]
    print(current_piece)

# ID: 4 - Packet type
def parse_literal_packet(binary_data, playhead):
    groups = []
    loops = 0
    group_size = 5

    # if a group of 1s and 0s starts with a 1, it continues to the
    # next group, a 0 means this is the last one
    while binary_data[playhead + (group_size * loops)] == '1':
        # Add in the last four of each group of five to the current group
        groups.append(binary_data[loops * group_size + 1: loops * group_size + group_size])
        loops += 1

    # Add last one
    groups.append(binary_data[loops * group_size + 1:loops * group_size + group_size])
    # Return the decimal value of the found binary value
    return (int(''.join(groups), 2), playhead + (loops * group_size))

def get_length_subpacket(binary_data, playhead):
    length = 15
    return (int(binary_data[playhead: playhead + length], 2), playhead + length)

def get_num_sub_packets(binary_data, playhead):
    length = 11
    return (int(binary_data[playhead: playhead + length], 2), playhead + length)

def get_operator_packet_length_type_id(binary_data, playhead):
    return (binary_data[playhead], playhead + 1)

def parse_operator_packet(binary_data, playhead):
    version, playhead = get_version(binary_data, playhead)
    packet_type_id, playhead = get_packet_type_id(binary_data, playhead)

    length_type_id, playhead = get_operator_packet_length_type_id(binary_data, playhead)
    
    if length_type_id == 0:
        length_subpacket, playhead = get_length_subpacket(binary_data, playhead)
        playhead = parse_packet(binary_data, playhead)

    if length_type_id == 1:
        num_subpackets, playhead = get_num_sub_packets(binary_data, playhead)
        for i in range(0, num_subpackets):
            playhead = parse_packet(binary_data, playhead)

    return playhead

def parse_packet(binary_data, playhead):
    global total_version

    version, playhead = get_version(binary_data, playhead)
    packet_type_id, playhead = get_packet_type_id(binary_data, playhead)

    total_version = total_version + version

    if packet_type_id == 4:
        literal_packet_data, playhead = parse_literal_packet(binary_data, playhead)

    print('Version: ', version, 'ID: ', packet_type_id, 'Playhead: ', playhead)
    return playhead

def parse_message(hex_string):
    binary_data = hex_to_binary_string(hex_string)

    playhead = 0
    while playhead < len(binary_data):
        playhead = parse_packet(binary_data, playhead)

    print('TOTAL', total_version)

parse_message(data)

# binary_data = hex_to_binary_string(data)
# message_binary = binary_data[6:]
# version = get_version(binary_data)
# packet_type_id = get_packet_type_id(binary_data)
# 
# 
# 
# print('Message Binary:', message_binary)
# print('------------')
# print('Binary: ', binary_data)
# print('Version: ', version)
# print('Packet type id:', packet_type_id)
# 
# print('Literal value in message', parse_literal_packet(message_binary))
