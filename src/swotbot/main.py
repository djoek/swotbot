import pathlib
from getpass import getuser
import logging

logger = logging.getLogger(__name__)

from dotenv import load_dotenv

load_dotenv(pathlib.Path().cwd() / '.env')

import typer
from swotbot.models import AvailableModels, set_model


def main(model: AvailableModels = "mistral"):

    set_model(model)
    from swotbot.team import swotbot_team

    swotbot_team.cli_app(
        message="Introduce yourself briefly, and request the user to provide a project description.",
        show_message=False,
        markdown=True, user=f"\n{getuser() or 'anonymous'}", stream=True, emoji="", )

def run():
    typer.run(main)

if __name__ == "__main__":
    typer.run(main)
