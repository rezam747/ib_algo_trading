import threading 
import numpy as np
import time 

from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
import time
import threading

class TradingApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

    def historicalData(self, reqId, bar):
        print("HistoricalData. ReqId:", reqId, "BarData.", bar)
    

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


tickers = ["AAPL", "MSFT", "TSLA"]

for ticker in tickers : 
    histData(tickers.index(ticker), usTechSTK(ticker), '5 M', '5 mins' )


time.sleep(10)