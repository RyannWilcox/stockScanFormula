import stockformula
import stockutilities

def main():
    #***************************************************************
    # combine all stock lists for now.
    # I might make it possible to choose what list to
    # use instead of all 3
    largeStockList = stockutilities.createListOfStocks()

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
        

    stockutilities.saveToFile(finalStockList)
    print "ITS FINISHED!"


if __name__ == '__main__':
    main()