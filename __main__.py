
import sys

import argparse

import subprocess as sp

import argparse


class InvalidArguments(Exception):
    pass

from functools import partial

def whoami(args):
    run = partial(sp.run, universal_newlines=True,
                  stdout=sp.PIPE, stderr=sp.DEVNULL)
    name  = run("git config user.name ".split())
    email = run("git config user.email".split())

    print(f"{name.stdout.strip()} {email.stdout.strip()}")

parser     = argparse.ArgumentParser(prog="mygit")
subparsers = parser.add_subparsers()

parser_whoami = subparsers.add_parser("whoami")
parser_whoami.set_defaults(handler=whoami)

try:
    try:
        args = parser.parse_args()

        if hasattr(args, 'handler'):
            args.handler(args)
        else:
            # 未知のサブコマンドの場合はヘルプを表示
            parser.print_help()
            
    except SystemExit as ex:
        returncode, = ex.args
        if returncode != 0:
            raise InvalidArguments()
        raise
except InvalidArguments:
    print("call git command")
    sys.exit(sp.call(["git"] + sys.argv[1:]))

