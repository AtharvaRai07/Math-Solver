from models.openai_model import get_model
from config.prompts import CALCULATOR_SYSTEM_PROMPT
from autogen_agentchat.agents import AssistantAgent

def get_calculator_agent():
    calculator_agent = AssistantAgent(
        name="Calculator",
        model_client=get_model(),
        system_message=CALCULATOR_SYSTEM_PROMPT
    )
    return calculator_agent