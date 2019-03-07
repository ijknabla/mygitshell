
import argparse

from sys import argv

import subprocess as sp

sp.call(['git'] + argv[1:])
