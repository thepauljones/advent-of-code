with open('test-data.dat') as file:
    data = [line.strip() for line in file][0]

def hex_to_binary_string(hex_value):
    hex_scale = 16
    return bin(int(hex_value, hex_scale))[2:].zfill(4)

def get_version(binary):
    binary_version = binary[:3]
    return int(binary_version, 2)


def get_packet_type_id(binary):
    binary_packet_type_id = binary[3:6]
    return int(binary_packet_type_id, 2)

def get_packet_value(binary):
    current_piece = binary[:5]
    print(current_piece)

binary_data = hex_to_binary_string(data)
message_binary = binary_data[6:]
print('Message Binary:', message_binary)
version = get_version(binary_data)
packet_type_id = get_packet_type_id(binary_data)

print('Binary: ', binary_data)

print('Version: ', version)

print('Packet type id:', packet_type_id)

