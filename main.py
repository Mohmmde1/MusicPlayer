import objs.player as player
import click
from config.config import Config



@click.group()
def cli():
    pass

cli.add_command(player.Player.play)
cli.add_command(player.Player.status)



if __name__ == '__main__':
    try:
        cli()
    finally:
        Config.end()

