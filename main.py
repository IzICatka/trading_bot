import ccxt
import time

exchange = ccxt.binance()
symbol = 'ETH/USDT'
timeframe = '1m'

# Получаем последнюю цену ETHUSDT с биржи Binance
def get_last_price():
    ticker = exchange.fetch_ticker(symbol)
    return ticker['last']

# Определяем изменение цены на 1% за последний час
def check_price_change(last_price, previous_price):
    change_percentage = (last_price - previous_price) / previous_price * 100
    if abs(change_percentage) >= 1:
        print(f"Price change: {change_percentage:.2f}%")

# Сохраняем цену каждую минуту и проверяем изменение цены за последний час
previous_price = get_last_price()

while True:
    current_price = get_last_price()
    check_price_change(current_price, previous_price)
    previous_price = current_price
    time.sleep(60)