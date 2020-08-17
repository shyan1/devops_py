#!/usr/bin/env python3

import click

@click.command()
@click.option('--greeting', default='Hiya', help='How do you want to greet?')
@click.option('--name', default='Tammy', help='Who do you want to greet?')
def greet(greeting, name):
    message = f"{greeting} {name}"
    print(message)

if __name__ == '__main__':
    greet()