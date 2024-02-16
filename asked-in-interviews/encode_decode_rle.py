"""

encode_rle(input_string): This function takes a string input_string as input and returns the Run Length Encoded (RLE)
string for the input string. In RLE, the output string should contain the character followed by the count of consecutive
occurrences of that character. If a character appears only once, its count should be '1'. The output string should
maintain the order of characters from the input string.

decode_rle(encoded_string): This function takes an encoded string encoded_string as input and returns the original
string before encoding. The input encoded string is formed by consecutive characters followed by their count. You need
to repeat each character according to its count to reconstruct the original string.

Example:

For input string "AAABBBCCCD", the output of encode_rle(input_string) should be "A3B3C3D1". The input string is encoded
as "A3B3C3D1" because there are 3 consecutive 'A's, 3 consecutive 'B's, 3 consecutive 'C's, and 1 'D' in the input
string.

For encoded string "A3B3C3D1", the output of decode_rle(encoded_string) should be "AAABBBCCCD". The encoded string is
decoded back to the original input string by repeating each character according to its count.

You need to implement the encode_rle and decode_rle functions to solve this problem. Ensure that your solution handles
edge cases and maintains the order of characters.
"""


def encode_rle(input_string):
    count = 1
    if len(input_string) == 0:
        return 0

    prev_char = input_string[0]
    encode_string = ''
    for i in range(1, len(input_string)):
        if prev_char == input_string[i]:
            count += 1

        else:
            encode_string += prev_char + str(count)
            count = 1
            prev_char = input_string[i]

    encode_string += prev_char + str(count)
    return encode_string


def decode_rle(input_string):
    chars = []
    digits = []
    count = ''
    decode_str = ''
    for char in input_string:
        if char.isdigit():
            count += char
        else:
            chars.append(char)
            digits.append(count)
            count = ''
    digits.append(count)
    digits.remove(digits[0])
    for i in range(len(chars)):
        decode_str += chars[i] * int(digits[i])
    return decode_str


print('encoded', encode_rle('AAABBCCGFDHTT'))
print('decoded', decode_rle('A3B1C1B3A3D1A1'))
