"""
This is the main file for the zync package.
"""

import argparse
from .__init__ import __all__ as methods

NAME = "zyncify"
DISPLAY_NAME = "zync"
DESCRIPTION = "zync is a utility tool for python operations"
URL = "https://github.com/tjbredemeyer/zync"
VERSION = "0.1.3"
AUTHOR = "TJ Bredemeyer"
AUTHOR_EMAIL = "tj@teicor.com"
LICENSE = "GNU Public License v3"

info_string = (
    "\n"
    f"name: {DISPLAY_NAME}\n"
    f"version: {VERSION}\n"
    f"author: {AUTHOR} - {AUTHOR_EMAIL}\n"
    f"license: {LICENSE}\n"
    f"url: {URL}\n"
    f"description: {DESCRIPTION}"
    "\n"
)


def main():
    """
    This is the main function for the zync package.
    """

    parser = argparse.ArgumentParser(description=NAME)
    parser.add_argument(
        "--version", action="version", version=f"\n{VERSION}\n"
    )
    parser.add_argument(
        "--info",
        action="store_const",
        const=info_string,
        help="show information about the zync package",
    )
    parser.add_argument(
        "--methods",
        action="store_const",
        const=methods,
        help="show available methods for the zync package",
    )

    args = parser.parse_args()

    if args.info:
        print(info_string)
    if args.methods:
        print("\navailable zyncs:")
        for method in methods:
            print(f"  {method}")
        print()
    if not args.info and not args.methods:
        parser.print_help()


if __name__ == "__main__":
    main()
