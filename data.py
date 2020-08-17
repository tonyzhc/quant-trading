# This file should take care of periodic data extraction from Yahoo Finance
import os
import sys
import json
import logging
import time
from threading import Thread
import socket
import yfinance
import talib
from config import LOG_FILE, LOCALHOST_PORT

class Trader:
    shutdown = False
    threads = []

    def __init__(self):
        """
        Starts the trading thread and listening thread
        Thread runs until self.shutdown == True
        User can shutdown server by python3 server_shutdown.py
        """
        os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
        logging.basicConfig(
                    filename=LOG_FILE,
                    filemode='w',
                    level=logging.INFO
                )
        try:
            self.threads.append(Thread(target=self.start_trading_process))
            self.threads.append(Thread(target=self.listen_commands))

            for thread in self.threads:
                thread.start()
            for thread in self.threads:
                thread.join()

        except Exception as e:
            logging.error(str(e))

    def listen_commands(self):
        """
        Listens for commands on localhost port 6000
        """
        udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        udp_sock.bind(("localhost", LOCALHOST_PORT))

        udp_sock.settimeout(1)

        while True:
            logging.info('Listening for commands...')
            time.sleep(0.1)

            if self.shutdown:
                udp_sock.close()
                logging.info('Listen thread shutting down')
                return

            try:
                data, _ = udp_sock.recvfrom(4096)
            except socket.timeout:
                continue

            # Decode list-of-byte-strings to UTF8 and parse JSON data
            try:
                message_dict = json.loads(data.decode("utf-8"))
            except json.JSONDecodeError:
                continue

            if 'signal' in message_dict.keys() and \
                    message_dict['signal'] == 'shutdown':
                        self.shutdown = True

    def start_trading_process(self):
        """
        This function runs analysis algorithm continuously
        """
        while not self.shutdown:
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

if __name__ == "__main__":
    Trader()
