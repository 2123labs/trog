import argparse
import sys
from trog.trog import convert_trog

args = argparse.ArgumentParser()
args.add_argument("trogfile", metavar="FILE", type=str, help="File to Trog")
args.add_argument("outfile", metavar="OUTFILE", type=str, help="Output Path", default="-")


def main() -> None:
    a = args.parse_args()
    inf = open(a.trogfile, "r")
    if a.outfile == "-":
        outf = sys.stdout
    else:
        outf = open(a.outfile, "w")
    convert_trog(inf, outf)
    outf.close()
    inf.close()
