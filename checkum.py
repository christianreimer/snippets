"""
Simple checksum calculation for a dictionary.

Useful when sending deltas (updates) in a distributed system, to allow the
downsteam party to validate they have not missed in intermediate update and
have the correct data.
"""


import json as j
import hashlib as h


def checksum(data):
    return f'0x{h.sha1(j.dumps(data, sort_keys=True).encode()).hexdigest()}'


def main():
    data = {'name': 'First Last', 'age': 42, 'choices': [False, False, True]}
    print(f'The checksum for {data} is {checksum(data)}')


if __name__ == '__main__':
    main()
