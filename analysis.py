'''
This module should take care of analyzing the data provided by the data loader 
and tells the amount of stock to buy or sell
''' 
import talib
from pandas import DataFrame
from typing import Tuple, Dict
from execution_type import Execution

Transaction = Tuple[Execution, int]

def analysis(data: DataFrame) -> Dict[str, Transaction]:
    pass