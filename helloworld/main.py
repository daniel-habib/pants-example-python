# Copyright 2020 Pants project contributors.
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from colors import blue

from helloworld.greet.greeting import Greeter


def say_hello() -> None:
    greeting = Greeter().greet("Pantsbuild")
    print(blue(greeting))


if __name__ == "__main__":
    say_hello()
