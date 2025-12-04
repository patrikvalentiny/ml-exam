import asyncio
from autogen_agentchat.ui import Console
from autogen_agentchat.teams import SelectorGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from src.models.gemini import gemini_flash
from typing import Literal

from src.agents.planner import planner
from src.agents.exam_creator import exam_creator
from src.agents.markdown_verifier import markdown_verifier
from src.agents.reviewer import reviewer


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
