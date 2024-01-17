import sys
sys.set_int_max_str_digits(999999999)

def binary_viewer_for_ints(number):
    binary_representation = bin(number)[2:]  # Convert the number to binary and remove the '0b' prefix
    return binary_representation

# Example usage:
number = 2**8191-1
binary_representation = binary_viewer_for_ints(number)
print(f"The binary representation of {number} \n \nis: \n{binary_representation}")

def utf8_to_binary(text):
    binary_representation = ''
    # Encode the text to UTF-8
    utf8_encoded_text = text.encode('utf-8')
    
    # Convert each byte to its binary representation
    for byte in utf8_encoded_text:
        binary_representation += format(byte, '08b') + ' ' # 08b for 8-bit binary

    return binary_representation.strip()

cyndaquils = ["Samantha Briasco-Stewart", "Cyndaquil", "weewow", "Samantha"]
#cyndaquil = "Samantha Briasco-Stewart"
for cyndaquil in cyndaquils:
    binary_cyndaquil = utf8_to_binary(cyndaquil)
    print(f"\nThe length of {cyndaquil} is {len(cyndaquil)} and {cyndaquil} in UTF-8 in binary is", binary_cyndaquil)

print("\n")

def view_binary_file(file_path):
    try:
        with open(file_path, 'rb') as file:
            while True:
                byte = file.read(1)
                if not byte:
                    break
                print("WTH is this", byte, end='  🤔 🤔 🤔 😘   ')
                print("This encoding on this line in hex is", byte.hex(), end='\n')
                
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def write_binary_file(file_path):
    pass

def inject_binary_file(file_path):
    pass

view_binary_file("test.bin")

len_of_M82589933 = len("商博")
# print(len("商博")) # this is so basic

print(f"\nThe length of M82589933 is {len_of_M82589933} and M82589933 is not able to encrypt this any futher unless you provide M82589933 with a public key 😘")
GhidraM82589933 = utf8_to_binary("商博")
print(f"\nwith love,\n{GhidraM82589933}")

#M82589933 = ["1"*82589933]
#print(f"with love,\n{M82589933}")
