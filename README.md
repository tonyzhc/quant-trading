# quant-trading

Plan of attack for now:
1. Periodically pull data from yahoo finance
2. Run data through TA-lib and get pattern for bullish/bearish
3. Set threshold and decide to buy or sell
4. Execute the transactions; for now, just keep track record

## Installation

Requires 
- [yfinance](https://github.com/ranaroussi/yfinance) 
- [TA-Lib](https://ta-lib.org/) and its [Python wrapper](https://github.com/mrjbq7/ta-lib). See [dependency](https://github.com/mrjbq7/ta-lib#dependencies) and [installation](https://github.com/mrjbq7/ta-lib#installation) under the GitHub repo. IMPORTANT: install dependencies first, then run `pip install talib`.

## Usages

To start the server, run
```
python3 data.py
```

To stop the server, run
```
python3 server_shutdown.py
```

To see server logs, run
```
tail -f logs/trading-log
```
