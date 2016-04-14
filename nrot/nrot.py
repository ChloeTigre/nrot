#!/usr/bin/env python3
# -*- encoding: utf-8

"""
nrot - a cipher for brains.

Mostly for python3 though it could be run in python2.

Ideal for playful encryption. Weak against cryptanalysis.
"""


class Nrot_constants(object):
    letterspace = (
        [chr(a) for a in range(ord('A'), ord('Z') + 1)] +
        [chr(a) for a in range(ord('a'), ord('z') + 1)] +
        [chr(a) for a in range(ord('0'), ord('9') + 1)] +
        [a for a in r''' '".?!:;,@#$%^&*()/\=+-_'''] +
        ['\n'] + ['\r'])


def valid_key(key):
    return all(a in Nrot_constants.letterspace for a in key)


def nrot_encrypt(data, key):
    cryptogram = []
    if not valid_key(key):
        raise RuntimeError("Invalid key! Key should be in letterspace")
    ls = Nrot_constants.letterspace
    ls += ls # cheap overflow allow
    for idx, char in enumerate(data):
        rotation_char = key[idx % len(key)]
        rotation_index = ls.index(rotation_char)
        if char not in ls:
            char = '_'
        cryptogram.append(ls[ls.index(char) + rotation_index])
    return ''.join(cryptogram)


def nrot_decrypt(cryptogram, key):
    data = []
    if not valid_key(key):
        raise RuntimeError("Invalid key! Key should be in letterspace")
    ls = Nrot_constants.letterspace
    for idx, char in enumerate(cryptogram):
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
    assert nrot_decrypt(nrot_encrypt(string_b, key_b), key_b) == string_b



# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
