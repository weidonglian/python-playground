import click, sys


@click.group()
@click.option('--debug/--no-debug', default=False)
def cli(debug):
    click.echo('Debug mode is %s' % ('on' if debug else 'off'))

@cli.command()
def cmake():
    click.echo('cmake')
    sys.exit(1)

@cli.command()
def test():
    click.echo('testing')
    sys.exit(0)

if __name__ == '__main__':
    cli()