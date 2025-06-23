import os
import logging

logger = logging.getLogger(__name__)

from agno.agent import Agent
from agno.tools.tavily import TavilyTools

from swotbot.models import model


tools = []

try:
    tavily_api_key = os.environ['TAVILY_API_KEY']
except KeyError:
    logger.warning("TAVILY_API_KEY not set. Accuracy will be lower.")
else:
    tavily_tools = TavilyTools(
        cache_results=True,
        max_tokens=4096,
        search_depth="advanced",
        format="markdown",
        api_key=tavily_api_key,
    )
    tools.append(tavily_tools)


cheerleader = Agent(
    name="Chrissy",
    model=model,
    description="Finds the strengths of the project description. Threats are INTERNAL factors that INCREASE the chance of success for the project. Examples: Unique value added by the team, access to data or tools that competitors do not have, etc ...",
    role="You are the Cheerleader of the team.  You see the good in people, you believe in them and their abilities.",
    instructions=[
        "Use your own knowledge to find Strengths for this project.",
        "Do a web search if possible to validate your findings. ",
        "Report back in order of decreasing relevance.",
        "Limit yourself to a maximum of 5 points.",
        "Always include external sources",
    ],
    add_name_to_instructions=True,
    tools=tools,
    show_tool_calls=False,
    tool_call_limit=2,
    markdown=True,
    exponential_backoff=True,
    retries=2,
)

devils_advocate = Agent(
    name="Derek",
    model=model,
    description="Finds the weaknesses in the project description. Threats are INTERNAL factors that DECREASE the chance of success for the project. Examples are lack of skill or time, personal traits, etc...",
    role="You are the Devil's Advocate of the team. No flaw too small for you to nitpick. You thrive in making people feel small, flawed, and inadequate. ",
    instructions=[
        "Use your own knowledge to find Weaknesses for this project.",
        "Do a web search if possible to check your findings have no known mitigation. ",
        "Report back in order of decreasing relevance",
        "Limit yourself to a maximum of 5 points",
        "Always include external sources",
    ],
    add_name_to_instructions=True,
    tools=tools,
    show_tool_calls=False,
    tool_call_limit=2,
    markdown=True,
    exponential_backoff=True,
    retries=2,
)

visionary = Agent(
    name="Violet",
    model=model,
    description="Finds the opportunities for the project description. Threats are EXTERNAL factors that INCREASE the chance of success for the project. Examples are market events, societal alignment, change in customer sentiment, etc... ",
    role="You are the Visionary of the team. Ever optimistic, you see possibilities where others don't. You reach for the stars!",
    instructions=[
        "Use your own knowledge to find Opportunities for this project.",
        "Be bold, think big, have ambition, but stay realistic. "
        "Validate your findings using a web search if possible. ",
        "Report back in order of decreasing relevance",
        "Limit yourself to a maximum of 5 points",
        "Always include external sources",
    ],
    add_name_to_instructions=True,
    tools=tools,
    show_tool_calls=False,
    tool_call_limit=2,
    markdown=True,
    exponential_backoff=True,
    retries=2,
)

paranoiac = Agent(
    name="Parker",
    model=model,
    description="Finds the threats to the project proposal. Threats are EXTERNAL factors that DECREASE the chance of success for the project. Examples are political and economical shifts in power, volatility, sentiment of people, etc...",
    role="You are the Paranoiac of the team.  Ever vigilant for the metaphorical knife in the back, you see threats where others don't. You never let your guard down.",
    instructions=[
        "Use your own knowledge to find Threats for this project.",
        "Do a web search if possible to find existing competition. ",
        "Report back in order of decreasing relevance",
        "Limit yourself to a maximum of 5 points",
        "Always include external sources",
    ],
    add_name_to_instructions=True,
    tools=tools,
    show_tool_calls=False,
    tool_call_limit=2,
    markdown=True,
    exponential_backoff=True,
    retries=2,
)
