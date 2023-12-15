# DFKQuestCostTracker
An API that show the breakeven gwei price for quests in the DeFi Kingdoms web3 game

This application takes into account various factors such as the expected value of loot drops (base rate) and gas costs

Powered by FastAPI

## Setup

```bash 
# From source
git clone https://github.com/xxlongzaixx/DFKQuestCostTracker.git
cd DFKQuestCostTracker

# Create a virtual environment
python -m venv venv

# Activate your virtual environment 
.\venv\Scripts\activate

# Install the dependencies to your virtual environment
pip install -r requirements.txt
```

## Usage
```bash
# Start API server
python main.py
```

Go to:

- API GET:
  - http://localhost:8000/api/v1/quest-cost-breakeven
