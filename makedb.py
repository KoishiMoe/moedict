#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import argparse
import sqlite3

def load_dict(filepath):
    with open(filepath, 'r') as file:
        for line in file:
            if len(ls := line.split("	")) == 2:
                yield ls[0].strip(), ls[1].strip().replace(" ", "")

def makedb(input_file, output_file):
    conn = sqlite3.connect(output_file)

    cursor = conn.cursor()
    cursor.execute('PRAGMA synchronous = OFF;')
    cursor.execute('PRAGMA journal_mode = MEMORY;')
    cursor.execute('PRAGMA secure_delete = OFF;')
    cursor.execute('PRAGMA foreign_keys = OFF;')
    cursor.execute('PRAGMA locking_mode = EXCLUSIVE;')

    insert_query = 'INSERT INTO entry (word, shortcut, locale) VALUES (?, ?, "zh-CN")'
    cursor.executemany(insert_query, load_dict(input_file))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a tab-separated dictionary to a Gboard personal dictionary sqlite db.")
    parser.add_argument("input", type=str, help="The input file.")
    parser.add_argument("output", type=str, help="The template & output file.")
    args = parser.parse_args()
    makedb(args.input, args.output)
