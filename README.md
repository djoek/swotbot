# SWOTbot

![swot](https://i.makeagif.com/media/6-30-2015/CSxye-.gif)

SWOTbot is an AI-powered tool that generates comprehensive SWOT (Strengths, Weaknesses, Opportunities, Threats) analyses for your project outlines. 
It uses AI agents to analyse your project description and provide professional, factual, and straightforward insights.

This is not intended as a production tool. It's a fun little tool that demos the possibilities of agentic AI using https://www.agno.com/

## Example

in the `examples/` folder you can read what SWOTbot wrote about itself.


## Setup Instructions

### Prerequisites

- Python 3.13 or higher
- uv package manager
- API keys for Mistral AI and Tavily


### API Key Configuration

SWOTbot uses two APIs to function at its best:

1. **Mistral AI API Key**: Used for the language model that powers the analysis
2. **Tavily API Key**: (optionally) Used for web searches to validate findings

you can set your env variables in the usual way, or create a `.env` file where you run swotbot with the following content:

```
MISTRAL_API_KEY=your_mistral_api_key
TAVILY_API_KEY=your_tavily_api_key
```

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/djoek/swotbot.git
   cd swotbot
   ```

## Usage

To run SWOTbot, execute the main.py script:

```bash
uv run swotbot
```

Follow the instructions. In the end, you can save the file by asking.  To end, just type `exit`

