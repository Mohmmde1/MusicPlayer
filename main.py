import player
import click

@click.group()
def cli():
    pass

cli.add_command(player.Player.play)
cli.add_command(player.Player.current_song_status)



if __name__ == '__main__':
    
    cli()

