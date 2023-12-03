import sys
from parser import Parser

class Assembler:

    def main():
        path = sys.argv[1]
        print("filepath is: " + path)
        # TODO: populate symbols

        parser = Parser()
        parser.preprocess(path)
        parser.process(path)
# 
    main()