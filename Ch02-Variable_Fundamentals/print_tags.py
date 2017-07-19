#! /usr/bine/env python3.6

import re
fh = open("./tags.html")
p = re.compile(r"^<([a-z]+)>(.*)</\1>$")
for line in fh:
    mo = p.search(line)
    print(mo.group(1) + ": " + mo.group(2))

fh.close()
