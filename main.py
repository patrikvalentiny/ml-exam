import asyncio
from pprint import pprint
from autogen_core.models import UserMessage
from src.models.ollama import ollama_model_client
from src.models.gemini import gemini_model_client
from autogen_agentchat.ui import Console
from autogen_agentchat.agents import AssistantAgent
from src.memory import chroma_memory


async def main():
    system_message = """Return a comprehensive answer based on the provided context. Answer in markdown format where appropriate. 
    Do not fabricate information. If the context does not contain the answer, respond with 'The provided context does not contain the answer to your question.'
    Do not mention anything about memory or how you retrieved the information.
    """

    client = gemini_model_client
    assistant = AssistantAgent(
        name="GeminiAssistant", model_client=client, memory=[chroma_memory], system_message=system_message
    )

    # client = ollama_model_client
    # assistant = AssistantAgent(
    #     name="OllamaAssistant", model_client=client, memory=[chroma_memory], system_message=system_message
    # )


    try:
        stream = assistant.run_stream(
            task="Generate a quiz about newest period of literature in Slovakia.",
        )
        await Console(stream)
        # response = await client.create([UserMessage(content="What knowledge about slovak literature do you have in memory", source="user")])
        # pprint(response)
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(main())
