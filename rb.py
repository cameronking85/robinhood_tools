from Robinhood import Robinhood
import getpass, time, sys

USERNAME = sys.argv[1]
STOCK_NAME = sys.argv[2]

trader = Robinhood()
logged_in = trader.login(username=USERNAME, password=getpass.getpass())

stock_instrument = None
while True:
	quote_info = trader.quote_data(STOCK_NAME)
	stock_instrument = trader.instruments(STOCK_NAME)[0]
	print("################################")
	print("Time:        {}".format(time.ctime()))
	print("################################")
	print("Name:        {}".format(stock_instrument['name']))
	print("Symbol:      {}".format(STOCK_NAME))
	print("Price:       ${}".format(quote_info['last_trade_price']))
	instrument_url = stock_instrument['url']
	owned = trader.securities_owned()['results']
	print("################################")
	for sec in owned:
		if sec['instrument'] == instrument_url:
			price = sec['average_buy_price']
			quantity = sec['quantity']
			print("Ave. Price:  ${}".format(price))
			print("Shares:      {}".format(quantity))
			print("Total Value: ${}".format(round(float(price)*float(quantity)), 2))
	print("################################\n")

def sellIf(instrument, current_price, sell_price, quantity):
	if current_price >= sell_price:
		return trader.place_sell_order(instrument, quantity)
	return None

def buyIf(instrument, current_price, buy_price, quantity):
	if current_price <= buy_price:
		return trader.place_buy_order(instrument, quantity)
	return None