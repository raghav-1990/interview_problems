import random 

probable_subnet_values = [128, 192, 224, 255, 240, 0, 248, 252, 254]

def generate_n_subnet(valid_numbers, n):
    "method to generate N number of subnet masks from a list of given integers"
    s = ''
    for _ in range(n+1):
        for i in range(4):
            if i == 0:
                s = str(random.choice(valid_numbers))
            else:
                s = s + '.' +  str(random.choice(valid_numbers))
        yield s

def validate_subnet_mask(subnet_mask:str):
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
    print(binary_mask)
    return True

#generate 10000 probable subnet masks
n = 10000
for subnet in generate_n_subnet(probable_subnet_values, n):
    if validate_subnet_mask(subnet):
        print(f"The subnet {subnet} is valid")

