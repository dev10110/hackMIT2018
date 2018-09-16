import requests
import json

aprs = []
locData = {}
#input list of volunteer's callsigns, returns

def volunteerLoc(callList):

    aprsWeb = 'https://api.aprs.fi/api/get?name='
    aprsWeb+=callList[0]
    
    for i in range(1,len(callList)):

        aprsWeb+=','
        call = callList[i]
        aprsWeb+= call 


    aprsWeb+='&what=loc&apikey=116932.M4GQQFbrZzOx9&format=json'
    grabaprs = requests.get(aprsWeb)
    jlist = grabaprs.content
    aprs = json.loads(jlist)

    for i in range(0,len(callList)):
        
        locData[aprs['entries'][i]['name']] = [aprs['entries'][i]['lat'],aprs['entries'][i]['lng']]
        
    return locData


print(volunteerLoc(['K1MQ','KB1IXO-9','EW3846']))

