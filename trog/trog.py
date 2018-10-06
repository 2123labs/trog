from arpeggio import ParserPython

from trog.grammar.peg import trogfile

from typing.io import TextIO


def convert_trog(inf: str, outf: TextIO) -> None:
    pp = ParserPython(trogfile, skipws=False)
    try:
        tree = pp.parse_file(inf)
        print(tree)
    except Exception as e:
        print(e)
