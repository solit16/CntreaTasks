class Dict:
	def __init__(self):
		self.size = 0
		self.table = [None]*10
		self.deleted = 0

	def __contains__(self, key):
		try:
			self[key]
			return True
		except:
			return False

	def __getitem__(self, key):
		start = hash(key) % len(self.table)
		index = start
		while True:
			if self.table[index] is None:
				raise KeyError(key)
			if self.table[index][0] == key:
				return self.table[index][1]

			index = (index + 1) % len(self.table)
			if index == start:
				raise KeyError(key)

	def __setitem__(self, key, value):
		start = hash(key) % len(self.table)
		index = start
		reserved_place = None
		while True:
			if self.table[index] == 'DELETED' and reserved_place is None:
				reserved_place = index
			if (type(self.table[index]) == list) and (self.table[index][0] == key):
				self.table[index][1] = value
				return
			if self.table[index] is None:
				if reserved_place is None:
					self.table[index] = [key, value]
				else:
					self.table[reserved_place] = [key, value]
				self.size += 1
				if (self.size + self.deleted) * 2 >= len(self.table):
					self.rebuild()
				return
			index = (index + 1) % len(self.table)
			if index == start:
				self.table[reserved_place] = [key, value]
				self.size += 1
				if (self.size + self.deleted) * 2 >= len(self.table):
					self.rebuild()
				return

	def __delitem__(self, key):
		start = hash(key) % len(self.table)
		index = start
		while True:
			if self.table[index] is None:
				raise KeyError(key)
			if (type(self.table) == list) and (self.table[index][0] == key):
				self.table[index] = 'DELETED'
				self.deleted += 1
				self.size -= 1
				return
			index = (index + 1) % len(self.table)
			if index == start:
				raise KeyError(key)

	def __len__(self):
		return self.size

	def rebuild(self):
		res = [None] * len(self.table) * 2
		for el in self.table:
		  if type(el) == list:
				index = hash(el[0]) % len(res)
				while True:
					if res[index] is None:
						res[index] = el
						break
					index = (index + 1) % len(res)
		self.deleted = 0
		self.table = res
		return

import sys
exec(sys.stdin.read())
