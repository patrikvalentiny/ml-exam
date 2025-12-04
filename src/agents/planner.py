from autogen_agentchat.agents import AssistantAgent
from src.models.gemini import gemini_flash

planner = AssistantAgent(
    name="Planner",
    model_client=gemini_flash,
    system_message="""
    You are a planner. Your responsibility is to coordinate the exam creation process.
    1. Ask ExamCreator to create the exam based on the user's request.
    2. Ask MarkdownVerifier to verify the markdown format.
    3. Ask Reviewer to review the content and save it if it is good.
    4. If there are issues, coordinate the fixes.
    5. Ensure the process is efficient. Do not add unnecessary comments when the task is completed.
    If you consider the task complete, say EXACTLY "TERMINATE".
    """
)
