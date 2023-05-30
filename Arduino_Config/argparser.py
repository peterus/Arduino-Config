import os
import argparse

from dataclasses import dataclass
from pathlib import Path


@dataclass(eq=True, frozen=True)
class Configuration:
    input: str
    default: str
    header: str


class ArgumentParser:
    args = None
    parser = None

    def __init__(self):
        self._init_argparse()

    @staticmethod
    def _check_file(path: Path):
        if not os.path.isfile(path):
            from . import die
            die(f"No valid file: {path}")

    @staticmethod
    def _check_dir(path: Path):
        if not os.path.isdir(path):
            from . import die
            die(f"No valid directory: {path}")

    def _init_argparse(self):
        self.parser = argparse.ArgumentParser()

        self.parser.add_argument('input', help="input description file.")
        self.parser.add_argument('--default', help="save defaults to json file.")
        self.parser.add_argument('--header', help="save header file.")

    def parse_args(self, args) -> Configuration:
        from . import die
        self.args = self.parser.parse_args(args)

        input = Path(self.args.input)
        self._check_file(input)

        default = None
        if self.args.default:
            default = Path(self.args.default)

        header = None
        if self.args.header:
            header = Path(self.args.header)

        if not default and not header:
            die("default or header file must be given")

        return Configuration(input, default, header)
