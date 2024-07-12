from argparse import ArgumentParser
from json import dumps


symbols_with_shift=[
	{"symbol":"!", "key":"1"},
	{"symbol":"@", "key":"2"},
	{"symbol":"#", "key":"3"},
	{"symbol":"$", "key":"4"},
	{"symbol":"%", "key":"5"},
	{"symbol":"^", "key":"6"},
	{"symbol":"&", "key":"7"},
	{"symbol":"*", "key":"8"},
	{"symbol":"(", "key":"9"},
	{"symbol":")", "key":"0"},
	{"symbol":"_", "key":"-"},
	{"symbol":"+", "key":"="},
	{"symbol":")", "key":"0"},
	{"symbol":"{", "key":"["},
	{"symbol":"}", "key":"]"},
	{"symbol":":", "key":";"},
	{"symbol":"\"", "key":"'"},
	{"symbol":"|", "key":"\\"},
	{"symbol":"<", "key":","},
	{"symbol":">", "key":"."},
	{"symbol":"?", "key":"/"}
]

symbols_without_shift="-=[];'\\,./ \n"

class converter:
	def __init__(self):
		self._argparse=ArgumentParser(
				prog="converter"
				)

		self._argparse.add_argument('input')
		self._argparse.add_argument('output')


		self._args=self._argparse.parse_args()


		with open(self._args.input,'r') as input_file:
			input=input_file.read()


		data=self.convert(input)

		with open(self._args.output,'w') as output_file:
		 	output_file.write(data)

	def _symbol_with_shift(self, data):
		for a in symbols_with_shift:
			if data==a['symbol']:
				return a
		return False


	def convert(self, input):
		output=[{"mods": ["win"], "keys": ["r"], "delay": 100},{"mods":[], "keys": ["c","m","d",".","e","x","e","\n"],"delay": 100} ]
		for a in input:
			if a.islower() or a.isdigit():
				data={
					"mods":[],
					"keys":[a]
					}

			else:
				if a in symbols_without_shift:
					data={
						"mods":[],
						"keys":[a]
					}

				elif self._symbol_with_shift(a):
					d=self._symbol_with_shift(a)
					data={
						"mods":['shift'],
						"keys":[d['key']]
					}
				else:
					data={
						"mods":["shift"],
						"keys":[a.lower()]
					}
			output.append(data)

		return dumps(output)






if __name__=="__main__":
	conv=converter()