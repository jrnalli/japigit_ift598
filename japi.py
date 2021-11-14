import urllib.request
import json


def getStockData(stockSymbol):
    nasdaqAppleURL = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stockSymbol}&apikey=HALHYZAMLVV8HHAF'
    connection = urllib.request.urlopen(nasdaqAppleURL)
    return connection.read().decode()


def main():
    i = 0
    while i < 10:
        inputValue = input("Stock Symbol: ")
        if inputValue != "quit":
            outputValue = getStockData(inputValue)
            print(outputValue)
            stockQuoteDictionary = json.loads(outputValue)
            stockPrice = stockQuoteDictionary['Global Quote']['05. price']
            currentPriceOutput = f'The current price of {inputValue} is: {stockPrice}'
            print(currentPriceOutput)
            openFile = open("japi.out", "a")
            openFile.write(outputValue + "\n\n")
            openFile.write(currentPriceOutput + "\n\n")
            openFile.close()
        else:
            quit()


main()
