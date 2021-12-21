#!/usr/bin/python

import os
import simple

# traverse root directory, and list directories as dirs and files as files
for root, dirs, files in os.walk("."):
    # path = root.split(os.sep)
    # print((len(path) - 1) * '---', os.path.basename(root))
    for file in files:
        # print(len(path) * '---', file)
        if (root.find("2021") != -1 and file.endswith(".txt")):
            simple.simplewordcloud(os.path.join(root, file))