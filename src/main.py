from swotbot.team import swotbot
from dotenv import load_dotenv

load_dotenv('./.env')

if __name__ == "__main__":
    swotbot.cli_app(
        message="Introduce yourself by name and purpose, and request the user to provide a project description.",
        markdown=True, user="\nUser", stream=True, emoji="",)

