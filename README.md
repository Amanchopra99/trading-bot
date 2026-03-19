# Binance Futures Testnet Trading Bot

## Overview

This is a Python-based trading bot that interacts with Binance Futures Testnet (USDT-M).
It allows users to place MARKET and LIMIT orders via a command-line interface.

---

## Features

* Place MARKET and LIMIT orders
* Supports BUY and SELL
* CLI-based input (argparse)
* Input validation
* Structured logging (requests, responses, errors)
* Exception handling (API errors, invalid input)

---

## Project Structure

```
trading_bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│
├── cli.py
├── requirements.txt
├── README.md
```

---

## Setup

1. Clone the repository:

```
git clone https://github.com/Amanchopra99/trading-bot.git
cd trading-bot
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Create a `.env` file:

```
API_KEY=your_api_key
API_SECRET=your_secret_key
```

---

## Usage

### Market Order

```
python3 cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002
```

### Limit Order

```
python3 cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 60000
```

---

## Sample Output

```
ORDER SUCCESS
Order ID: XXXXX
Status: FILLED
Executed Qty: 0.002
Avg Price: XXXXX
```

---

## Assumptions

* Binance Futures Testnet is used
* Minimum notional value (~100 USDT) is respected

---

## Notes

* API keys are stored securely using environment variables
* `.env` file is excluded from version control
