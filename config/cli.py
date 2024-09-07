import click

@click.group()
def cli():
    pass

@cli.command()
def start():
    """Start the NIDS"""
    print("NIDS started")

@cli.command()
def stop():
    """Stop the NIDS"""
    print("NIDS stopped")

@cli.command()
def configure():
    """Configure the NIDS"""
    print("NIDS configured")

if __name__ == '__main__':
    cli()
    