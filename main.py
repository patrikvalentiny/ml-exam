import asyncio
from autogen_agentchat.ui import Console
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination

from src.agents.planner import planner
from src.agents.exam_creator import exam_creator
from src.agents.markdown_verifier import markdown_verifier
from src.agents.reviewer import reviewer
from src.agents.saver import saver
from src.task import task_description_sk


async def main():
    termination = TextMentionTermination("TERMINATE")

    team = RoundRobinGroupChat(
        [planner, exam_creator, markdown_verifier, reviewer, saver],
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
