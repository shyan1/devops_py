#!/usr/bin/env python3

import click


@click.group()
def cli():
    pass


@click.group(help='Ship related commands')
def ships():
    pass


cli.add_command(ships)


@ships.command(help='Sail a ship')
def sail():
    ship_name = "Your ship"
    print(f"{ship_name} is setting sail")


@ships.command(help='List all of the ships')
def list_ships():
    ships = ['John B', 'Yankee Clipper', 'Pequod']
    print(f"Ships: {','.join(ships)}")

@cli.command(help='Talk to a sailer')
@click.option('--greeting', default='Ahoy there', help='Greeting for sailer')
@click.argument('name')
def sailers(greeting, name):
    message = f"{greeting} {name}"
    print(message)

if __name__ == '__main__':
    cli()