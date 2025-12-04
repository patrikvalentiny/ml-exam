from autogen_agentchat.agents import AssistantAgent
from src.models.gemini import gemini_flash
from src.tools.file_tools import save_file

saver = AssistantAgent(
    name="Saver",
    model_client=gemini_flash,
    tools=[save_file],
    system_message="""
    You are the Saver agent. 
    Your task is to save the final exam to a file ONLY when the Reviewer has approved it.
    
    Instructions:
    1. Check the chat history for the Reviewer's message "Exam is approved".
    2. If found, identify the final markdown content of the exam.
    3. Use the `save_file` tool to save this content to 'exam.md'.
    4. After saving, say EXACTLY "TERMINATE".
    5. If the Reviewer has NOT approved the exam yet, just say "Waiting for approval."
    """
)
