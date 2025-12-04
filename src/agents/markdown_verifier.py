from autogen_agentchat.agents import AssistantAgent
from src.models.gemini import gemini_flash_lite
from src.tools.markdown_tools import verify_markdown_content

markdown_verifier = AssistantAgent(
    name="MarkdownVerifier",
    model_client=gemini_flash_lite,
    tools=[verify_markdown_content],
    system_message="""
    You are a markdown verifier. 
    Verify the markdown format of the exam provided by the ExamCreator. 
    Use the `verify_markdown_content` tool to check the markdown syntax.
    If there are issues, report them and ask the ExamCreator to fix them.
    If the markdown is correct, say "Markdown is correct".
    If the Reviewer has approved the exam, do not perform any verification.
    """
)
