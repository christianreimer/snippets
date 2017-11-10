"""
Simple checksum calculation for a dictionary.

Useful when sending deltas (updates) in a distributed system, to allow the
downsteam party to validate they have not missed in intermediate update and
have the correct data.
"""


import json
import hashlib


def checksum(data):
    return hashlib.sha1(json.dumps(data, sort_keys=True).encode()).hexdigest()


def main():
    data = {'name': 'First Last', 'age': 42, 'choice': False}
    print(f'The checksum for {data} is {checksum(data)}')


if __name__ == '__main__':
    main()
