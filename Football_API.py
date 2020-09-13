import json
import urllib.request,urllib.parse,urllib.error

def data():
    id =getTeamid()
    url = "https://www.thesportsdb.com/api/v1/json/1/eventsnext.php?id="+id
    html = urllib.request.urlopen(url).read().decode()
    js = json.loads(html)

    fix = list()
    events = js['events']
    for i in range(0,len(events)):
        data = js["events"][i]["strEvent"]+js['events'][i]['strLeague']+js['events'][i]['dateEvent']+js['events'][i]['strTime']+js['events'][i]['strVenue']
        fix.append(data)
    return fix


def getTeamid():
    name = input('Enter the name of the team whose fixtures you want: ')
    url = 'https://www.thesportsdb.com/api/v1/json/1/searchteams.php?t='+name
    html = urllib.request.urlopen(url).read().decode()
    js = json.loads(html)
    id = js['teams'][0]['idTeam']
    return id
