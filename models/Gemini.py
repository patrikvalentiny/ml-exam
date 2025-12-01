import os
from dotenv import load_dotenv
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.models import ModelInfo

load_dotenv()

model_info = ModelInfo(
    vision=True,
    function_calling=True,
    json_output=True,
    family='gemini-2.5-flash',
    structured_output=True
)


gemini_model_client = OpenAIChatCompletionClient(
    model="gemini-2.5-flash-lite",
    model_info=model_info,
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )