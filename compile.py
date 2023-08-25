class Templates:
	SUMMON = '/summon minecraft:wandering_trader ~ ~ ~ {Invulnerable:1b, NoAI:1b, Glowing:1b, Offers:{Recipes:[%s]}}'
	TRADE = '{maxUses:999999999, rewardExp:0b, priceMultiplier:1, buy: %s, buyB: %s, sell: %s}'
	ITEM = '{id: "minecraft:%s", Count: %s}'
	AIR = '{id:"minecraft:air"}'


class Parser:
	def __init__(self):
		self.names = {}
		self.trades = []

	def parse(self, text: str) -> str:
		for line in text.splitlines():
			line = line.strip()
			if line == '': continue
			elif line.startswith('/'): continue
			elif line == '//': break
			elif line.startswith('$ '): self.new_name(line[1:])
			else: self.new_trade(line)
		return Templates.SUMMON % ', '.join(self.trades)

	def new_name(self, line: str) -> None:
		name, value = (i.strip() for i in line.split(':', 1))
		self.names[name] = f'{value[:-1]}, Count: %s}}'

	def new_trade(self, line: str) -> None:
		def process_item(text: str) -> str:
			if text == 'air': return Templates.AIR
			if '*' in text: name, count = (i.strip() for i in text.split('*'))
			else: name, count = text.strip(), '1'
			if name in self.names: return self.names[name] % count
			return Templates.ITEM % (name, count)

		price, sell = line.split('=>', 1)
		sell: str = process_item(sell)
		price: str
		if ',' in price: buy, buy_b = price.split(',')
		else: buy, buy_b = price, 'air'
		buy = process_item(buy)
		buy_b = process_item(buy_b)
		self.trades.append(Templates.TRADE % (buy, buy_b, sell))


if __name__ == '__main__':
	with open(input('> '), 'r') as file: print(Parser().parse(file.read()))
