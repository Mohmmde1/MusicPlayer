import player
import click
from config import Config



@click.group()
def cli():
    pass

cli.add_command(player.Player.play)
cli.add_command(player.Player.status)



if __name__ == '__main__':
    Config.start()
    cli()

