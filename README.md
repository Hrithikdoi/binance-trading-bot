# Binance Trading Bot

An automated cryptocurrency trading bot that interacts with the Binance API to execute trades based on predefined trading strategies.

## Overview

This project is a simple algorithmic trading bot built to demonstrate how automated trading systems can interact with cryptocurrency exchanges.  
The bot connects to the Binance API, retrieves real-time market data, and executes trades based on predefined logic.

The goal of this project is to understand how automated trading works and how APIs can be used to interact with financial platforms.

## Features

- Automated cryptocurrency trading
- Binance API integration
- Real-time market data monitoring
- Strategy-based trade execution
- Customizable configuration
- Logging for executed trades

## Technologies Used

- Python
- Binance API
- REST APIs
- JSON
- Python libraries (requests, etc.)

## Project Structure

```
binance-trading-bot/
│
├── bot.py
├── config.py
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Hrithikdoi/binance-trading-bot.git
```

Navigate to the project directory:

```bash
cd binance-trading-bot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Add your Binance API credentials in the configuration file or environment variables.

```
BINANCE_API_KEY=your_api_key
BINANCE_SECRET_KEY=your_secret_key
```

⚠️ Never share your API keys publicly.

## Running the Bot

Run the trading bot using:

```bash
python bot.py
```

The bot will connect to Binance and begin monitoring market conditions based on the defined strategy.

## Disclaimer

This project is for **educational purposes only**. Cryptocurrency trading involves financial risk.  
Always test strategies carefully before using real funds.

## Future Improvements

- Add technical indicators (RSI, MACD, Moving Averages)
- Implement better risk management
- Add backtesting functionality
- Create a dashboard for monitoring trades
