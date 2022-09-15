import akshare as ak
import datetime
from dateutil.relativedelta import relativedelta
import sqlite3
import time
conn = sqlite3.connect('../data.sqlite')

#stock_zh_a_spot_em_df = ak.stock_zh_a_spot_em()
#stock_zh_a_spot_em_df.to_sql('code', con=conn, if_exists='append', index=True)

cursor=conn.cursor()

end = datetime.datetime.now()
start = end - relativedelta(months=3)
#start = end - relativedelta(days=10)

cursor.execute("SELECT \"日期\" FROM stock ORDER BY \"日期\" DESC LIMIT 1")

lastDate = ""
for row in cursor:
	lastDate = row[0]
	print("lastDate: %s", lastDate)

lastDate_timeStamp = int(time.mktime(time.strptime(lastDate, '%Y-%m-%d')))

exit = False
try:
	stock_1 = cursor.execute("select * from stock")
	exit = True
except:
	exit = False

if not exit:
	sql = "create table stock("
	sql += "股票代码 TEXT,"
	sql += "日期 TEXT,"
	sql += "开盘 FLOAT,"
	sql += "收盘 FLOAT,"
	sql += "最高 FLOAT,"
	sql += "最低 FLOAT,"
	sql += "成交量 FLOAT,"
	sql += "成交额 FLOAT,"
	sql += "振幅 FLOAT,"
	sql += "涨跌幅 FLOAT,"
	sql += "涨跌额 FLOAT,"
	sql += "换手率 FLOAT)"
	print(sql)
	cursor.execute(sql)

content = cursor.execute("SELECT 代码 from code")
index = 0

code_list = list()
for row in cursor:
	code_list.append(row[0])

for code_ in code_list:
	index +=1
	print(code_)
	stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol=code_, period="daily", start_date=lastDate,
											end_date=end.strftime("%Y%m%d"), adjust="")
	for value in stock_zh_a_hist_df.values:
		date = value[0]
		date_timeStamp = int(time.mktime(time.strptime(date, '%Y-%m-%d')))
		# print(date_timeStamp)
		if date_timeStamp > lastDate_timeStamp:
			print(value)
			sql = "insert into stock(股票代码,日期,开盘,收盘,最高,最低,成交量,成交额,振幅,涨跌幅,涨跌额,换手率) values ('"
			sql += code_ + "','"
			sql += str(value[0]) + "',"
			sql += str(value[1]) + ","
			sql += str(value[2]) + ","
			sql += str(value[3]) + ","
			sql += str(value[4]) + ","
			sql += str(value[5]) + ","
			sql += str(value[6]) + ","
			sql += str(value[7]) + ","
			sql += str(value[8]) + ","
			sql += str(value[9]) + ","
			sql += str(value[10]) + ")"
			print(sql)
			cursor.execute(sql)
	conn.commit()
conn.close()