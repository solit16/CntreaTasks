import sys

class Network:
	def __init__(self):
		self.node_array = []
	def node(self, combine, indexes):
		self.node_array.append((combine, indexes[:]))
		return len(self.node_array) - 1
	def values(self, items):
		d = {}
		for key, val in items:
			d[key] = val

		for i in range(len(self.node_array)):
			if i not in d:
				d[i] = self.node_array[i][0]([d[x] for x in self.node_array[i][1]])
		return list(d.values())

exec(sys.stdin.read())
