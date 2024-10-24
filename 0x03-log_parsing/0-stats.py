#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics"""
import sys


def print_stats(size, status_codes):
    """Print accumulated metrics"""
    print("File size: {}".format(size))
    for key in sorted(status_codes.keys()):
        if status_codes[key] != 0:
            print("{}: {}".format(key, status_codes[key]))


status_codes = {
    "200": 0, "301": 0, "400": 0, "401": 0,
    "403": 0, "404": 0, "405": 0, "500": 0
}
count = 0
size = 0

try:
    for line in sys.stdin:
        if count != 0 and count % 10 == 0:
            print_stats(size, status_codes)

        try:
            parts = line.split()
            size += int(parts[-1])
            if parts[-2] in status_codes:
                status_codes[parts[-2]] += 1
        except (IndexError, ValueError):
            pass
        count += 1

    print_stats(size, status_codes)

except KeyboardInterrupt:
    print_stats(size, status_codes)
    raise
