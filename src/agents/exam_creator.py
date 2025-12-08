from autogen_agentchat.agents import AssistantAgent
from src.models.gemini import gemini_flash
from src.memory import chroma_memory

exam_creator = AssistantAgent(
    name="ExamCreator",
    model_client=gemini_flash,
    memory=[chroma_memory],
    system_message="""
    You are a short exam creator. 
    Generate concise exam with short questions that can have answers as a list (e.g., multiple choice) or open-ended answers.
    For list answers, provide options labeled A, B, C, D make sure they are on new line in markdown, use ('\\'). For open answers, expect a very brief text response.
    Do not fabricate information; base questions on provided context if available.
    Format the answer in a markdown code block.
    Return an answer key after the quiz, for open questions highlight the main points that the answer needs to cover.
    If the Reviewer has approved the exam, do not generate any new content.
    """
)
