import ccxt
import requests
import json

# para = {
#     'apiKey': 'WFUhgamf9cjOgCGUwpRVoFM0byn4TzCUdhdDQU',
#     'secret': 'z90Wf2qUR7M6hLbgr0DuqvbnjlfPLxLl1jfCOpZtk1jZtyZMC',
#     'timeout': 30000,# # spot:��ȡbnb�����
#     'enableRateLimit': True,# bnb_balance = binance.fetch_balance()['total']['BNB']
# }# print(bnb_balance)


para = {
    'apiKey': 'fc',
    'secret': '24AA9D2E0',
    'password': 'Sas1.',
    'timeout': 30000,
    'enableRateLimit': True,
}
# binance = ccxt.binance(para)

binance = ccxt.okex(para)
# # spot����ȡeth�����
eth_balance = binance.fetch_balance()['total']['ETH']
print(eth_balance)

# # spot���м��µ� ETH ����20USDT
# try :
#     binance.create_market_buy_order('ETH/USDT', 20)
# except Exception as e:
#     print(e)

# # spot:���޼۵����۸�1200usdt������20USDT��ETH
# try:
#     binance.create_limit_buy_order('ETH/USDT', 20, 1200)
# except Exception as e:
#     print(e)

# ���ñҰ�������Ϊ������Լ ��set exchange.options['defaultType'] to 'spot', 'margin', 'delivery' or 'future'
# binance.options['efaultType'] = 'future'


# ��ȡ�Ұ���������������Լ�Ľ��׶�
# res = binance.load_markets()
# res['BTC/USDT']



# future����ȡ������Լ�Ľ��׶�
# binance.symbols


# future:��ȡusdt���
# binance.fetch_balance()['USDT']['free']

# future:�µ�ETHUSDT������Լ���۸����мۡ�������1�š�����������
# try:
#     binance.create_order('ETH/USDT', 'market', 'buy', 1)
# except Exception as e:
#     print(e)
#
# # future:�µ�ETHUSDT������Լ���۸����޼ۡ�������1�š����������롢�۸���1000
# try:
#     binance.create_order('ETH/USDT', 'limit', 'buy', 1, 1000)
# except Exception as e:
#     print(e)


def getFearInfo():
    try :
        fearInfo = requests.get('https://history.btc123.fans/zhishu/api.php')
        content = fearInfo.text
        json_dict = json.loads(content)
        fearValue = int(json_dict['data'][-1]['value'])
        print(fearValue)
    except Exception as e :
        print(e)
        return e
    return fearValue


def buy():
    USDT_balance = binance.fetch_balance()['total']['USDT']
    print(USDT_balance)
    buy_USDT_vavlue = 20

    if USDT_balance >= buy_USDT_vavlue :
        ticker = binance.fetch_ticker(symbol="ETH/USDT")
        price_last = ticker["last"]
        buy_eth_amount = buy_USDT_vavlue / price_last
        try :
              binance.create_market_buy_order('ETH/USDT', buy_eth_amount)
        except Exception as e:
              print(e)

import time

def test_run():

    while True:
        try:
             _fearInfo = getFearInfo()
             if(_fearInfo <= 23) :
                 buy()
        except Exception as e:
            print(e)

        time.sleep(10)



if __name__ == '__main__':
    test_run()