import json
import requests                     #To install this package run: sudo pip install requests

def spam():
    token = "" #Insert access token here. Can be obtained from https://developers.facebook.com/tools/explorer
    appId = '145634995501895' #Make sure that you get the updated AppId from https://developers.facebook.com/tools/debug/accesstoken (You can use the AppId for Graph API Explorer)
    
    graph_url = "https://graph.facebook.com/"
    version = "v2.9/"
    id = "" # Enter the victim's Facebook id
    query = graph_url + version + id + "/posts?fields=id&limit=100&access_token=" + token # Added limit of 100 latest posts as required by FB
    response = requests.get(query)
    r = response.json()
    
    
    
    idlist = [x['id'] for x in r['data']]
    idlist.reverse()
    print("There are "+ str(len(idlist)) +" spammable posts.")
    
    char1 = input("Do you want to spam? (y/n) ")
    count = 0
    if char1 == 'y':
        nos = int(input("Enter number of posts to be spammed with comments: "))
        comment = input("Enter the message to be commented: ")
        if nos <= len(idlist):
           for indid in (idlist[(len(idlist) - nos):]):
            url = graph_url + version + indid + "/comments/?message=" + comment + "&access_token=" + token
            data = str({"appId":"%s"}) % (appId)
            resp = requests.post(url = url, data = data)
            assert resp.status_code == 200
            #Comments on each post
            print("Notification number: " + str(count) + " on www.facebook.com/" + str(indid).split('_')[0] 
              + "/posts/" + str(indid).split('_')[1])
        else: 
          print("Not that many spammable posts available. No spam happening.")
    else :
      print("No spam happening then.")

spam()