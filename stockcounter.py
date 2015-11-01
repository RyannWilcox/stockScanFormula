from Tkinter import *

class stockcounter:
    incrementableCount = 0
    
    # set up small frame and label for keeping track of stocks that have
    # gone through the formula.
    def __init__(self, window,totalStocks):
        self.window = window
        self.totalStocks = totalStocks
        self.currentCount = StringVar()
        window.resizable(width=FALSE, height=FALSE)
        window.geometry("150x100")
        window.title("stock count")
        self.currentCount.set("0")
        self.count = Label(window, justify = LEFT, padx = 50, textvariable = self.currentCount)
        self.count.pack()
        
        self.separator = Label(window, justify = LEFT, padx = 50, text = "-----")
        self.separator.pack()
        
        self.totalCount = Label(window, justify = LEFT, padx = 50, text = str(totalStocks))
        self.totalCount.pack()       
    
    # When a stock has been put through the formula we want to
    # increment the counter label.
    def updateCompleted(self):
        stockcounter.incrementableCount += 1
        self.currentCount.set(str(stockcounter.incrementableCount))

