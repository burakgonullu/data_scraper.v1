import time
import yfinance as yf

while True:
    btc_historical = yf.download("BTC-USD", period="1d", interval="1m")
    print(btc_historical)

    time.sleep(60)
