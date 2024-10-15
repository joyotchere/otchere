#!/usr/bin/env python3
# Author ID: JoyOtchere

def is_digits(sobj):
    # Loops through each character in sobj and checks if it is a digit
    for char in sobj:
        if not char.isdigit():
            return False
    return True

if __name__ == '__main__':
    test_list = ['x3058', '3058', '8503x', '8503']
    for item in test_list:
        if is_digits(item):
            print(item, 'is an integer.')
        else:
            print(item, 'is not an integer.')
