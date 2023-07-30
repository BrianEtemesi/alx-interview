#!/usr/bin/python3
"""
funtion to determine if data set represents valid UTF-8 encoding
"""


def validUTF8(data):
    """
    determine if data set represents a valid UTF-8 encoding
    """
    num_bytes_to_process = 0

    for byte in data:
        if num_bytes_to_process == 0:
            # Check for single-byte character (ASCII)
            if byte & 0x80 == 0:
                continue

            # Count the number of leading '1's to
            num_bytes_to_process = 1
            mask = 0x40
            while byte & mask:
                num_bytes_to_process += 1
                mask >>= 1

            # Invalid number of bytes for a character
            if num_bytes_to_process > 4 or num_bytes_to_process == 1:
                return False

        else:
            # Check if the current byte starts with '10' pattern
            if not (byte & 0xC0 == 0x80):
                return False

        # Decrement the number of bytes to process for the character
        num_bytes_to_process -= 1

    return num_bytes_to_process == 0
