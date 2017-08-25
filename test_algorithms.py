
import stock_algorithms

price_list = [1, 2, 3, 4, 5, 5, 5, 4, 3]

alg = stock_algorithms.SellAlgorithm(2, 1.1)

for price in price_list:
	result = alg.nextState(price)
	if result == stock_algorithms.SELL:
		print "Selling at ${}".format(price)
		return

