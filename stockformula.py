from yahoo_finance import Share
from pprint import pprint

import finsymbols
import time
import datetime

# creates a list of stocks from a provided csv file
def createListOfStocks():
    listOfStockNames = []
    initialAmex = finsymbols.get_amex_symbols()
    initialNasdaq = finsymbols.get_nasdaq_symbols()
    initialNyse = finsymbols.get_nyse_symbols()
    
    nyse = [stockInfo['symbol'].strip() for stockInfo in initialNyse]
    nasdaq = [stockInfo['symbol'].strip() for stockInfo in initialNasdaq]
    amex = [stockInfo['symbol'].strip() for stockInfo in initialAmex]
    
    return nasdaq


# Returns current day and the 20th trading day before day.
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




# Average Volume over 20 days...
def getAverageVolumeOver20Days(stockName,cur_day,twenty_day):
    stock = Share(stockName)
    stockData = stock.get_historical(str(twenty_day),str(cur_day))
    
    twentyDayVolAvg = 0
    if stockData == []:
        return 0       
    for date in stockData:
            twentyDayVolAvg = twentyDayVolAvg + float(stockData[0]['Volume'])    
    return twentyDayVolAvg / 20

 
def findData(stock, curDay,key):
     data = ()
     dayCount = 1
     check = False
     
     while check == False:
         difference = datetime.timedelta(days = dayCount)
         day = curDay[1] - difference
         stockInfo = stock.get_historical(str(day), str(day))
         
         if stockInfo != []:
             data = float(stockInfo[0][key]), day
             check = True
         else:
            dayCount += 1
            
     return data

def findP1Close(stock,curDay):
    print " "

#****************************************************
# Last = This is the lowest price the stock traded at that day
# PLow = Previous day's low
# P1Close = Previous day's close
# P2Close = The close the day before P1
# P3Close = The close the day before P2
# P4Close = The close the day before P3
#
# ---------------------------------------------------
# Formula
# ---------------------------------------------------
# VolAvg20 > 350,000
# Last     > PLow
# P1Close  < P2Close
# P2Close  < P3Close
# P3Close  < P4Close
######################################################
def pullBackSwingTradeFormula(stockName):
    stock = Share(stockName)
    currentDay = datetime.date.today()
    #default tuple
    theDay = 0.0 , currentDay
    
    Last = findData(stock, theDay, 'Low')
    PLow = findData(stock, Last, 'Low')
    
    # P1Close is a special case because it
    # is on the same day as PLow
    # Had to add an if stmt in here because yahoo_finance
    # would randomly give blank data sets for no reason..
    stockInfo = stock.get_historical(str(PLow[1]), str(PLow[1]))
    if stockInfo == []:
        P1Close = 0.0, PLow[1]
    else:
        P1Close = float(stockInfo[0]['Close']), PLow[1]

    
    P2Close = findData(stock, P1Close,'Close')
    P3Close = findData(stock, P2Close,'Close')
    P4Close = findData(stock, P3Close,'Close')
    
    if (Last[0] > PLow[0]) and (P1Close[0] < P2Close[0]) and (P2Close[0] < P3Close[0]) and (P3Close[0] < P4Close[0]):
        print  "\(^_^)/ Made it through the formula  " ,stockName
        return stockName
    else:
        return ''

# saves the list of stocks that passed the formula
# This function appends to a text file so the
# previous list of stocks will remain.
def saveToFile(stockList):
    currentDay = datetime.date.today()
    file = open("final_stock_list","a")
    file.write('\n')
    file.write( "Stock formula run on -> "+ str(currentDay) + '\n')
    
    for item in stockList:
        file.write(item + '\n')
    file.write('****************************************** \(^_^)/')
    file.write('\(^_^)/***********************************')
    
#***************************************************************
# combine all stock lists for now.
# I might make it possible to choose what list to
# use instead of all 3
largeStockList = createListOfStocks()

finalStockList = []
# Use a random stock as a way to find the last 20 trading days
# This makes it so we only have to get these dates one time, as
# opposed to finding them every time we need to get the average.
last20 = getLast20TradingDays('AAPL')

for stock in largeStockList:
    avg = getAverageVolumeOver20Days(stock, last20[0],last20[1])
    if avg > 350000:
        stockName = pullBackSwingTradeFormula(stock)
        
        if stockName != '':
            finalStockList.append(stockName)
        

saveToFile(finalStockList)
print "ITS FINISHED!"