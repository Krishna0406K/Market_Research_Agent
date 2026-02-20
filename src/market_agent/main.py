
from market_agent.crew import MarketAgent



def run():
    """
    Run the crew.
    """
    inputs = {
        "product_idea": "An AI powered tool that summarizes youtube videos on my channel and posts the summary on various social media platforms like LinkedIn, Instagram, Facebook,X, WhatsApp"
    }

    try:
        MarketAgent().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

