from Tkinter import *
from stockcounter import *

import stockformula
import stockutilities
import threading
import time

#***************************************************************
# combine all stock lists for now.
# I might make it possible to choose what list to
# use instead of all 3
largeStockList = stockutilities.createListOfStocks()
totalInList = len(largeStockList)

def main(stockcounter,root):    
    
    finalStockList = []
    # Use a random stock as a way to find the last 20 trading days
    # This makes it so we only have to get these dates one time, as
    # opposed to finding them every time we need to get the average.
    last20 = stockutilities.getLast20TradingDays('AAPL')
    for stock in largeStockList:
        avg = stockformula.getAverageVolumeOver20Days(stock, last20[0],last20[1])
        if avg > 350000:
            stockName = stockformula.pullBackSwingTradeFormula(stock)
        
            if stockName != '':
                finalStockList.append(stockName)
                
        stockcounter.updateCompleted()
        stockcounter.updatePercent(totalInList)
        # update the tkinter form
        root.update()
        
    stockutilities.saveToFile(finalStockList)
    print "ITS FINISHED!"


if __name__ == '__main__':
    root = Tk()
    theStockCounter = stockcounter(root,totalInList)
    
    # Now that a frame is involved... we need to make the stock formula
    # loop in its own thread.  The frame is also in its own thread.
    GOSTOCKS = threading.Thread(target = main(theStockCounter,root))
    GOSTOCKS.start()