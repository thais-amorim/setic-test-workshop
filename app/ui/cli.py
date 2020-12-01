#!/usr/bin/python
import click
import os
from app.calculator import Calculator as c

def arg_to_list(args):
    option = args
    try:
        option = str(option)
    except ValueError:
        pass

    option = option[1:-1]  # trim '[' and ']'

    options = option.split(',')

    for i, value in enumerate(options):
        # catch integers
        try:
            int(value)
        except ValueError:
            options[i] = value
        else:
            options[i] = int(value)
    return options


class TerminalView():

    @click.group()
    def process():
        pass

    @click.command()
    @click.option("--operator", "-o", "operator", required=True,
                  help="A valid operator",
                  )
    @click.option("--input-x", "-x", "x", required=True,
                  help="A valid number",
                  )
    @click.option("--input-y", "-y", "y", required=True,
                  help="A valid number",
                  )
    def calc(operator, x, y):
        """
        Realize a computation based on the passed parameters.
        """
        result = c.calculate(
            int(operator),
            int(x),
            int(y)
            )
        print(result, end='\n')

    # Add commands to group
    process.add_command(calc)
