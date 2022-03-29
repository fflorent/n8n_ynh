#!/usr/bin/env python3

import sys

def main():
    print("SET sql_mode='NO_BACKSLASH_ESCAPES';")
    lines = sys.stdin.read().splitlines()
    for line in lines:
        processLine(line)

def processLine(line):
    if (
        line.startswith("PRAGMA") or
        line.startswith("BEGIN TRANSACTION;") or
        line.startswith("COMMIT;") or
        line.startswith("DELETE FROM sqlite_sequence;") or
        line.startswith("INSERT INTO \"sqlite_sequence\"")
       ):
        return
    line = line.replace("AUTOINCREMENT", "AUTO_INCREMENT")
    line = line.replace("DEFAULT 't'", "DEFAULT '1'")
    line = line.replace("DEFAULT 'f'", "DEFAULT '0'")
    line = line.replace(",'t'", ",'1'")
    line = line.replace(",'f'", ",'0'")
    in_string = False
    new_line = ''
    for c in line:
        if not in_string:
            if c == "'":
                in_string = True
            elif c == '"':
                new_line = new_line + '`'
                continue
        elif c == "'":
            in_string = False
        new_line = new_line + c
    print(new_line)

if __name__ == "__main__":
    main()
