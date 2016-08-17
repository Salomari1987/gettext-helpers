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
    parser.add_argument('-b', '--base', help="Base po file")
    parser.add_argument('-u', '--update', help="po file to update base from")
    parser.add_argument('-o', '--outfile', help="Output file", default=None)

    args = parser.parse_args(arguments)

    base_po = polib.pofile(args.base)
    update_po = polib.pofile(args.update)

    print "base_po %d translated" % base_po.percent_translated()
    print "update_po %d translated" % update_po.percent_translated()


    for update_entry in update_po.translated_entries():
        base_entry = base_po.find(update_entry.msgid)
        if base_entry and base_entry.msgstr !=  update_entry.msgstr:
            print "%sMessage: %s%s" % (BLUE, GREEN, base_entry.msgid)
            print "%sUpdated: %s%s" % (BLUE, RED, base_entry.msgstr)
            print "%sTo: %s%s%s" % (BLUE, GREEN,update_entry.msgstr,NC)
            print "******"
            base_entry.msgstr = update_entry.msgstr

    print "New po %d translated" % base_po.percent_translated()
    outfile = args.outfile if args.outfile else args.base
    print "%sSaving to %s%s" % (BLUE,outfile,NC)
    base_po.save(outfile)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
