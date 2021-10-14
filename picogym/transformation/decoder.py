
def encode(flag):
    encoded = ([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
    return encoded

'''
''.join adds everything to a string
chr() converts a number to character
ord() converts a character to base10 number

iterate throught the elements of flag in 2's
use ord() to convert both characaters to base10 numbers
multiply the first one by 2^8
leave the second as is
convert both base10 numbers to characters
join
'''

def decode(enc_flag):
    dec_flag = ""
    for i in range(0, len(enc_flag)):
        packed_int = ord(enc_flag[i])
        high_char = packed_int >> 8
        dec_flag += chr(high_char)
        low_char = packed_int - (high_char << 8)
        dec_flag += chr(low_char)
    print(f"\n Decoded is: {dec_flag}")

enc_flag = input("Encoded flag: ")
decode(enc_flag)
