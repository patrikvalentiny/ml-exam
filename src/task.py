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
