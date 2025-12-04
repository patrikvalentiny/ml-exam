import os
from dotenv import load_dotenv
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.models import ModelInfo

load_dotenv()

keys = [
    os.getenv("GEMINI_EXAMK1"),
    os.getenv("GEMINI_EXAMK2"),
    os.getenv("UNIF2025"),
]


model_info = ModelInfo(
    vision=True,
    function_calling=True,
    json_output=True,
    family='gemini',
    structured_output=True,
    multiple_system_messages=True
)


gemini_flash_lite = OpenAIChatCompletionClient(
    model="gemini-2.5-flash-lite",
    model_info=model_info,
    api_key=keys[0],
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    cache_seed=None,
)

gemini_flash = OpenAIChatCompletionClient(
    model="gemini-2.5-flash",
    model_info=model_info,
    api_key=keys[1],
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    cache_seed=None,
)

gemini_pro = OpenAIChatCompletionClient(
    model="gemini-2.5-pro",
    model_info=model_info,
    api_key=keys[2],
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    cache_seed=None,
)