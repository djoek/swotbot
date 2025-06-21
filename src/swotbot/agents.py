import os
import logging

logger = logging.getLogger(__name__)

from agno.agent import Agent
from agno.tools.tavily import TavilyTools

from swotbot.models import mistral_model as model


tools = []

if os.getenv('TAVILY_API_KEY'):
    tavily_tools = TavilyTools(
        cache_results=True,
        max_tokens=1024,
        search_depth="advanced",
        format="markdown",
    )
    tools.append(tavily_tools)


strengths = Agent(
    name="Strengths",
    model=model,
    role="Finds the strengths of the project description",
    instructions=[
        "Use your own knowledge to Strengths for this project.",
        "Do a web search if possible to validate your findings. ",
        "Report back in order of decreasing relevance.",
        "Limit yourself to a maximum of 5 points.",
        "Always include external sources",
    ],
    add_name_to_instructions=True,
    tools=tools,
    show_tool_calls=True,
    tool_call_limit=1,
    markdown=True,
    exponential_backoff=True,
    retries=2,
)

weaknesses = Agent(
    name="Weaknesses",
    model=model,
    role="Finds the weaknesses in the project description",
    instructions=[
        "Use your own knowledge to Weaknesses for this project.",
        "Do a web search if possible to check your findings have no known mitigation. ",
        "Report back in order of decreasing relevance",
        "Limit yourself to a maximum of 5 points",
        "Always include external sources",
    ],
    add_name_to_instructions=True,
    tools=tools,
    show_tool_calls=True,
    tool_call_limit=1,
    markdown=True,
    exponential_backoff=True,
    retries=2,
)

opportunities = Agent(
    name="Opportunities",
    model=model,
    role="Finds the opportunities for the project description",
    instructions=[
        "Use your own knowledge to Opportunities for this project.",
        "Be bold, think big, have ambition, but stay realistic. "
        "Validate your findings using a web search if possible. ",
        "Report back in order of decreasing relevance",
        "Limit yourself to a maximum of 5 points",
        "Always include external sources",
    ],
    add_name_to_instructions=True,
    tools=tools,
    show_tool_calls=True,
    tool_call_limit=1,
    markdown=True,
    exponential_backoff=True,
    retries=2,
)

threats = Agent(
    name="Threats",
    model=model,
    role="Finds the threats to the project proposal",
    instructions=[
        "Use your own knowledge to Threats for this project.",
        "Do a web search if possible to find existing competition. ",
        "Report back in order of decreasing relevance",
        "Limit yourself to a maximum of 5 points",
        "Always include external sources",
    ],
    add_name_to_instructions=True,
    tools=tools,
    show_tool_calls=True,
    tool_call_limit=1,
    markdown=True,
    exponential_backoff=True,
    retries=2,
)
