# Binance Futures Testnet Trading Bot

## Overview

This project is a simplified Python trading bot that places orders on Binance Futures Testnet (USDT-M).
It supports MARKET and LIMIT orders via a command-line interface.

## Features

* Place MARKET and LIMIT orders
* Supports BUY and SELL
* CLI input using Typer
* Input validation
* Structured code (client, orders, validators, CLI)
* Logging of API responses and errors

## Setup

1. Clone the repository

git clone <your-repo-link>
cd trading_bot

2. Create virtual environment

python -m venv venv
venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

4. Add API credentials

Create `.env` file:

API_KEY=your_api_key
API_SECRET=your_secret_key

## Run the Bot

### MARKET order

python cli.py BTCUSDT BUY MARKET 0.002

### LIMIT order

python cli.py BTCUSDT SELL LIMIT 0.002 --price 100000

## Project Structure

trading_bot
│
├── bot
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│
├── cli.py
├── .env
├── requirements.txt
├── README.md

## Logs

Logs are stored in:

bot.log

They include API responses and error messages.
