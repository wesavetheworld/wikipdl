import urllib.request
import requests

NSFW_LIST = ['sex','anal ','penis','vagina','boobs','vagin','seins']
print("-- Thanks for downloading wikpidl.py V:0.0.1")
print("-- When searching use _ instead of spaces and make sure to capitalize each word")
print("-- i.e. Aaron_Swartz or All_About_That_Bass")
langAnswered = False
while langAnswered == False:
    try :
        language = str(input("\nWhat language do you want the page to be in ? (English or French) "))
        if language.lower() == "english":
            lang = 'en'
            langAnswered = True
        elif language.lower() == 'french':
            lang = 'fr'
            langAnswered = True
    except ValueError:
        langAnswered = False

pageValidation = False

while pageValidation == False:
    article = str(input("\nWhat wikipedia page do you want to download ? "))
    url = 'https://' + lang + '.wikipedia.org/wiki/' + article
    
    ret = requests.head(url)
    statCode = ret.status_code
    if statCode == 200:
        #print('\nThis webpage exists ! ')
        pageValidation = True
    else:
        print("\nThis webpage doesn't exist ! ")
    #print(ret.status_code)


response = urllib.request.urlopen(url)
webContent = str(response.read().decode("utf-8"))
webContentLowered = webContent.lower()

for i in NSFW_LIST:
    if i in webContentLowered:
        if i == 'anal ':
            print("\nThis page is NSFW ! It has the word " + i + "in it !")
        else:
            print("\nThis page is NSFW ! It has the word " + i + " in it !")

dlname = lang+'_'+article.lower()+'_wikipedia.html'

f = open(dlname, 'w')
f.write(webContent)
f.close

print('\nThis webpage exists ! ' + dlname + " has been downloaded ! ")