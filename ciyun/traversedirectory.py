#!/usr/bin/python

import os
import simple
from pathlib import Path

# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk("."):
    # path = root.split(os.sep)
    # print((len(path) - 1) * '---', os.path.basenamos.pathe(root))
    for file in files:
        # print(len(path) * '---', file)
        txt = Path(os.path.join(root, file))
        png = Path(os.path.join(root, file)).with_suffix('.png')
        if (root.find("2022") != -1 and txt.suffix == ".txt"):
            if (not png.exists() or os.path.getmtime(txt) > os.path.getmtime(png)):
                simple.simplewordcloud(txt)
