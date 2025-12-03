from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create a custom config
config = DEFAULT_CONFIG.copy()
config["deep_think_llm"] = "gpt-5"  # Use a different model
config["quick_think_llm"] = "gpt-5"  # Use a different model
config["max_debate_rounds"] = 5  # Increase debate rounds

# Configure data vendors (default uses yfinance and alpha_vantage)
config["data_vendors"] = {
    "core_stock_apis": "yfinance",  # Options: yfinance, alpha_vantage, local
    "technical_indicators": "yfinance",  # Options: yfinance, alpha_vantage, local
    "fundamental_data": "alpha_vantage",  # Options: openai, alpha_vantage, local
    "news_data": "alpha_vantage",  # Options: openai, alpha_vantage, google, local
}

# Initialize with custom config
ta = TradingAgentsGraph(
    selected_analysts=["market", "social", "news", "fundamentals"],
    debug=True,
    config=config,
)

# forward propagate
_, decision = ta.propagate("NVDA", "2025-11-11")
print(decision)

# Memorize mistakes and reflect
# ta.reflect_and_remember(1000) # parameter is the position returns
