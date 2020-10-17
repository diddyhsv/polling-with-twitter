#this uses sentiment analysis and counts the number of users that posted positive tweets for each candidate

from textblob import TextBlob as TextBlob #2
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
import pickle
#import nltk
text1 = '''Join me in supporting Nicole Galloway via @actblue https://t.co/Kg0e5scsKF''' #3`
text2 = '''President Trump went to Toledo, Ohio today''' #4
text3 = '''For anyone keeping track here, Jim Justice is just straight-up lying during this debate. And he's not even lying to defend his terrible record - he's lying about CARS''' #5
blob = TextBlob(text1) #6
print(blob.sentiment.polarity) #11
blob = TextBlob(text2) #12
print(blob.sentiment.polarity) #13
blob = TextBlob(text3) #12
print(blob.sentiment.polarity) #13

johncarney, juliannemurray, ericholcomb, woodymyers, donaldrainwater, mikeparson, nicolegalloway, mikecooney, greggianforte, chrissununu, danfeltes, roycooper, danforest, dougburgum, shelleylenz, spencercox = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
christopherpeterson, philscott, davidzuckerman, jayinslee, lorenculp, jimjustice, bensalango, danielluz = set(), set(), set(), set(), set(), set(), set(), set()

client = MongoClient(port=27017)
db=client.TWITTERUSA
collection = db['tweets']
cursor = collection.find({"retweeted_status.full_text":{"$exists": "true"}})
for tw in cursor:
    if ("john carney" in tw["retweeted_status"]["full_text"].lower() ):
        blob = TextBlob(tw["retweeted_status"]["full_text"])
        if blob.sentiment.polarity > 0:
            johncarney.add(tw["user"]["id"])
    if ("julianne murray" in tw["retweeted_status"]["full_text"].lower() ):
        blob = TextBlob(tw["retweeted_status"]["full_text"])
        if blob.sentiment.polarity > 0:
            juliannemurray.add(tw["user"]["id"])
    if ("eric holcomb" in tw["retweeted_status"]["full_text"].lower() ):
        blob = TextBlob(tw["retweeted_status"]["full_text"])
        if blob.sentiment.polarity > 0:
            ericholcomb.add(tw["user"]["id"])
    if ("woody myers" in tw["retweeted_status"]["full_text"].lower() ):
        blob = TextBlob(tw["retweeted_status"]["full_text"])
        if blob.sentiment.polarity > 0:
            woodymyers.add(tw["user"]["id"])
    if ("donald rainwater" in tw["retweeted_status"]["full_text"].lower() ):
        blob = TextBlob(tw["retweeted_status"]["full_text"])
        if blob.sentiment.polarity > 0:
            donaldrainwater.add(tw["user"]["id"])
    if ("mike parson" in tw["retweeted_status"]["full_text"].lower() ):
        blob = TextBlob(tw["retweeted_status"]["full_text"])
        if blob.sentiment.polarity > 0:
            mikeparson.add(tw["user"]["id"])
    if ("nicole galloway" in tw["retweeted_status"]["full_text"].lower() ):
        blob = TextBlob(tw["retweeted_status"]["full_text"])
        if blob.sentiment.polarity > 0:
            nicolegalloway.add(tw["user"]["id"])
    if ("mike cooney" in tw["retweeted_status"]["full_text"].lower() ):
        blob = TextBlob(tw["retweeted_status"]["full_text"])
        if blob.sentiment.polarity > 0:
            mikecooney.add(tw["user"]["id"])
    if ("gregg gianforte" in tw["retweeted_status"]["full_text"].lower() ):
        blob = TextBlob(tw["retweeted_status"]["full_text"])
        if blob.sentiment.polarity > 0:
            greggianforte.add(tw["user"]["id"])
    if ("chris sununu" in tw["retweeted_status"]["full_text"].lower() ):
        blob = TextBlob(tw["retweeted_status"]["full_text"])
        if blob.sentiment.polarity > 0:
            chrissununu.add(tw["user"]["id"])
    if ("dan feltes" in tw["retweeted_status"]["full_text"].lower() ):
        blob = TextBlob(tw["retweeted_status"]["full_text"])
        if blob.sentiment.polarity > 0:
            danfeltes.add(tw["user"]["id"])
    if ("roy cooper" in tw["retweeted_status"]["full_text"].lower() ):
        blob = TextBlob(tw["retweeted_status"]["full_text"])
        if blob.sentiment.polarity > 0:
            roycooper.add(tw["user"]["id"])
    if ("dan forest" in tw["retweeted_status"]["full_text"].lower() ):
        blob = TextBlob(tw["retweeted_status"]["full_text"])
        if blob.sentiment.polarity > 0:
            danforest.add(tw["user"]["id"])
    if ("doug burgum" in tw["retweeted_status"]["full_text"].lower() ):
        blob = TextBlob(tw["retweeted_status"]["full_text"])
        if blob.sentiment.polarity > 0:
            dougburgum.add(tw["user"]["id"])
    if ("shelley lenz" in tw["retweeted_status"]["full_text"].lower() ):
        blob = TextBlob(tw["retweeted_status"]["full_text"])
        if blob.sentiment.polarity > 0:
            shelleylenz.add(tw["user"]["id"])
    if ("spencer cox" in tw["retweeted_status"]["full_text"].lower() ):
        blob = TextBlob(tw["retweeted_status"]["full_text"])
        if blob.sentiment.polarity > 0:
            spencercox.add(tw["user"]["id"])
    if ("christopher peterson" in tw["retweeted_status"]["full_text"].lower() ):
        blob = TextBlob(tw["retweeted_status"]["full_text"])
        if blob.sentiment.polarity > 0:
            christopherpeterson.add(tw["user"]["id"])
    if ("phil scott" in tw["retweeted_status"]["full_text"].lower() ):
        blob = TextBlob(tw["retweeted_status"]["full_text"])
        if blob.sentiment.polarity > 0:
            philscott.add(tw["user"]["id"])
    if ("david zuckerman" in tw["retweeted_status"]["full_text"].lower() ):
        blob = TextBlob(tw["retweeted_status"]["full_text"])
        if blob.sentiment.polarity > 0:
            davidzuckerman.add(tw["user"]["id"])
    if ("jay inslee" in tw["retweeted_status"]["full_text"].lower() ):
        blob = TextBlob(tw["retweeted_status"]["full_text"])
        if blob.sentiment.polarity > 0:
            jayinslee.add(tw["user"]["id"])
    if ("loren culp" in tw["retweeted_status"]["full_text"].lower() ):
        blob = TextBlob(tw["retweeted_status"]["full_text"])
        if blob.sentiment.polarity > 0:
            lorenculp.add(tw["user"]["id"])
    if ("jim justice" in tw["retweeted_status"]["full_text"].lower() ):
        blob = TextBlob(tw["retweeted_status"]["full_text"])
        if blob.sentiment.polarity > 0:
            jimjustice.add(tw["user"]["id"])
    if ("ben salango" in tw["retweeted_status"]["full_text"].lower() ):
        blob = TextBlob(tw["retweeted_status"]["full_text"])
        if blob.sentiment.polarity > 0:
            bensalango.add(tw["user"]["id"])
    if ("daniel luz" in tw["retweeted_status"]["full_text"].lower() ):
        blob = TextBlob(tw["retweeted_status"]["full_text"])
        if blob.sentiment.polarity > 0:
            danielluz.add(tw["user"]["id"])
