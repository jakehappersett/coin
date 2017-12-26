import coinmarketcap
#import json
#import pprint
#import reddit

market = coinmarketcap.Market()
names = ["ethereum", "bitcoin", "ripple"]
total = [.5, .5, 50]
value = []


#calculate values 
for name in names:
    out = market.ticker(name)
    t = float(out[0]['price_usd']) * total[names.index(name)]
    value.append(t)

#format and print data 
print("coin --- price --- owned --- value")
for name in names:
    out = market.ticker(name)
    print( "\n", out[0]['symbol'],  " --- " , out[0]['price_usd'], " --- ", total[names.index(name)], " --- ", value[names.index(name)])

print("\n")


