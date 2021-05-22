data = {
    "address": "0x544444444444",
    "ETH": {
        "balance": 444,
        "totalIn": 444,
        "totalOut": 4
    },
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 0
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 0
        }
    ]
}
print(data)
print('Вывести списки ключей и значений словаря', data.keys())
print('Вывести списки ключей и значений словаря', data.values())
data['ETH'].update({'total_diff': 100})
print('В “ETH” добавить ключ “total_diff” со значением 100', data)
data["tokens"][0]['fst_token_info']['name'] = 'doge'

print('Внутри “fst_token_info” значение ключа “name” поменять с “fdf” на “doge”', data['tokens'][0]['fst_token_info']['name'])

data['ETH']['totalOut'] = data['tokens'][1]['total_out']
del data['tokens'][1]['total_out']
del data['tokens'][0]['total_out']
print('Удалить “total_out” из tokens и присвоить его значение в “total_out” внутри “ETH”', data['ETH'],'\n', data['tokens'])
print()

data['tokens'][1]['sec_token_info']['TOTAL_PRICE'] = data['tokens'][1]['sec_token_info'].pop('price')
print('Внутри "sec_token_info" изменить название ключа “price” на “total_price', data['tokens'][1]['sec_token_info'])