import argparse
import codecs
import fileinput

from . import lemmatize_line


def main() -> int:
    parser = argparse.ArgumentParser(
        description='A lemmatizer for Icelandic text')

    parser.add_argument('-s', '--separator', help='the string separating word forms, tags and lemmas (default: \\t)',
                        default='\t')

    parser.add_argument('filename', nargs='*', help='File to read and parse')

    args = parser.parse_args()

    separator = codecs.decode(args.separator, 'unicode_escape')

    has_errors = False
    for line in fileinput.input(args.filename):
        form, tag, lemma = lemmatize_line(line, separator)
        if form is not None and tag is not None and lemma is not None:
            print(separator.join([form, tag, lemma]))
            continue
        else:
            has_errors = True
        print()

    if has_errors:
        return 1
    else:
        return 0


if __name__ == '__main__':
    exit(main())
