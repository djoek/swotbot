import os
import enum
import logging

logger = logging.getLogger(__name__)

model = None


class AvailableModels(str, enum.Enum):
    mistral = "mistral"
    openai = "openai"


def set_model(model_choice: AvailableModels):
    global model

    match model_choice:
        case AvailableModels.mistral:
            from agno.models.mistral import MistralChat

            try:
                mistral_api_key = os.environ["MISTRAL_API_KEY"]
            except KeyError:
                logger.warning("MISTRAL_API_KEY is not set. Mistral will not be available.")
            else:
                model = MistralChat(id="mistral-large-latest", api_key=mistral_api_key, )
        case AvailableModels.openai:
            from agno.models.openai import OpenAIChat

            try:
                openai_api_key = os.environ["OPENAI_API_KEY"]
            except KeyError:
                logger.warning("OPENAI_API_KEY is not set. OpenAI will not be available.")
            else:
                model = OpenAIChat(id="gpt-4o", api_key=openai_api_key, )
        case _:
            raise ValueError("No valid model available")


