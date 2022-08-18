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
    
    def error(self, reqId, errorCode, errorString):
        print("Error {} {} {}".format(reqId,errorCode,errorString))

    def contractDetails(self, reqId, contractDetails):
        print("reqID: {}, contract: {}".format(reqId,contractDetails))

def websocket_conn():
    app.run()
    event.wait()
    if event.is_set():
        app.close()

event = threading.Event()
app = TradingApp()
app.connect("127.0.0.1", 7497, clientId=0)


con_thread = threading.Thread(target = websocket_conn)
con_thread.start()
time.sleeo(1)

contract = Contract()
contract.symbol = "AAPL"
contract.secType = "STK"
contract.currency = "USD"
contract.exchange = "SMART"

app.reqContractDetails(100, contract)
time.sleep(5)
event.set()