from autogen_agentchat.agents import AssistantAgent
from src.models.gemini import gemini_pro
from src.tools.file_tools import save_file

reviewer = AssistantAgent(
    name="Reviewer",
    model_client=gemini_pro,
    tools=[save_file],
    system_message="""
    You are an expert reviewer. 
    Verify the answers in the exam. Check if they are correct based on your knowledge. 
    Also provide suggestions for improvement. 
    If the exam is good and you have no further suggestions, SAVE the exam to a file named 'exam.md' using the `save_file` tool.
    AFTER saving, say EXACTLY "TERMINATE".
    """ 
)
