import atexit
import json
import sys

from . import argp
from .argparser import Configuration
from .field import Field
from .default_file import create_default_fields
from .header_file import create_header
from .time import print_execution_time


def main():
    config: Configuration = argp.parse_args(sys.argv[1:])
    atexit.register(print_execution_time)

    fields = []
    with open(config.input) as f:
        j = json.load(f)
        # print(j)
        for k in j:
            u = Field(**k)
            fields.append(u)
            # print(u)

    if config.default:
        defaults = create_default_fields(fields)
        with open(config.default, "w") as outfile:
            json.dump(defaults, outfile, indent=4)

    if config.header:
        header = create_header(fields)
        with open(config.header, "w") as outfile:
            outfile.write(header)


if __name__ == '__main__':
    main()
