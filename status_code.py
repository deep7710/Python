import csv
import socket
import time
from urllib2 import urlopen

#URLS = ['http://www.google.com', 'http://www.yahoo.com']
#socket.setdefaulttimeout( 23 )  # timeout in seconds

#with open('/home/deependrasaraswat/python/url.csv', mode='r') as csv_file:
#    csv_reader = csv.DictReader(csv_file)
#    fields = csv_reader.next()
with open('url.csv','r') as csvf: # Open file in read mode
    data = csvf.read()
    urls = data.split("\n")


for url in urls:
    print str(url)
    print 'Checking URL {0}'.format(url)
    start = time.clock()
    try:
        socket.setdefaulttimeout( 23 )
        response = urlopen(url)
        print response.getcode()
#        print('response.getcode()')
    except StandardError, e:
        print 'Check failed: {0}'.format(e)
#
    print 'took {0}s\n'.format(time.clock() - start)
