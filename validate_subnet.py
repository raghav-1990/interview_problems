
def validate_subnet_mask(subnet_mask:str):
    "method to validate if the given subnet mask is correct"
    octets = subnet_mask.split('.')
    binary_mask = ""

    if len(octets) != 4 or set(octets) == {'0'}:
        return False
    for octet in octets:
        binary_octet = bin(int(octet))[2:]
        binary_mask = binary_mask + binary_octet

    flag = False
    if binary_mask[0] == "0":
        flag = True
    
    for each in binary_mask[1:]:
        if each == "1" and flag:
            return False
        if each == "0":
            flag = True
    return True

subnet = "255.255.0.0"
if validate_subnet_mask(subnet):
    print(f"The given  subnet {subnet} is valid ")