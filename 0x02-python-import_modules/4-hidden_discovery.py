#!/usr/bin/python3
import sys

module_path = "hidden_4.pyc"

if __name__ == "__main__":
    module_namescape = {}
    with open(module_path, 'rb') as f:
        code = compile(f.read(), module_path, 'exec')
        exec(code, module_namescape)
        filtered_names = [name for name in module_namescape if not name.startswith("__")]
        sorted_names = sorted(filtered_names)
        for name in sorted_names:
            print(name)
