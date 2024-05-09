#!/usr/bin/python3
"""
UTF-8 Encoding Validation
"""


def validUTF8(data):
    """
    Return true if data is a valid UTF-8 encoding, else return False
    """
    byte_num = 0

    for byte in data:
        if byte_num == 0:
            if byte >> 5 == 0b110 or byte >> 5 == 0b1110:
                byte_num = 1
            elif byte >> 4 == 0b1110:
                byte_num = 2
            elif byte >> 3 == 0b11110:
                byte_num = 3
            elif byte >> 7 == 0b1:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            byte_num -= 1
    return byte_num == 0
