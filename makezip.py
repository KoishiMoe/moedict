#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import argparse
import zipfile

def convert(input_file, output_file):
    if (os.path.exists("dictionary.txt")):
        raise FileExistsError("dictionary.txt already exists.")
    with open(input_file, 'r') as f:
        with open("dictionary.txt", 'w', encoding='utf-8') as o:
            o.write("# Gboard Dictionary version:1\n\n")
            for line in f:
                if len(ls := line.split("	")) == 2:
                    o.write(ls[1].strip().replace(" ", "") + "	" + ls[0].strip() + "	" + "zh-CN\n")
    
    with zipfile.ZipFile(output_file, 'w') as z:
        z.write("dictionary.txt")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a tab-separated dictionary to a Gboard dictionary.")
    parser.add_argument("input", type=str, help="The input file.")
    parser.add_argument("output", type=str, help="The output file.")
    args = parser.parse_args()
    convert(args.input, args.output)
                    