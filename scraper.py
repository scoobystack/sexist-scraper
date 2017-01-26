

#import requests
from bs4 import BeautifulSoup as Soup 
import urllib, requests, re, pandas as pd 

beginurl = 'http://api.indeed.com/ads/apisearch?publisher=3025890005972088&q=software+engineer&sort=&radius=&st=&jt=fulltime&start='
endurl = '&limit=3000&fromage=0&filter=1&latlong=1&co=us&chnl=&userip=1.2.3.4&useragent=Mozilla/%2F4.0%28Firefox%29&v=2'

pd.set_option('max_colwidth',500)	#remove column limit
df = pd.DataFrame()		# create a new data frame
 
# textfile = open("/Users/stacy/Desktop/sexist-scraper/unedited.txt","a")
 
for page in range(0,20): #change to 30
    print page
    print
    print
    indeedurl = "%s%s%s" % (beginurl, page*25, endurl) # get full url 
    # print indeedurl
    rawdata = Soup(urllib.urlopen(indeedurl), "lxml") 

    for i in range(0,25):#change to 25
        result = rawdata.results.contents[i]
        jobtitle = result.find({'jobtitle'}).getText()
        # print jobtitle
        company = result.find({'company'}).getText()
        # print company
        location = result.find({'formattedlocation'}).getText()
        # print location
        city = result.find({'city'}).getText()
        state = result.find({'state'}).getText()
        date = result.find({'date'}).getText()
        # print date
        snippet = result.find({'snippet'}).getText()
        # print snippet
        joburl = result.find({'url'}).getText()
        # print joburl
        # access url and grab full job description
        wordsoup = Soup(urllib.urlopen(joburl), "lxml")
        descript = wordsoup.find('span', attrs = {'id':'job_summary'}).getText().strip()
        # print descript
        sponsored = result.find({'sponsored'}).getText()
        # print sponsored
        expired = result.find({'expired'}).getText()
        # print expired
        uniqueID = company[0:2]+location[0:2]+date[8:10]+date[5:7]+joburl[37:42]
        # print uniqueID
        print i

        
        df = df.append({
            'A-Unique ID': uniqueID, 
            'B-Job Title': jobtitle,
            'C-Company': company, 
            'D-City': city, 
            'E-State': state, 
            'F-Location': location, 
            'G-Snippet': snippet, 
            'H-Date': date, 
            'I-Url': joburl, 
            'J-Sponsored': sponsored, 
            'K-Expired': expired, 
            'L-Full description': descript}, 
            ignore_index=True)

    # textfile.write(str(rawdata))

# textfile.close()

df
df.to_csv("/Users/stacy/Desktop/sexist-scraper/Jan_25.csv", encoding="utf-8")

"""get job info from indeed.com

http://api.indeed.com/ads/apisearch?publisher=2109852150262296
&q=software+engineer&jt=fulltime&fromage=0&chnl=PsychProject
&userip=1.2.3.4&useragent=Mozilla/%2F4.0%28Firefox%29&v=2

http://api.indeed.com/ads/apisearch?publisher=3025890005972088&q=software+engineer&sort=&radius=&st=&jt=fulltime&start=&limit=1000&fromage=0&filter=1&latlong=1&co=us&chnl=&userip=1.2.3.4&useragent=Mozilla/%2F4.0%28Firefox%29&v=2

"""