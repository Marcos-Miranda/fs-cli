import click
import yaml


@click.group()
def cli():
    pass


@cli.command()
# @click.option("")
def print_1():
    click.echo("print_1")


@cli.command()
def print_2():
    click.echo("print_2")


if __name__ == "__main__":
    cli()
