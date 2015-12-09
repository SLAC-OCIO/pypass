#!/usr/bin/env python
# encoding: utf-8
from tempfile import mkstemp
from shutil import move
from os import remove, close
import codecs
filename='/Users/xalg/dev/Python/aegir_ldap/global.inc'

def replace(source_file_path, pattern, substring):
    fh, target_file_path = mkstemp()

    with codecs.open(target_file_path, 'w', 'utf-8') as target_file:
        with codecs.open(filename, 'r', 'utf-8') as source_file:
            for line in source_file:
                target_file.write(line.replace(orig, new))
    remove(source_file_path)
    move(target_file_path, source_file_path)

def main():
    replace(filename,orig,new)

if __name__ == '__main__':
    main()