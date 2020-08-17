#!/usr/bin/env python3

import fire


class Ships():
    def sail(self):
        ship_name = "Your ship"
        print(f"{ship_name} is setting sail")

    def list(self):
        ships = ['John B', 'Yankee Clipper', 'Pequod']
        print(f"Ships: {','.join(ships)}")


def sailors(greeting, name):
    print(f"{greeting} {name}")


class Cli():
    def __init__(self):
        super().__init__()
        self.sailers = sailors
        self.ships = Ships()


if __name__ == '__main__':
    fire.Fire(Cli)