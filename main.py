import asyncio
from pprint import pprint
from src.models.gemini import gemini_flash, gemini_flash_lite, gemini_pro
from autogen_agentchat.ui import Console
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import SelectorGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from src.memory import chroma_memory
from src.tools.markdown_tools import verify_markdown_content
from src.tools.file_tools import save_file
from typing import Literal


def task_description(
    topic: str,
    min: int = 3,
    max: int = 6,
    format: Literal["mix", "multiple-choice", "open-ended"] = "mix",
) -> str:
    formats = {
        "mix": "a mix of multiple-choice and open-ended formats",
        "multiple-choice": "multiple-choice format",
        "open-ended": "open-ended format",
    }

    return f"""
    Create a short exam on the topic of {topic}, including at least {min} and at most {max} questions with {formats[format]}.
    """


def task_description_sk(
    topic: str,
    min: int = 3,
    max: int = 6,
    format: Literal["mix", "multiple-choice", "open-ended"] = "mix",
) -> str:
    formats = {
        "mix": "kombinácia formátov s výberom odpovedí a otvorených otázok",
        "multiple-choice": "formát s výberom odpovedí",
        "open-ended": "formát otvorených otázok",
    }

    return f"""
        Vytvorte krátky test na tému {topic}, ktorý obsahuje najmenej {min} a najviac {max} otázok vo formáte {formats[format]}.
        Nezabudnite zahrnúť kľúč správnych odpovedí na konci testu.
        """


async def main():
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
        """
    )

    exam_creator = AssistantAgent(
        name="ExamCreator",
        model_client=gemini_flash,
        memory=[chroma_memory],
        system_message="""
        You are a short exam creator. 
        Generate concise exam with short questions that can have answers as a list (e.g., multiple choice) or open-ended answers.
        For list answers, provide options labeled A, B, C, D. For open answers, expect a very brief text response.
        Do not fabricate information; base questions on provided context if available.
        Format the answer in a markdown code block.
        Return an answer key after the quiz, for open questions highlight the main points that the answer needs to cover.
        The quiz needs to be in Slovak language.
        """
    )

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
        """
    )

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

    termination = TextMentionTermination("TERMINATE")

    team = SelectorGroupChat(
        [planner, exam_creator, markdown_verifier, reviewer],
        model_client=gemini_flash,
        termination_condition=termination,
    )

    try:
        stream = team.run_stream(task=task_description_sk(topic="moderna"))
        await Console(stream)
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        pass


if __name__ == "__main__":
    asyncio.run(main())
