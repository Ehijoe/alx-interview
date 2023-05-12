#!/usr/bin/python3
"""Log Parser."""
import sys
from collections import OrderedDict
import re

ip_regex = r"((\d{1,3}\.){3}\d{1,3})"
date_regex = r"\[(.*)\]"
verb_regex = r"\"GET /projects/260 HTTP/1\.1\""
status_regex = r"(200|301|400|401|403|404|405|500)"
size_regex = r"(\d+)"
pattern = re.compile("^{} - {} {} {} {}$".format(
    ip_regex,
    date_regex,
    verb_regex,
    status_regex,
    size_regex,
))


def process(lines, stat_count):
    """Process a list of log lines and return the total file_size."""
    size = 0
    for line in lines:
        match = pattern.match(line)
        if match is not None:
            try:
                size += int(match.group(5))
            except (ValueError, TypeError):
                pass
            stat_count[int(match.group(4))] += 1
    return size


def print_info(stat_count, size):
    """Print the info from the logs."""
    print("File size: {}".format(size))
    for stat, count in stat_count.items():
        print("{}: {}".format(stat, count))


def main():
    """Parse a log file."""
    to_process = []
    size = 0
    statuses = [200, 301, 400, 401, 403, 404, 405, 500]
    status_count = OrderedDict()
    for status in statuses:
        status_count[status] = 0
    try:
        for line in sys.stdin:
            to_process.append(line)
            if len(to_process) == 10:
                size += process(to_process, status_count)
                print_info(status_count, size)
                to_process = []
    except KeyboardInterrupt:
        size += process(to_process, status_count)
        print_info(status_count, size)


if __name__ == '__main__':
    main()
