#!/usr/bin/python

#Create by /x46/x47/x50 

import shodan

SHODAN_API_KEY = "YOUR API KEY"

api = shodan.Shodan(SHODAN_API_KEY)

try:
            # This is scriptin has objective find Tomcat Manager
            results = api.search('realm="Tomcat Manager Application"')

            # Show the results
            print 'Results found: %s' % results['total']
            for result in results['matches']:
                   print 'IP: %s' % result['ip_str']
                   print 'Port: %s' %result['port']
                   print result['data']
                   print '/home/fgp/ScriptShodan/BannerTomcat.txt'
except shodan.APIError, e:
            print 'Error: %s' % e
