"""Command line entry point for plumbgamble8b_kit."""
import argparse
import sys

from .core import Plumbgamble8bTool


def main(argv=None):
    parser = argparse.ArgumentParser(description="check JSON syntax")
    parser.add_argument("files", nargs="+")
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args(argv)
    checker = Plumbgamble8bTool()
    failed = 0
    for path in args.files:
        ok, payload = checker.check(path)
        if ok:
            if not args.quiet:
                print(payload)
        else:
            failed += 1
            print(f"{path}: {payload}", file=sys.stderr)
    return 1 if failed else 0
