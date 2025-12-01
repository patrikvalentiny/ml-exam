import asyncio
from autogen_core.models import UserMessage
from models.Ollama import ollama_model_client
from models.Gemini import gemini_model_client

async def main():
    # Assuming your Ollama server is running locally on port 11434.
    client = gemini_model_client
    try:
        response = await client.create([UserMessage(content="What is the capital of France?", source="user")])
        print(response)
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())