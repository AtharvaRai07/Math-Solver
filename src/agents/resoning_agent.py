from models.openai_model import get_model
from config.prompts import REASONING_SYSTEM_PROMPT
from autogen_agentchat.agents import AssistantAgent

def get_reasoning_agent():
    reasoning_agent = AssistantAgent(
        name="Reasoner",
        model_client=get_model(),
        system_message=REASONING_SYSTEM_PROMPT
    )
    return reasoning_agent