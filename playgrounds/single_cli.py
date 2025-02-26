import click
import sys


@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def cli(count: int, name: str):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)
    sys.exit(1)

def cli_test(count: int, name: str):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(10):
        print(f'Hello {name}!')

if __name__ == '__main__':
    cli()
