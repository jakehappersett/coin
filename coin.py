import coinmarketcap
import beautifultable 
#import json
#import pprint
#import reddit

market = coinmarketcap.Market()
names = ["ethereum", "bitcoin", "ripple"]
ammount = [.5, .5, 50]
value = []


#calculate values 
for name in names:
    out = market.ticker(name)
    t = float(out[0]['price_usd']) * ammount[names.index(name)]
    value.append(t)

total = sum(value)
#format and print data 
#print("coin --- price --- owned --- value")
#for name in names:
#    out = market.ticker(name)
#    print( "\n", out[0]['symbol'],  " --- " , out[0]['price_usd'], " --- ", total[names.index(name)], " --- ", value[names.index(name)])


#create and format table
table = beautifultable.BeautifulTable()
table.column_headers=["coin", "price", "owned", "value"]
for name in names: 
    out = market.ticker(name)
    table.append_row([out[0]['symbol'],out[0]['price_usd'],ammount[names.index(name)],value[names.index(name)]])

table.append_row(["","","total",'${:,.2f}'.format(total)])

print(table)    
