from src.analysis.convert import Convert

data = Convert().getData()
for code_ in data.keys():
	data.get(code_).infos.sort(key=lambda x: x.date, reverse=False)

print(data)
