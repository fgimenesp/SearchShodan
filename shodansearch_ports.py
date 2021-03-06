#!/usr/bin/python

#Create by /x46/x47/x50

import shodan

SHODAN_API_KEY = "YOUR API KEY"

api = shodan.Shodan(SHODAN_API_KEY)

try:
            # This is a script that aims to find common ports in any AS
            results = api.search('ASN:Your AS port:25,80,110,143,443,500,4500,8080,8443,20,21,22,23,139,161,445,1433,1900,2222,3306,3389,5900')
 
            # Show the results
            print 'Results found: %s' % results['total']
            for result in results['matches']:
                   print 'IP: %s' % result['ip_str']
                   print 'Port: %s' %result['port']
                   print result['data']
                   print ''
except shodan.APIError, e:
            print 'Error: %s' % e

