import os
import pathlib
from getpass import getuser
import logging
logger = logging.getLogger(__name__)

from dotenv import load_dotenv
load_dotenv(pathlib.Path().cwd() / '.env')

from swotbot.team import swotbot_team

def main():
    try:
        _ = os.environ['MISTRAL_API_KEY']
    except KeyError:
        logger.error('MISTRAL_API_KEY not set. I really need this. ')
        exit(1)

    swotbot_team.cli_app(
        message="Introduce yourself briefly, and request the user to provide a project description.",
        show_message=False,
        markdown=True, user=f"\n{getuser() or 'anonymous'}", stream=True, emoji="", )



if __name__ == "__main__":
    main()
