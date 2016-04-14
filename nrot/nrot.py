#!/usr/bin/env python3
# -*- encoding: utf-8

"""
nrot - a cipher for brains.

Mostly for python3 though it could be run in python2.

Ideal for playful encryption. Weak against cryptanalysis.
"""


class Nrot_constants(object):
    letterspace = (
        [chr(a) for a in range(ord('0'), ord('9') + 1)] +
        [chr(a) for a in range(ord('a'), ord('z') + 1)] +
        [chr(a) for a in range(ord('A'), ord('Z') + 1)]
    )

    immutables = list(' \r\n' + r''''".?!:;,@#$%^&*()/\=+-_''')


def valid_key(key):
    return all(a in Nrot_constants.letterspace for a in key)


def nrot_encrypt(data, key):
    cryptogram = []
    if not valid_key(key):
        raise RuntimeError("Invalid key! Key should be in letterspace")
    ls = Nrot_constants.letterspace
    ls += ls # cheap overflow allow
    for idx, char in enumerate(data):
        if char in Nrot_constants.immutables:
            cryptogram.append(char)
            continue
        rotation_char = key[idx % len(key)]
        rotation_index = ls.index(rotation_char)
        if char not in ls:
            cryptogram.append('_')
            continue
        cryptogram.append(ls[ls.index(char) + rotation_index])
    return ''.join(cryptogram)


def nrot_decrypt(cryptogram, key):
    data = []
    if not valid_key(key):
        raise RuntimeError("Invalid key! Key should be in letterspace")
    ls = Nrot_constants.letterspace
    for idx, char in enumerate(cryptogram):
        if char in Nrot_constants.immutables:
            data.append(char)
            continue
        rotation_char = key[idx % len(key)]
        rotation_index = ls.index(rotation_char)
        data.append(ls[ls.index(char) - rotation_index])
    return ''.join(data)


def test_nrot():
    string_a = "J'aime les Pâtes"
    key_a = "emansupilo"
    expected_out = "J'aime les P_tes"
    assert nrot_decrypt(nrot_encrypt(string_a, key_a), key_a) == expected_out
    string_b = '''
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
    veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
    consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
    cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat
    cupidatat non proident, sunt in culpa qui officia deserunt mollit
    anim id est laborum.'''
    key_b = '75niAXdmJAoksgGDyUaC'
    cryptogram_b = nrot_encrypt(string_b, key_b)
    assert nrot_decrypt(cryptogram_b, key_b) == string_b
    print("Cryptogram b:", cryptogram_b)




# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
