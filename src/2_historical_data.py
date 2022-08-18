import threading 
import numpy as np
import time 

from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
import time
import threading

import pandas as pd

class TradingApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
        self.data = {}

    def historicalData(self, reqId, bar):
        if reqId not in self.data : 
            self.data[reqId] = [{"Date":bar.date, "Open":bar.open, "High":bar.high, "Low":bar.low, "Close":bar.close, "Volume":bar.volume}]
        else:
            self.data[reqId].append({"Date":bar.date, "Open":bar.open, "High":bar.high, "Low":bar.low, "Close":bar.close,"Volume":bar.volume})

        print("reqId:{}, date:{}, open:{}, high:{}, low:{}, close:{}, volume:{}".format(reqId, bar.date, bar.open, bar.high, bar.low, bar.close, bar.volume))

    

def websocket_conn():
    app.run()

app = TradingApp()
app.connect("127.0.0.1", 7497, clientId=1)


con_thread = threading.Thread(target = websocket_conn, daemon = True)
con_thread.start()
time.sleep(1)

def usTechSTK (symbol, sec_type="STK", currency="USD", exchange = "ISLAND"):
    contract = Contract()
    contract.symbol = symbol
    contract.secType = sec_type
    contract.currency = currency
    contract.exchange = exchange
    return contract

def histData(req_num, contract, duration, candle_size):
    app.reqHistoricalData(reqId = req_num,
                        contract = contract,
                        endDateTime = '',
                        durationStr = duration,
                        barSizeSetting = candle_size,
                        whatToShow = 'ADJUSTED_LAST',
                        useRTH = 1,
                        formatDate = 1,
                        keepUpToDate = 0,
                        chartOptions = [] )	


tickers = ["AAPL", "MSFT","AMZN","SPY"]

for ticker in tickers : 
    histData(tickers.index(ticker), usTechSTK(ticker), '1 M', '5 mins' )
    time.sleep(7)


def dataDataFrame(tradeapp_obj, tickers):
    df_dict = {}
    for ticker in tickers :
        df_dict[ticker] = pd.DataFrame(tradeapp_obj.data[tickers.index(ticker)])
        df_dict[ticker].set_index("Date", inplace=True)
    return  df_dict


historicalData = dataDataFrame(app, tickers)


#Adding MACD indicator
from src.indicators import *
MACD_SMA(historicalData["AMZN"])
MACD_EMA(historicalData["AMZN"])
bollBnd(historicalData["AMZN"])
atr(historicalData["AMZN"],n=20)
rsi(historicalData["AMZN"],n=20)
adx(historicalData["AMZN"],n=20)
stochOscltr(historicalData["AMZN"],a=20,b=3)



# bollBnd(historicalData["AMZN"])
atr(historicalData["AMZN"])


app.data




TI_dict = {}
for ticker in tickers :
    TI_dict[ticker] = bollBnd(historicalData[ticker], 20)