#!/usr/bin/env python

import sys
import argparse
import polib

GREEN = '\033[92m'
RED = '\033[91m'
BLUE = '\033[94m'
NC='\033[0m' # No Color

def main(arguments):

    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-p', '--po', help="po file input")
    parser.add_argument('-m', '--mo', help="mo file output")

    args = parser.parse_args(arguments)

    print "%sSaving %s as %s%s" % (BLUE,args.po,args.mo,NC)
    polib.pofile(args.po).save_as_mofile(args.mo)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
