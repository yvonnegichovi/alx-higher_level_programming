#!/usr/bin/python3

import importlib

if __name__ == "__main__":
    module_import = importlib.import_module('hidden_4')

    names = dir(module_import)
    for i, name in enumerate(names):
        if name[0] == '_':
            continue
        print("{}".format(name))
