#!/usr/bin/env python3
"""
Simple command-line tool using sys.argv
"""
import sys


def say_it(greeting, target):
    message = f"{greeting} {target}"
    print(message)


if __name__ == '__main__':
    greeting = "Hello"
    target = "Joe"

    if '--name' in sys.argv:
        name_index = sys.argv.index('--name') + 1
        if name_index < len(sys.argv):
            target = sys.argv[name_index]
    

    say_it(greeting, target)
