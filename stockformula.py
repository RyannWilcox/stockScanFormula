from yahoo_finance import Share
import time
import datetime
import stockutilities;

# Average Volume over 20 trading days...
def getAverageVolumeOver20Days(stockName,cur_day,twenty_day):
    stock = Share(stockName)
    stockData = stock.get_historical(str(twenty_day),str(cur_day))
    
    twentyDayVolAvg = 0
    if stockData == []:
        return 0       
    for date in stockData:
        twentyDayVolAvg = twentyDayVolAvg + float(stockData[0]['Volume'])
                   
    return twentyDayVolAvg / 20

# will return stock data based on the day and the key provided
def findData(stock, curDay, key):
     data = ()
     dayCount = 1
     check = False
     
     while check == False:
         difference = datetime.timedelta(days = dayCount)
         day = curDay[1] - difference
         stockInfo = stock.get_historical(str(day), str(day))
         
         if stockInfo != []:
             try:
                 data = float(stockInfo[0][key]), day
             except:
                 print "bad data."
                 data = 0.0, day
                 
             check = True
         else:
            dayCount += 1
            
     return data

#****************************************************
# The main part of the formula
#
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
        print stockName + "Empty query retrieved for " + stockName;
        P1Close = 0.0, PLow[1]
    else:
        try:
            P1Close = float(stockInfo[0]['Close']), PLow[1]
        except:
            print stockName + " incorrect data sent.."
            P1Close = 0.0, PLow[1]
    
    P2Close = findData(stock, P1Close,'Close')
    P3Close = findData(stock, P2Close,'Close')
    P4Close = findData(stock, P3Close,'Close')
    
    if (Last[0] > PLow[0]) and (P1Close[0] < P2Close[0]) and (P2Close[0] < P3Close[0]) and (P3Close[0] < P4Close[0]):
        print  "\(^_^)/ Made it through the formula  " , stockName
        return stockName
    else:
        return ''