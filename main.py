import player
import click

@click.group()
def cli():
    pass

cli.add_command(player.Player.play)

if __name__ == '__main__':
    cli()
    # player.Player.play()