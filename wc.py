#!/Users/kirill/Bioinformatics_Institute/Python/UNIX_utilities/venv/bin/python
import sys
import argparse


def main():
    """Here we implemented wc UNIX-command. As original one it takes input from a file or from stdin.
    Output set by default to direct in stdout, you can change it by adding '> filename'  after a command.
    It can work in pipes.
    Idk why it has some problems while counting bytes in Russian text (-c param)."""
    parser = argparse.ArgumentParser('Count lines, words or bytes. ')
    parser.add_argument('-l', help='prints the line count', action='store_true')
    parser.add_argument('-w', help='prints the word count', action='store_true')
    parser.add_argument('-c', help='prints the byte count', action='store_true')
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    parser.add_argument('outfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout)
    args = parser.parse_args()
    if not args.l and not args.c and not args.w:
        args.l = True
        args.c = True
        args.w = True
    text = args.infile.readlines()
    lines = len(text)
    words = 0
    c_bytes = 0
    for line in text:
        c_bytes += len(line.encode('utf-8'))
        for _ in line.split():
            words += 1
    if args.l and args.c and args.w:
        print(f"\t{lines}\t{words}\t{c_bytes} {args.infile.name if args.infile.name != '<stdin>' else ''}")
    elif args.l and args.c:
        print(f"\t{lines}\t{c_bytes} {args.infile.name if args.infile.name != '<stdin>' else ''}")
    elif args.l and args.w:
        print(f"\t{lines}\t{words} {args.infile.name if args.infile.name != '<stdin>' else ''}")
    elif args.w and args.c:
        print(f"\t{words}\t{c_bytes} {args.infile.name if args.infile.name != '<stdin>' else ''}")
    elif args.c:
        print(f"\t{c_bytes} {args.infile.name if args.infile.name != '<stdin>' else ''}")
    elif args.w:
        print(f"\t{words} {args.infile.name if args.infile.name != '<stdin>' else ''}")
    else:
        print(f"\t{lines} {args.infile.name if args.infile.name != '<stdin>' else ''}")
    return 0

if __name__ == '__main__':
    main()
