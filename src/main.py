import asyncio
from team.math_team import math_team
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult

async def main():
    task = "What is the distance a freely falling object covers in the first 5 seconds? Assume acceleration due to gravity is standard."
    try:
        team = math_team()
        async for message in team.run_stream(task=task):
            print("-"*40)
            if isinstance(message,TextMessage):
                print(f"{message.source} : {message.content}")
            elif isinstance(message,TaskResult):
                print("-"*40)
                print(f"TERMINATION REASON : {message.stop_reason}")

    except Exception as e:
        print(f"Error {str(e)}")
    finally:
        print("Task Completed")

if __name__ == "__main__":
    asyncio.run(main())
