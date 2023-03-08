# topmost.py as part of lab 1
# Joel h 4/07-2020
from wordfreq import tokenize, countWords, printTopMost
import sys
import urllib.request
# Try adding a comment


def main():
    inp_stopfile = open(sys.argv[1], "r", encoding="utf-8")
    n = sys.argv[3]

    # Check if url of local file
    if sys.argv[2].startswith("http://") or sys.argv[2].startswith("https://"):
        inp_file = urllib.request.urlopen(sys.argv[2])
        lines = inp_file.read().decode("utf8").splitlines()
        words = (tokenize(lines))
    else:
        inp_file = open(sys.argv[2], "r", encoding="utf-8")
        words = (tokenize(inp_file))

    # perform counting and sorting
    dic = countWords(words, inp_stopfile)
    printTopMost(dic, int(n))

    # close files
    inp_file.close()
    inp_stopfile.close()


main()
