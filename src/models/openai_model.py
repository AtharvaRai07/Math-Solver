from config.constant import MODEL,API_KEY
from autogen_ext.models.openai import OpenAIChatCompletionClient

def get_model():
    model_client = OpenAIChatCompletionClient(
        model = MODEL,
        api_key = API_KEY
    )
    return model_client