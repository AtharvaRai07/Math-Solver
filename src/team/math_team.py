from agents.wikipedia_agent import get_wikipedia_agent
from agents.calculator_agent import get_calculator_agent
from agents.resoning_agent import get_reasoning_agent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from config.constant import TEXT_MENTION,MAX_TURNS

def math_team():
    wikipedia_agent = get_wikipedia_agent()
    calculator_agent = get_calculator_agent()
    reasoning_agent = get_reasoning_agent()
    team = RoundRobinGroupChat(
        participants = [wikipedia_agent,calculator_agent,reasoning_agent],
        termination_condition = TextMentionTermination(TEXT_MENTION),
        max_turns=MAX_TURNS
    )
    return team

