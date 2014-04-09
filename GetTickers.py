import os
import io

import urllib
import urllib2
import json
import time
import hmac,hashlib

#import thread
import threading
import Queue


class Ticker(threading.Thread):
    def __init__(self, marketName,   APIaddress,  pair):
        threading.Thread.__init__(self)
        
        self.link = APIaddress
        self.marketName = marketName
        self.pair = pair
        #print self.link
        #self.Loop()

     
    def run(self):
        #while True:
        host = self.pair.get()
        
        toWrite = self.getData(self.link + host)
        self.writeDataFile(toWrite,  (host +'.txt'))
    
        self.pair.task_done()
              
        
    def getData(self,  url):
        try:
            data = urllib2.urlopen(urllib2.Request(url)).read()
            print data
            return data
        except:
            self.writeErrorFile('error connecting to %s API at %i\n' %(self.marketName,  int(time.time())))
            print "error connecting to %s %s %s" %(url,  self.link,  self.pair)
            #print 'error'
            return 'error at: %i' %int(time.time())
        
        
    def writeErrorFile(self,  log):
        file = 'Data/ErrorLogs/log.txt'
        with open(file,  'a') as errorfile:
            errorfile.write(log)
     
     
    def writeDataFile(self,  toWrite,  fname):
        file = (os.path.join('Data/',  self.marketName+"/",  fname))
        with open(file, 'a') as outfile:
                outfile.write(toWrite + '\n')



exchanges={
        "BTC-e":"https://btc-e.com/api/3/ticker/",
        #"Cryptsy":"http://pubapi.cryptsy.com/api.php?method=singlemarketdata&marketid=", 
        "Bitfinex":"https://api.bitfinex.com/v1/ticker/", 
        "Bitstamp":"https://www.bitstamp.net/api/", 
        "MtGox":"http://data.mtgox.com/api/2/BTCUSD/money/", 
    }
exchange_pairs={
        "BTC-e":
            ("btc_usd", "ltc_btc", "ltc_usd",
              "nmc_btc", "nmc_usd", "nvc_btc",
             "nvc_usd", "trc_btc", "ppc_btc",
             "ppc_usd", "ftc_btc", "xpm_btc"),
        #"Cryptsy":("3", ), 
        "Bitfinex":("btcusd",  "ltcbtc",  "ltcusd" ), 
        "Bitstamp":("ticker", ), 
        "MtGox":("ticker_fast" , ), 
}




def main():
    queue = Queue.Queue()
   
    for exchange in exchanges.keys():
        for pair in exchange_pairs.get(exchange):
            queue.put(pair)
            
            t = Ticker(exchange,  exchanges.get(exchange),  queue)
            t.setDaemon(True)
            t.start()
    
    queue.join()

    #print 'done'
    
    
while True:
    main()
    time.sleep(4)
