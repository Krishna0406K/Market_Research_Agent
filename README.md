# Market Research Agent 🚀

An AI-powered market research and business analysis system built with [crewAI](https://crewai.com). This multi-agent system conducts comprehensive market research, competitive analysis, customer insights, and product strategy development for any AI product idea.

## Overview

Market Agent orchestrates five specialized AI agents that work together to analyze market opportunities and generate investor-ready business reports. Each agent brings domain expertise and collaborates sequentially to build a complete picture of your product's market potential.

### The Agent Team

1. **Market Research Specialist** - Analyzes market size, growth trends, and industry dynamics
2. **Competitive Intelligence Analyst** - Identifies competitors and uncovers market gaps
3. **Customer Insights Researcher** - Develops customer personas and pain point analysis
4. **Product Strategy Advisor** - Designs MVP features and product roadmap
5. **Business Analyst** - Synthesizes findings into pricing strategy and investment thesis

## Features

- Automated market sizing (TAM, SAM, SOM)
- Competitive landscape mapping
- Customer segmentation and persona development
- MVP feature prioritization
- Pricing strategy recommendations
- Financial projections and revenue modeling
- Risk analysis and go/no-go recommendations
- Professional markdown reports ready for stakeholders

## Prerequisites

- Python >=3.10, <3.14
- [UV](https://docs.astral.sh/uv/) package manager
- API keys for:
  - Google Gemini (for AI agents)
  - SerperDev (for web search)

## Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd market_agent
```

2. Install UV if you haven't already:
```bash
pip install uv
```

3. Install dependencies:
```bash
crewai install
```

4. Set up environment variables:
Create a `.env` file in the root directory:
```env
GOOGLE_API_KEY=your_google_api_key_here
SERPER_API_KEY=your_serper_api_key_here
```

## Usage

### Quick Start

Run the market analysis with the default product idea:
```bash
crewai run
```

Or use the Python entry point:
```bash
python -m market_agent.main
```

### Custom Product Analysis

Edit `src/market_agent/main.py` to analyze your own product idea:

```python
inputs = {
    "product_idea": "Your AI product idea description here"
}
```

### Output

The system generates a comprehensive business report at `reports/report.md` containing:
- Executive summary
- Market research findings
- Competitive analysis
- Customer insights
- Product strategy
- Pricing recommendations
- Financial projections
- Final go/no-go recommendation

## Project Structure

```
market_agent/
├── src/market_agent/
│   ├── config/
│   │   ├── agents.yaml      # Agent configurations
│   │   └── tasks.yaml       # Task definitions
│   ├── tools/               # Custom tools
│   ├── crew.py             # Crew orchestration
│   └── main.py             # Entry point
├── reports/                # Generated reports
├── knowledge/              # Knowledge base
├── .env                    # Environment variables
└── pyproject.toml         # Project dependencies
```

## Configuration

### Agents

Customize agent behavior in `src/market_agent/config/agents.yaml`. Each agent has:
- Role and expertise
- Goals and objectives
- Backstory and experience

### Tasks

Modify research tasks in `src/market_agent/config/tasks.yaml`. Each task defines:
- Detailed instructions
- Expected output format
- Context dependencies
- Assigned agent

### Tools

The system uses these crewAI tools:
- `SerperDevTool` - Web search capabilities
- `ScrapeWebsiteTool` - Website content extraction
- `SeleniumScrapingTool` - Dynamic web scraping

Add custom tools in `src/market_agent/tools/`.

## Available Commands

```bash
# Run the crew
crewai run
# or
market_agent

# Train the crew (if training data available)
train

# Replay a specific task
replay

# Run tests
test
```

## Example Use Cases

- Validating startup ideas before building
- Conducting competitive research for product launches
- Generating investor pitch materials
- Market entry strategy development
- Product-market fit analysis
- Pricing strategy optimization

## Development

### Adding New Agents

1. Define the agent in `config/agents.yaml`
2. Create the agent method in `crew.py`:
```python
@agent
def your_agent(self) -> Agent:
    return Agent(
        config=self.agents_config["your_agent"],
        tools=toolkit
    )
```

### Adding New Tasks

1. Define the task in `config/tasks.yaml`
2. Create the task method in `crew.py`:
```python
@task
def your_task(self) -> Task:
    return Task(
        config=self.tasks_config["your_task"],
        context=[self.previous_task()]
    )
```

## Limitations

- Requires active internet connection for web research
- API rate limits apply based on your service plans
- Analysis quality depends on available online information
- Generated reports require human review and validation

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

This project is provided as-is for educational and commercial use.

## Support

For questions about crewAI:
- [crewAI Documentation](https://docs.crewai.com)
- [crewAI GitHub](https://github.com/joaomdmoura/crewai)
- [crewAI Discord](https://discord.com/invite/X4JWnZnxPb)

## Acknowledgments

Built with [crewAI](https://crewai.com) - the leading framework for orchestrating role-playing, autonomous AI agents.
