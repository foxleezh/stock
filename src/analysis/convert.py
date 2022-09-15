import sqlite3
from src.data.history_info import history_info
from src.data.history_info import code_info

class Convert:
	def getData(self):
		conn = sqlite3.connect('../../data_test.sqlite')
		cursor = conn.cursor()
		cursor.execute("select * from stock")
		data = {"000001": code_info()}
		for row in cursor:
			code_ = row[0]
			info = history_info()
			info.code = code_
			info.date = row[1]
			info.open = row[2]
			info.close = row[3]
			info.high = row[4]
			info.low = row[5]
			info.volume = row[6]
			info.total = row[7]
			info.range = row[8]
			info.raise_volume = row[9]
			info.raise_total = row[10]
			info.exchange = row[11]
			temp = data.get(code_)
			if temp is None:
				list = code_info()
				list.code = code_
				list.infos = []
				list.infos.append(info)
				data[code_] = list
			else:
				temp.infos.append(info)
		conn.close()
		return data