# This file should take care of periodic data extraction from Yahoo Finance
import os
import sys
import logging
import time
import yfinance
import talib
from config import LOG_FILE

def start_trading_process():
    """
    This function runs analysis algorithm continuously
    """
    while True:
        try:
            # get stock data
            logging.info('GETTING STOCK DATA')
            data = yfinance.download(
                       tickers = 'SPY',
                       period='1d',
                       interval='1m',
                   )

            # TODO: call talib
            # TODO: analysis
            # TODO: record trade results
            logging.info('SUCCESSFULLY GOT STOCK DATA')
            time.sleep(1)
        except Exception as e:
            raise e

def main():
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    logging.basicConfig(
                filename=LOG_FILE,
                filemode='w',
                level=logging.INFO
            )
    try:
        start_trading_process()
    except Exception as e:
        logging.ERROR(str(e))

if __name__ == "__main__":
    main()
