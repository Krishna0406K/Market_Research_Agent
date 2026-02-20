# Market Agent 🚀

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![crewAI](https://img.shields.io/badge/crewAI-1.9.3-purple.svg)](https://crewai.com)
[![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

An AI-powered market research and business analysis system built with [crewAI](https://crewai.com). This multi-agent system conducts comprehensive market research, competitive analysis, customer insights, and product strategy development for any AI product idea.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Available Commands](#available-commands)
- [Example Use Cases](#example-use-cases)
- [Web Interface Features](#web-interface-features)
- [Development](#development)
- [Limitations](#limitations)
- [Support](#support)

## 📚 Additional Documentation

- **[Quick Start Guide](QUICKSTART.md)** - Get up and running in 5 minutes
- **[Demo Walkthrough](DEMO.md)** - See a complete example analysis
- **[Feature Overview](FEATURES.md)** - Detailed feature descriptions
- **[Troubleshooting](TROUBLESHOOTING.md)** - Common issues and solutions

## Overview

Market Agent orchestrates five specialized AI agents that work together to analyze market opportunities and generate investor-ready business reports. Each agent brings domain expertise and collaborates sequentially to build a complete picture of your product's market potential.

### The Agent Team

1. **Market Research Specialist** - Analyzes market size, growth trends, and industry dynamics
2. **Competitive Intelligence Analyst** - Identifies competitors and uncovers market gaps
3. **Customer Insights Researcher** - Develops customer personas and pain point analysis
4. **Product Strategy Advisor** - Designs MVP features and product roadmap
5. **Business Analyst** - Synthesizes findings into pricing strategy and investment thesis

## Features

- 🎨 **Beautiful Web Interface** - Marketing-themed Streamlit UI with gradient designs
- 🔑 **Easy API Configuration** - Enter API keys directly in the UI or use .env file
- 📥 **Word Document Export** - Download reports as formatted .docx files
- 🤖 **Five Specialized AI Agents** - Each with domain expertise
- 📊 **Real-time Progress Tracking** - Watch your agents work
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

**Quick Start:** See [QUICKSTART.md](QUICKSTART.md) for a 5-minute setup guide.

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
# or
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the root directory:
```env
GOOGLE_API_KEY=your_google_api_key_here
SERPER_API_KEY=your_serper_api_key_here
```

**Alternative:** You can also configure API keys directly in the web interface sidebar.

## Usage

### Web Interface (Recommended)

Launch the beautiful Streamlit web interface:
```bash
streamlit run app.py
```

The web interface provides:
- 🎨 Beautiful marketing-themed UI
- 📝 Easy product idea input
- 📊 Real-time progress tracking
- 📥 One-click Word document download
- 📄 In-browser report preview

![Market Agent UI](https://via.placeholder.com/800x400/667eea/ffffff?text=Market+Agent+AI+Interface)

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
├── app.py                  # Streamlit web interface ⭐
├── run_app.bat            # Quick launch script (Windows)
├── run_app.sh             # Quick launch script (Mac/Linux)
├── QUICKSTART.md          # 5-minute setup guide
├── TROUBLESHOOTING.md     # Common issues and solutions
├── .env.example           # Environment variables template
├── .streamlit/
│   └── config.toml        # Streamlit theme configuration
├── src/market_agent/
│   ├── config/
│   │   ├── agents.yaml      # Agent configurations
│   │   └── tasks.yaml       # Task definitions
│   ├── tools/               # Custom tools
│   ├── crew.py             # Crew orchestration
│   └── main.py             # CLI entry point
├── reports/                # Generated reports (Word & Markdown)
├── knowledge/              # Knowledge base
├── .env                    # Environment variables (create this)
├── requirements.txt        # Python dependencies
└── pyproject.toml         # Project configuration
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
# Launch web interface (recommended)
streamlit run app.py
# or on Windows
run_app.bat

# Run via command line
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

## Web Interface Features

The Streamlit frontend provides an intuitive, beautiful interface with:

### Design
- 🎨 Modern gradient theme with purple/blue marketing colors
- 📱 Responsive layout that works on all devices
- 🎯 Clean, professional design suitable for presentations

### Functionality
- **API Key Configuration**: Enter keys directly in the sidebar (no .env file needed)
- **Product Idea Input**: Large text area for detailed product descriptions
- **Agent Showcase**: Visual representation of all 5 AI agents
- **Real-time Progress**: Progress bar and status updates during analysis
- **Report Preview**: In-browser markdown rendering of the full report
- **Export Options**: 
  - Download as formatted Word document (.docx)
  - Download as Markdown (.md)
- **Report History**: Access previously generated reports

### User Experience
- One-click analysis start
- Clear error messages and validation
- Helpful tooltips and guidance
- Professional report formatting in Word with:
  - Custom headers and styling
  - Color-coded sections
  - Proper document structure
  - Branded title page

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

**Having issues?** Check the [TROUBLESHOOTING.md](TROUBLESHOOTING.md) guide.

For questions about crewAI:
- [crewAI Documentation](https://docs.crewai.com)
- [crewAI GitHub](https://github.com/joaomdmoura/crewai)
- [crewAI Discord](https://discord.com/invite/X4JWnZnxPb)

## Acknowledgments

Built with [crewAI](https://crewai.com) - the leading framework for orchestrating role-playing, autonomous AI agents.
