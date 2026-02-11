#!/usr/bin/env python3

import sys
import re

params = sys.argv[1:]

if not params:
    print("none")
else:
    for param in params:
        if not re.search(r"ism$", param):
            print(param + "ism")
