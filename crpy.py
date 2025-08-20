import time, random, re
import pandas as pd
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
	if re.findall(r'(?i)ZigZag\+\+',  z.description):  z.setOption('in_10', False)	# !repaint
	if re.findall(r'(?i)ZigZag\+\+', z2.description): z2.setOption('in_10', False)	# !repaint
	s =ch.Study(z); s2=ch.Study(z2); time.sleep(1)
	for cn in arCo:
		ch.setMarket(cn, { 'timeframe': tf }); time.sleep(1)
		for i in range(0, lim):
			v1 = {} if str(type( s.periods[i])) == "<class 'NoneType'>" else  s.periods[i].valueOf()
			v2 = {} if str(type(s2.periods[i])) == "<class 'NoneType'>" else  s2.periods[i].valueOf()
			cc = ch.infos['name'] if str(type(ch.infos['base_currency'])) == "<class 'NoneType'>" else ch.infos['base_currency']
			cc=re.sub('USDT?$', '',cc)
			vv = {**v1, **v2}
			if (i in [1]) and ( re.findall(r'(?i)ZigZag\+\+', z.description+' '+z2.description) ):
				if int(vv['New_Higher_Low']) ==1: arB.append({'c': cc, 's': 'zz_hl', 'd':'long'})
				if int(vv['New_Lower_Low'])  ==1: arB.append({'c': cc, 's': 'zz_ll', 'd':'long'})
				if int(vv['New_Higher_High'])==1: arB.append({'c': cc, 's': 'zz_hh', 'd':'short'})
				if int(vv['New_Lower_High']) ==1: arB.append({'c': cc, 's': 'zz_lh', 'd':'short'})
			for i, r in pd.DataFrame(arB).drop_duplicates().iterrows():
				print(f"- {r['c']}, {r['s']}, {r['d']}, {datetime.now()}")
# with open('hello.txt', 'w') as f:
# 	f.write('Hello World from Python script!')
# print("File written successfully")
