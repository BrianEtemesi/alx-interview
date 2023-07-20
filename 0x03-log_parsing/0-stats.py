#!/usr/bin/python3
"""
reads from stdin line by line and computes metrics
"""
import sys

line_count = 0
FileSize = 0

status = {'200': 0, '301': 0, '400': 0, '401': 0,
          '403': 0, '404': 0, '405': 0, '500': 0}

codes = ['200', '301', '400', '401', '403', '404', '405', '500']

try:
    for line in sys.stdin:
        line_count += 1

        # Parse the line and extract relevant information
        parts = line.split(' ')

        if len(parts) > 2:
            FileSize += int(parts[-1])
            if parts[-2] in status:
                status[parts[-2]] += 1

        if line_count % 10 == 0:
            print("File size: {}".format(FileSize))
            for code in codes:
                if status[code]:
                    print("{}: {}".format(code, status[code]))

except KeyboardInterrupt:
    pass
finally:
    print("File size: {}".format(FileSize))
    for code in codes:
        if status[code]:
            print("{}: {}".format(code, status[code]))
