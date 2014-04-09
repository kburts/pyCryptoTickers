import os

import pprint
import json
import simplejson


outdata = []
outstr = ''

with open('Data/BTC-e/btc_usd.txt') as data_file:
    data = data_file.readlines()

    outdata.append('[')
    for N in data[:-1]:
        if N[0]!= 'error':
            outdata.append(N+",")
    outdata.append(data[-1])
    outdata.append(']')

    for line in outdata:
        outstr += line
    print outstr

    outdata = simplejson.loads(outstr)

with open('input.csv', 'w') as output_file:
    for line in outdata:
        #print line
        output_file.write("%s,%0.12f,%0.6f\n" %(
            line.get('btc_usd').get('updated'), float(line.get('btc_usd').get('last')),float(line.get('btc_usd').get('vol_cur'))))

print 'done'