cursor = collection.find({"retweeted_status.full_text":{"$exists": "false"}})
for tw in cursor:
    if ("john carney" in tw["full_text"].lower() ):
        blob = TextBlob(tw["full_text"])
        if blob.sentiment.polarity > 0:
            johncarney.add(tw["user"]["id"])
    if ("julianne murray" in tw["full_text"].lower() ):
        blob = TextBlob(tw["full_text"])
        if blob.sentiment.polarity > 0:
            juliannemurray.add(tw["user"]["id"])
    if ("eric holcomb" in tw["full_text"].lower() ):
        blob = TextBlob(tw["full_text"])
        if blob.sentiment.polarity > 0:
            ericholcomb.add(tw["user"]["id"])
    if ("woody myers" in tw["full_text"].lower() ):
        blob = TextBlob(tw["full_text"])
        if blob.sentiment.polarity > 0:
            woodymyers.add(tw["user"]["id"])
    if ("donald rainwater" in tw["full_text"].lower() ):
        blob = TextBlob(tw["full_text"])
        if blob.sentiment.polarity > 0:
            donaldrainwater.add(tw["user"]["id"])
    if ("mike parson" in tw["full_text"].lower() ):
        blob = TextBlob(tw["full_text"])
        if blob.sentiment.polarity > 0:
            mikeparson.add(tw["user"]["id"])
    if ("nicole galloway" in tw["full_text"].lower() ):
        blob = TextBlob(tw["full_text"])
        if blob.sentiment.polarity > 0:
            nicolegalloway.add(tw["user"]["id"])
    if ("mike cooney" in tw["full_text"].lower() ):
        blob = TextBlob(tw["full_text"])
        if blob.sentiment.polarity > 0:
            mikecooney.add(tw["user"]["id"])
    if ("gregg gianforte" in tw["full_text"].lower() ):
        blob = TextBlob(tw["full_text"])
        if blob.sentiment.polarity > 0:
            greggianforte.add(tw["user"]["id"])
    if ("chris sununu" in tw["full_text"].lower() ):
        blob = TextBlob(tw["full_text"])
        if blob.sentiment.polarity > 0:
            chrissununu.add(tw["user"]["id"])
    if ("dan feltes" in tw["full_text"].lower() ):
        blob = TextBlob(tw["full_text"])
        if blob.sentiment.polarity > 0:
            danfeltes.add(tw["user"]["id"])
    if ("roy cooper" in tw["full_text"].lower() ):
        blob = TextBlob(tw["full_text"])
        if blob.sentiment.polarity > 0:
            roycooper.add(tw["user"]["id"])
    if ("dan forest" in tw["full_text"].lower() ):
        blob = TextBlob(tw["full_text"])
        if blob.sentiment.polarity > 0:
            danforest.add(tw["user"]["id"])
    if ("doug burgum" in tw["full_text"].lower() ):
        blob = TextBlob(tw["full_text"])
        if blob.sentiment.polarity > 0:
            dougburgum.add(tw["user"]["id"])
    if ("shelley lenz" in tw["full_text"].lower() ):
        blob = TextBlob(tw["full_text"])
        if blob.sentiment.polarity > 0:
            shelleylenz.add(tw["user"]["id"])
    if ("spencer cox" in tw["full_text"].lower() ):
        blob = TextBlob(tw["full_text"])
        if blob.sentiment.polarity > 0:
            spencercox.add(tw["user"]["id"])
    if ("christopher peterson" in tw["full_text"].lower() ):
        blob = TextBlob(tw["full_text"])
        if blob.sentiment.polarity > 0:
            christopherpeterson.add(tw["user"]["id"])
    if ("phil scott" in tw["full_text"].lower() ):
        blob = TextBlob(tw["full_text"])
        if blob.sentiment.polarity > 0:
            philscott.add(tw["user"]["id"])
    if ("david zuckerman" in tw["full_text"].lower() ):
        blob = TextBlob(tw["full_text"])
        if blob.sentiment.polarity > 0:
            davidzuckerman.add(tw["user"]["id"])
    if ("jay inslee" in tw["full_text"].lower() ):
        blob = TextBlob(tw["full_text"])
        if blob.sentiment.polarity > 0:
            jayinslee.add(tw["user"]["id"])
    if ("loren culp" in tw["full_text"].lower() ):
        blob = TextBlob(tw["full_text"])
        if blob.sentiment.polarity > 0:
            lorenculp.add(tw["user"]["id"])
    if ("jim justice" in tw["full_text"].lower() ):
        blob = TextBlob(tw["full_text"])
        if blob.sentiment.polarity > 0:
            jimjustice.add(tw["user"]["id"])
    if ("ben salango" in tw["full_text"].lower() ):
        blob = TextBlob(tw["full_text"])
        if blob.sentiment.polarity > 0:
            bensalango.add(tw["user"]["id"])
    if ("daniel luz" in tw["full_text"].lower() ):
        blob = TextBlob(tw["full_text"])
        if blob.sentiment.polarity > 0:
            danielluz.add(tw["user"]["id"])

