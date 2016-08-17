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
    parser.add_argument('-p', '--po', help="po file")

    args = parser.parse_args(arguments)

    pofile = polib.pofile(args.po)

    print "pofile %d translated" % pofile.percent_translated()

    for entry in pofile.untranslated_entries():
        print "%sMessage: %s%s%s" % (BLUE, GREEN, entry.msgid,NC)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
