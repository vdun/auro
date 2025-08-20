import time
from javascript import require
tv=require('@mathieuc/tradingview')
# print(tv)
c=tv.Client(); time.sleep(1)
ch = c.Session.Chart()
print(ch)
	
# with open('hello.txt', 'w') as f:
# 	f.write('Hello World from Python script!')
# print("File written successfully")
