import requests



#Сделать запрос API
def get_info():
    response = requests.get(url="https://yobit.net/api/3/info")

#Записать полученную информацию в файл
    with open("info.txt", "w") as file:
        file.write(response.text)

    return response.text




#Cделать запрос информации о цене ETHUSDT(?ignore_invalid=1 нужно для избежания ошибки при неверном запросе)
def get_ticker(coin1="eth", coin2="usdt"):
    response = requests.get(url=f"https://yobit.net/api/3/ticker/{coin1}_{coin2}?ignore_invalid=1")

#Записать полученную информацию в файл
    with open("ticker.txt", "w") as file:
        file.write(response.text)

    return response.text



#Сделать запрос информации о выставленных на покупку ордерах
def get_depth(coin1="eth", coin2="usdt", limit=150):
    response = requests.get(url=f"https://yobit.net/api/3/depth/{coin1}_{coin2}?limit={limit}&ignore_invalid=1")

#Записать полученную информацию в файл
    with open("depth.txt", "w") as file:
        file.write(response.text)

#Подсчитать цену и колличество монет
    bids = response.json()[f"{coin1}_usdt"]["bids"]

    total_bids_amount = 0
    for item in bids:
        price = item[0]
        coin_amount = item[1]

        total_bids_amount += price * coin_amount

#Подсчитать общую стоимость для закупки
    return f"Total bids: {total_bids_amount} "




#Сделать запрос информации о совершённых покупках и продажах
def get_trades(coin1="eth", coin2="usdt", limit=150):
    response = requests.get(url=f"https://yobit.net/api/3/trades/{coin1}_{coin2}?limit={limit}&ignore_invalid=1")

#Записать полученную информацию в файл
    with open("trades.txt", "w") as file:
        file.write(response.text)

#Создать две переменные с значениями покупки и продажи
    total_trade_ask = 0
    total_trade_bid = 0


#Когда монету пампят, её активно закупают, следовательно type_bid растёт.
#Подсчитать общую сумму проданных и купленных монет.
    for item in response.json()[f"{coin1}_{coin2}"]:
        if item["type"] == "ask":
            total_trade_ask += item["price"] * item["amount"]
        else:
            total_trade_bid += item["price"] * item["amount"]

    info = f"[-] TOTAL {coin1} SELL: {round(total_trade_ask, 2)} $\n[+] TOTAL {coin1} BUY: {round(total_trade_bid, 2)} $"

    return info




#Вызвать нужную функцию 
def main():
    #print(get_info())
    #print(get_ticker())
    #print(get_depth())
    print(get_trades())

if __name__ == '__main__':
    main()












