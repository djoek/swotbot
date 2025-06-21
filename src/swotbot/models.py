import os
from agno.models.mistral import MistralChat

mistral_model = MistralChat(id="mistral-medium-latest", api_key=os.getenv("MISTRAL_API_KEY"), )
