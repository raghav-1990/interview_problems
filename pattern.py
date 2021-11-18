
import random
import string

#Sample pattern = "2*TTT"
#should print "TTTTTT"

def multiply_pattern(pattern:str):
    elements = pattern.split("*")
    return int(elements[0]) * elements[1]

def generate_random_patterns(num_of_patterns:int):
    for _ in range(num_of_patterns):
        string_length = random.randint(1,5)
        multiplying_digit = str(random.randint(1,9))
        char = random.choice(string.ascii_letters)
        pattern = multiplying_digit + "*" + string_length*char
        yield pattern

num_of_patterns = 20
for pattern in generate_random_patterns(num_of_patterns):
    print(multiply_pattern(pattern))
