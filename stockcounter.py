from Tkinter import *

class stockcounter:
    incrementableCount = 0
    percent = 0.0
    
    # set up small frame and label for keeping track of stocks that have
    # gone through the formula.
    def __init__(self, window,totalStocks):
        self.window = window
        self.totalStocks = totalStocks
        self.currentCount = StringVar()
        self.percentComplete = StringVar()
        self.currentCount.set("0")
        self.percentComplete.set("0 %")
        
        window.resizable(width=FALSE, height=FALSE)
        window.geometry("160x110")
        window.title("stock count")
        
        # will show a total completion
        self.count = Label(window, justify = LEFT, padx = 50, textvariable = self.currentCount)
        self.count.pack()
        
        self.separator1 = Label(window, justify = LEFT, padx = 50, text = "-----")
        self.separator1.pack()
        
        self.totalCount = Label(window, justify = LEFT, padx = 50, text = str(totalStocks))
        self.totalCount.pack()
        
        self.separator2 = Label(window,justify = LEFT, padx = 50, text = "-----")
        self.separator2.pack()
        
        # will show percent complete
        self.percent = Label(window, justify = LEFT, padx = 50, textvariable = self.percentComplete)
        self.percent.pack()    
    
    # When a stock has been put through the formula we want to
    # increment the counter label.
    def updateCompleted(self):
        stockcounter.incrementableCount += 1
        self.currentCount.set(str(stockcounter.incrementableCount))
    
    # When a stock has been put through the formula we want to
    # compute the percent complete.
    def updatePercent(self,totalStocks):
        # formatted to show up to two decimal places
        stockcounter.percent = "{0:.2f}".format(100.0 * stockcounter.incrementableCount / totalStocks)
        self.percentComplete.set(str(stockcounter.percent) + " %")
        
