# SWOTbot

SWOTbot is an AI-powered tool that generates comprehensive SWOT (Strengths, Weaknesses, Opportunities, Threats) analyses for your project outlines. It uses AI agents to analyze your project description and provide professional, factual, and straightforward insights.

## Setup Instructions

### Prerequisites

- Python 3.13 or higher
- API keys for Mistral AI and Tavily


### API Key Configuration

SWOTbot requires two API keys to function properly:

1. **Mistral AI API Key**: Used for the language model that powers the analysis
2. **Tavily API Key**: Used for web searches to validate findings

you can create a `.env` file in the project root with the following content:

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
uv run src/main.py
```

Follow the instructions. In the end, you can save the file by asking.  To end, just type `exit`

