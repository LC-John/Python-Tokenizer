# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 14:04:17 2019

@author: DrLC
"""

import tokenize
import io
import os, sys

def myTokenize(filename):
    
    with open(filename, "r") as f:
        lines = f.readlines()
        line = ""
        for l in lines:
            line += l
        
    tokens = tokenize.tokenize(io.BytesIO(line.encode('utf-8')).readline)
    string = []
    for t in tokens:
        if t.type in [0, 59, 57]:  # ENDMARKER, ENCODING, COMMENT,
            continue
        elif t.type == 3:   # STRING
            string.append(t.string.replace(' ', '<__SPACE__>') \
                .replace("\n", "<__SLASHN__>") \
                .replace("\r", "<__SLASHR__>"))
        elif t.type in [4, 58]: # EOL
            string.append("<__EOL__>")
        elif t.type == 5:   # INDENT
            string.append("<__IND__>")
        elif t.type == 6:   # DEDENT
            string.append("<__DED__>")
        elif '#' not in t.string:
            string.append(t.string)
    
    return string

if __name__ == "__main__":
    
    tokens = myTokenize("hello_world.py")
    for t in tokens:
        print (t)