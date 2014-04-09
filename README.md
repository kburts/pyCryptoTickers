# Kevin's Ticker App
## Simple Multithreaded app to get updated crypto-exchange prices

This is a simple app I made in python to query many crypto currency exchanges at once, and save the data to a text file. I used it with my candlestick-charter to make graphs & charts of crypto prices.

Note for the readDataFile.py script, you need to specify which exchange/pair you want to port into input.csv, then copy input.csv over to the candlestick-charter folder (it is automated on the django-charter site, but manual for only running the script so that the two apps don't directly interact with eachother.)


### Tickers.py > collect data for a couple days > configure readDatafile > readDataFile.py > copy input.csv to django-charter > run django-charter.py

