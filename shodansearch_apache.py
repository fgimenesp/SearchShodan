#!/usr/bin/python

#Create by /x46/x47/x50 

import shodan

SHODAN_API_KEY = "Your API KEY"

api = shodan.Shodan(SHODAN_API_KEY)

try:
            # Search Shodan
            results = api.search('ASN:Your AS product:apache')

            # Show the results
            print 'Results found: %s' % results['total']
            for result in results['matches']:
                   print 'IP: %s' % result['ip_str']
                   print 'Port: %s' %result['port']
                   print result['data']
                   print ''
except shodan.APIError, e:
            print 'Error: %s' % e
