from yahoo_finance import Share
import finsymbols
import time
import datetime

# saves the list of stocks that passed the formula
# This function appends to a text file so the
# previous list of stocks will remain.
def saveToFile(stockList):
    currentDay = datetime.date.today()
    file = open("final_stock_list","w")
    file.write('\n')
    file.write( "Stock formula run on -> "+ str(currentDay) + '\n')
    
    for item in stockList:
        file.write(item + '\n')
    file.write('****************************************** \(^_^)/')
    file.write('\(^_^)/***********************************')


# creates a list of stocks from a provided by the module finsymbols
# Only using nasdaq for now becuase nyse and amex were giving strange
# results.
def createListOfStocks():
    initialAmex = finsymbols.get_amex_symbols()
    initialNasdaq = finsymbols.get_nasdaq_symbols()
    initialNyse = finsymbols.get_nyse_symbols()
    
    nyse = [stockInfo['symbol'].strip() for stockInfo in initialNyse]
    nasdaq = [stockInfo['symbol'].strip() for stockInfo in initialNasdaq]
    amex = [stockInfo['symbol'].strip() for stockInfo in initialAmex]
    
    return nasdaq


# Returns current day and the 20th trading day
def getLast20TradingDays(stockName):
    stock = Share(stockName)
    currentDay = datetime.date.today()
    difference = datetime.timedelta(days=100)
    day = currentDay - difference

    stockData = stock.get_historical(str(day),str(currentDay))
    if stockData == []:
        return 0
    else:
        return [stockData[0]['Date'], stockData[19]['Date']]
