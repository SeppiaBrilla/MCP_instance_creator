#!/usr/bin/python3
from instance import Instance
from sys import argv


def main(m,n,max_load_range, file_name, file_path):

    instance = Instance(m,n,max_load_range)

    print(f'max_loads = {instance.max_load},\nsizes = {instance.size}')
    instance.save_dzn(file_name=file_name,file_path=file_path)

if __name__ == "__main__":
    args = argv[1:]
    if len(args) == 0:
        main(3,7,(7,20), None, None)
    elif args[0] == "-a":
        main(3,7,(7,20), None, None)
    elif args[0] == "-m":
        m = int(input("m: "))
        n = int(input("n: "))
        min = int(input("max_load_range (min): "))
        max = int(input("max_load_range (max): "))
        name = input("file name: ")
        path = input("file path: ")
        main(m,n,(min,max), name, path)
    elif args[0] == "-h":
        print('''usage:
-a automatic parameters
-m manual parameters
-h help

default: -a
        ''')