print("Delaware:")
print("John Carney (D): ", (len(johncarney)/(len(johncarney)+len(juliannemurray))))
print("Julianne Murray (R): ", (len(juliannemurray)/(len(johncarney)+len(juliannemurray))))
print("")
print("Indiana:")
print("Eric Holcomb (R): ", (len(ericholcomb)/(len(ericholcomb)+len(woodymyers)+len(donaldrainwater))))
print("Woody Myers (D): ",  (len(woodymyers)/(len(ericholcomb)+len(woodymyers)+len(donaldrainwater))))
print("Donald Rainwater (L): ",  (len(donaldrainwater)/(len(ericholcomb)+len(woodymyers)+len(donaldrainwater))))
print("")
print("Missouri:")
print("Mike Parson (R): ", (len(mikeparson)/(len(mikeparson)+len(nicolegalloway))))
print("Nicole Galloway (D): ", (len(nicolegalloway)/(len(mikeparson)+len(nicolegalloway))))
print("")
print("Montana:")
print("Mike Cooney (D): ", (len(mikecooney)/(len(mikecooney)+len(greggianforte))))
print("Greg Gianforte (R): ", (len(greggianforte)/(len(mikecooney)+len(greggianforte))))
print("")
print("New Hampshire:")
print("Chris Sununu (R): ", (len(chrissununu)/(len(chrissununu)+len(danfeltes))))
print("Dan Feltes (D): ", (len(danfeltes)/(len(chrissununu)+len(danfeltes))))
print("")
print("North Carolina:")
print("Roy Cooper (D): ", (len(roycooper)/(len(roycooper)+len(danforest))))
print("Dan Forest (R): ", (len(danforest)/(len(roycooper)+len(danforest))))
print("")
print("North Dakota:")
print("Doug Burgum (R): ", (len(dougburgum)/(len(dougburgum)+len(shelleylenz))))
print("Shelley Lenz (D): ", (len(shelleylenz)/(len(dougburgum)+len(shelleylenz))))
print("")
print("Utah:")
print("Spencer Cox (R): ", (len(spencercox)/(len(spencercox)+len(christopherpeterson))))
print("Christopher Peterson (D): ", (len(christopherpeterson)/(len(spencercox)+len(christopherpeterson))))
print("")
print("Vermont:")
print("Phil Scott (R): ", (len(philscott)/(len(philscott)+len(davidzuckerman))))
print("David Zuckerman (P): ", (len(davidzuckerman)/(len(philscott)+len(davidzuckerman))))
print("")
print("Washington:")
print("Jay Inslee (D): ", (len(jayinslee)/(len(jayinslee)+len(lorenculp))))
print("Loren Culp (R): ", (len(lorenculp)/(len(jayinslee)+len(lorenculp))))
print("")
print("West Virginia:")
print("Jim Justice (R): ", (len(jimjustice)/(len(jimjustice)+len(bensalango))))
print("Ben Salango (D): ", (len(bensalango)/(len(jimjustice)+len(bensalango))))




