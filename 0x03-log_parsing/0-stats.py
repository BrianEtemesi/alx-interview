#!/usr/bin/python3
"""
reads from stdin line by line and computes metrics
"""
import sys


def parse_log():
    """
    parses log files and prints out statistics
    """
    total_size = 0
    status_code_counts = {}

    try:
        line_count = 0
        for line in sys.stdin:
            line_count += 1
            if line_count % 10 == 0:
                print_statistics(total_size, status_code_counts)

            # Parse the line and extract relevant information
            parts = line.split()
            if len(parts) >= 9 and parts[7].isdigit():
                status_code = int(parts[7])
                file_size = int(parts[8])
                total_size += file_size

                if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
                    x = status_code_counts.get(status_code, 0) + 1
                    status_code_counts[status_code] = x

    except KeyboardInterrupt:
        # If the user interrupts with CTRL+C, print the final statistics
        print_statistics(total_size, status_code_counts)


def print_statistics(total_size, status_code_counts):
    print("File size: {}".format(total_size))
    for status_code in sorted(status_code_counts.keys()):
        print("{}: {}".format(status_code, status_code_counts[status_code]))


if __name__ == "__main__":
    parse_log()
