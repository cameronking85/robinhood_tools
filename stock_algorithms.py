import time

STATE_START   = 0
STATE_RISING  = 1
STATE_FALLING_LOW = 2
STATE_FALLING_HIGH = 3

SELL = 1

class SellAlgorithm(object):

	def __init__(self, buy_price, margin_percent):
		self._history = []
		self._state = STATE_START
		self._buy_price = buy_price
		self._margin_percent = margin_percent
		if margin_percent < 1.:
			raise Exception("Margin must be greater than one")

	def addData(self, price):
		self._history.append((time.ctime(), price))

	def nextState(self, price):
		self.addData(price)
		
		if len(self._history) > 1:
			if price > self._history[-2][1]:
				self._state = STATE_RISING
			elif price < self._history[-2][1]:
				if price > self._buy_price:
					self._state = STATE_FALLING_HIGH
				else:
					self._state = STATE_FALLING_LOW

		if self._state == STATE_FALLING_HIGH:
			if price > self._buy_price*self._margin_percent:
				return SELL







