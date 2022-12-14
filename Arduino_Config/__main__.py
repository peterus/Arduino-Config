
import json
import argparse
from .field import Field
from .default_file import create_default_fields
from .header_file import create_header_file

parser = argparse.ArgumentParser()
parser.add_argument('input', help="input description file.")
parser.add_argument('--default', help="save defaults to json file.")
parser.add_argument('--header', help="save header file.")
args = parser.parse_args()
print(args.default, args.input)

fields = []
with open(args.input) as f:
    j = json.load(f)
    # print(j)
    for k in j:
        u = Field(**k)
        fields.append(u)
        # print(u)

if args.default:
    defaults = create_default_fields(fields)
    with open(args.default, "w") as outfile:
        json.dump(defaults, outfile, indent=4)

if args.header:
    header = create_header_file(fields)
    with open(args.header, "w") as outfile:
        outfile.write(header)
