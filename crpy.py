import time, random
from javascript import require
lCh=[]; lSt=[];
tv=require('@mathieuc/tradingview')
# print(tv)
c=tv.Client(); time.sleep(1)
ch = c.Session.Chart()
print(ch)
lCh.append(ch)
ch.setMarket('BINANCE:BTCUSDT', { 'timeframe': '15' }); time.sleep(1)
arCo=['BINANCE:BTCUSDT', 'BINANCE:ETHUSDT']
lim=3; tf='15';
arCo=['BINANCE:BTCUSDT', 'BINANCE:ETHUSDT', 'BINANCE:SOLUSDT', 'BINANCE:XRPUSDT', 'BINANCE:BNBUSDT', 'BINANCE:ADAUSDT', 'BINANCE:LINKUSDT', 'BINANCE:XLMUSDT', 'BINANCE:BCHUSDT', 'BINANCE:LTCUSDT', 'BINANCE:UNIUSDT', 'BINANCE:AAVEUSDT']; random.shuffle(arCo)
lSt.append('PUB;ut1T8n2nhY3cjgArO4iFqk4n0M9ssI1d')		# ZigZag++ by DevLucem
lSt.append('STD;Zig_Zag')
arB=[]
for i1 in range(0, len(lSt) - 1, 2):
	std=lSt[i1]; std2=lSt[i1 + 1]
	ch = c.Session.Chart()
	ch.setMarket('BINANCE:BTCUSDT', { 'timeframe': tf }); time.sleep(1)
	z =tv.getIndicator(std, 'last'); z2=tv.getIndicator(std2, 'last'); time.sleep(1)
print([z.description, z2.description])
# with open('hello.txt', 'w') as f:
# 	f.write('Hello World from Python script!')
# print("File written successfully")
