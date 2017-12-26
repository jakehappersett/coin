import coinmarketcap
import beautifultable 
import json
#import pprint
#import reddit

with open('coinconfig.json', 'r') as fp:
    obj = json.load(fp)


market = coinmarketcap.Market()
names = list(obj.keys())
ammount = []
value = []

#calculate ammounts
for name in names:
    a = float(obj[name]['ammount'])
    ammount.append(a)


#calculate values 
for name in names:
    out = market.ticker(name)
    t = float(out[0]['price_usd']) * ammount[names.index(name)]
    value.append(t)

total = sum(value)

#create and format table
table = beautifultable.BeautifulTable()
table.column_headers=["coin", "price", "owned", "value"]
for name in names: 
    out = market.ticker(name)
    table.append_row([out[0]['symbol'],out[0]['price_usd'],ammount[names.index(name)],value[names.index(name)]])

table.append_row(["","","total",'${:,.2f}'.format(total)])

print(table)    
