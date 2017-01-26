
"""get job info from indeed.com

http://api.indeed.com/ads/apisearch?publisher=2109852150262296
&q=java&l=94103&sort=&radius=10&st=&jt=fulltime&start=&limit=15&fromage
=100&filter=&latlong=1&co=us&chnl=PsychProject&userip=1.2.3.4&
useragent=Mozilla/%2F4.0%28Firefox%29&v=2

"""

#import requests
from bs4 import BeautifulSoup as Soup 
import urllib, requests, re, pandas as pd 

base_url = 'https://www.indeed.com/jobs?q=software+engineer&jt=fulltime&fromage=0&sort=#sthash.DnQEAxE8.dpuf'
sort_by = 'date'	# sort by data
start_from = '&start='	# start page number

pd.set_option('max_colwidth',500)	#remove column limit
df = pd.DataFrame()		# create a new data frame
 
for page in range(1,2): # page from 1 to 100 (last page we can scrape is 100) change from 2 to 100 after testing
    page = (page-1) * 11  
    url = "%s%s%s%d" % (base_url, sort_by, start_from, page) # get full url 
    print url
    rawdata = Soup(urllib.urlopen(url), "lxml") 
    # my test of whether collecting the data
    textfile = open("/Users/stacy/Desktop/sexist-scraper/unedited.txt","a")
    textfile.write(str(rawdata))
    textfile.close()

    targetJobs = rawdata.findAll('div', attrs ={'class':' row result'}) 
    lastJob = rawdata.findAll('div', attrs = {'class':'lastRow row result'})

    print len(targetJobs)
    print len(lastJob)

    for info in targetJobs: 
        company = info.find('span', attrs={'itemprop':'name'}).getText().strip()
        print "company: "+company
        location = info.find('span', attrs={'itemprop':'addressLocality'}).getText().strip()
        print "location: "+location
        summary = info.find('span', attrs={'itemprop':'description'}).getText().strip()
        print "summary: "+summary
        # joblink = info.find('a', attrs = {'href'})
        # # fulllink = 'indeed.com'+joblink
        # print joblink

    #joblink
        #fulljobdescription
    # trying to get each specific job information (such as company name, job title, urls, ...)
    #positionsummary
    #salary (if there)
