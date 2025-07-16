from models.openai_model import get_model
from tools.wikipedia_tool import web_search_tool
from config.prompts import WIKIPEDIA_SYSTEM_PROMPT
from autogen_agentchat.agents import AssistantAgent

def get_wikipedia_agent():
    wikipedia_agent = AssistantAgent(
        name="Web_Search",
        model_client=get_model(),
        system_message=WIKIPEDIA_SYSTEM_PROMPT,
        tools=[web_search_tool],
        reflect_on_tool_use=True
    )
    return wikipedia_agent