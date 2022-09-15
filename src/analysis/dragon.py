from src.analysis.convert import Convert

data = Convert().getData()
index = 0
for code_ in data.keys():
	index +=1
	infos = data.get(code_).infos
	if len(infos) < 30:
		continue
	infos.sort(key=lambda x: x.date, reverse=False)
	avg = 0
	sum = 0
	count = 0
	max = 0
	min = 10000
	for info in infos:
		sum += info.close
		count += 1
		if info.close > max:
			max = info.close
		if info.close < min:
			min = info.close
	range = ((max - min) / min)*100
	avg = sum/count
	sum = 0
	for info in infos:
		sum += (info.close - avg)*(info.close - avg)
	variance = sum/count
	variance = (variance/avg)*100
	if range < 20 :
		print(code_ + " " +str(range) + " " + str(variance))

