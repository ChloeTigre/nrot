#!/usr/bin/env python
# -*- encoding: utf-8

"""
nrot: cipher or decipher text using a key.


Usage: nrot (--encrypt|--decrypt) --key KEY --text TEXT

Options:
    --encrypt       encrypt mode
    --decrypt       decrypt mode
    --key KEY       use this key
    --text TEXT     [en|de]crypt this text
"""
import nrot.nrot as nrot
import docopt
import sys

def load_text_from_stdin():
    return "".join(sys.stdin)

if __name__ == '__main__':
    pass
    opts = docopt.docopt(__doc__)
    if opts['--text'] == '-':
        opts['--text'] = load_text_from_stdin()
    args = (opts['--text'], opts['--key'], )
    if opts['--encrypt']:
        print(nrot.nrot_encrypt(*args))
    else:
        print(nrot.nrot_decrypt(*args))

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
