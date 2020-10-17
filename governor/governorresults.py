#this uses sentiment analysis and counts the number of positive tweets for each candidate

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

johncarney, juliannemurray, ericholcomb, woodymyers, donaldrainwater, mikeparson, nicolegalloway, mikecooney, greggianforte, chrissununu, danfeltes, roycooper, danforest, dougburgum, shelleylenz, spencercox = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
christopherpeterson, philscott, davidzuckerman, jayinslee, lorenculp, jimjustice, bensalango, danielluz = 0, 0, 0, 0, 0, 0, 0, 0

client = MongoClient(port=27017)
db=client.TWITTERUSA
collection = db['tweets']
cursor = collection.find({"retweeted_status.full_text":{"$exists": "true"}})
for tw in cursor:
	if ("john carney" in tw["retweeted_status"]["full_text"].lower() ):
		blob = TextBlob(tw["retweeted_status"]["full_text"])
		if blob.sentiment.polarity > 0:
			johncarney += 1
	if ("julianne murray" in tw["retweeted_status"]["full_text"].lower() ):
		blob = TextBlob(tw["retweeted_status"]["full_text"])
		if blob.sentiment.polarity > 0:
			juliannemurray += 1
	if ("eric holcomb" in tw["retweeted_status"]["full_text"].lower() ):
		blob = TextBlob(tw["retweeted_status"]["full_text"])
		if blob.sentiment.polarity > 0:
			ericholcomb += 1
	if ("woody myers" in tw["retweeted_status"]["full_text"].lower() ):
		blob = TextBlob(tw["retweeted_status"]["full_text"])
		if blob.sentiment.polarity > 0:
			woodymyers += 1
	if ("donald rainwater" in tw["retweeted_status"]["full_text"].lower() ):
		blob = TextBlob(tw["retweeted_status"]["full_text"])
		if blob.sentiment.polarity > 0:
			donaldrainwater += 1
	if ("mike parson" in tw["retweeted_status"]["full_text"].lower() ):
		blob = TextBlob(tw["retweeted_status"]["full_text"])
		if blob.sentiment.polarity > 0:
			mikeparson += 1
	if ("nicole galloway" in tw["retweeted_status"]["full_text"].lower() ):
		blob = TextBlob(tw["retweeted_status"]["full_text"])
		if blob.sentiment.polarity > 0:
			nicolegalloway += 1
	if ("mike cooney" in tw["retweeted_status"]["full_text"].lower() ):
		blob = TextBlob(tw["retweeted_status"]["full_text"])
		if blob.sentiment.polarity > 0:
			mikecooney += 1
	if ("gregg gianforte" in tw["retweeted_status"]["full_text"].lower() ):
		blob = TextBlob(tw["retweeted_status"]["full_text"])
		if blob.sentiment.polarity > 0:
			greggianforte += 1
	if ("chris sununu" in tw["retweeted_status"]["full_text"].lower() ):
		blob = TextBlob(tw["retweeted_status"]["full_text"])
		if blob.sentiment.polarity > 0:
			chrissununu += 1
	if ("dan feltes" in tw["retweeted_status"]["full_text"].lower() ):
		blob = TextBlob(tw["retweeted_status"]["full_text"])
		if blob.sentiment.polarity > 0:
			danfeltes += 1
	if ("roy cooper" in tw["retweeted_status"]["full_text"].lower() ):
		blob = TextBlob(tw["retweeted_status"]["full_text"])
		if blob.sentiment.polarity > 0:
			roycooper += 1
	if ("dan forest" in tw["retweeted_status"]["full_text"].lower() ):
		blob = TextBlob(tw["retweeted_status"]["full_text"])
		if blob.sentiment.polarity > 0:
			danforest += 1
	if ("doug burgum" in tw["retweeted_status"]["full_text"].lower() ):
		blob = TextBlob(tw["retweeted_status"]["full_text"])
		if blob.sentiment.polarity > 0:
			dougburgum += 1
	if ("shelley lenz" in tw["retweeted_status"]["full_text"].lower() ):
		blob = TextBlob(tw["retweeted_status"]["full_text"])
		if blob.sentiment.polarity > 0:
			shelleylenz += 1
	if ("spencer cox" in tw["retweeted_status"]["full_text"].lower() ):
		blob = TextBlob(tw["retweeted_status"]["full_text"])
		if blob.sentiment.polarity > 0:
			spencercox += 1
	if ("christopher peterson" in tw["retweeted_status"]["full_text"].lower() ):
		blob = TextBlob(tw["retweeted_status"]["full_text"])
		if blob.sentiment.polarity > 0:
			christopherpeterson += 1
	if ("phil scott" in tw["retweeted_status"]["full_text"].lower() ):
		blob = TextBlob(tw["retweeted_status"]["full_text"])
		if blob.sentiment.polarity > 0:
			philscott += 1
	if ("david zuckerman" in tw["retweeted_status"]["full_text"].lower() ):
		blob = TextBlob(tw["retweeted_status"]["full_text"])
		if blob.sentiment.polarity > 0:
			davidzuckerman += 1
	if ("jay inslee" in tw["retweeted_status"]["full_text"].lower() ):
		blob = TextBlob(tw["retweeted_status"]["full_text"])
		if blob.sentiment.polarity > 0:
			jayinslee += 1
	if ("loren culp" in tw["retweeted_status"]["full_text"].lower() ):
		blob = TextBlob(tw["retweeted_status"]["full_text"])
		if blob.sentiment.polarity > 0:
			lorenculp += 1
	if ("jim justice" in tw["retweeted_status"]["full_text"].lower() ):
		blob = TextBlob(tw["retweeted_status"]["full_text"])
		if blob.sentiment.polarity > 0:
			jimjustice += 1
	if ("ben salango" in tw["retweeted_status"]["full_text"].lower() ):
		blob = TextBlob(tw["retweeted_status"]["full_text"])
		if blob.sentiment.polarity > 0:
			bensalango += 1
	if ("daniel luz" in tw["retweeted_status"]["full_text"].lower() ):
		blob = TextBlob(tw["retweeted_status"]["full_text"])
		if blob.sentiment.polarity > 0:
			danielluz += 1
cursor = collection.find({"retweeted_status.full_text":{"$exists": "false"}})
for tw in cursor:
	if ("john carney" in tw["full_text"].lower() ):
		blob = TextBlob(tw["full_text"])
		if blob.sentiment.polarity > 0:
			johncarney += 1
	if ("julianne murray" in tw["full_text"].lower() ):
		blob = TextBlob(tw["full_text"])
		if blob.sentiment.polarity > 0:
			juliannemurray += 1
	if ("eric holcomb" in tw["full_text"].lower() ):
		blob = TextBlob(tw["full_text"])
		if blob.sentiment.polarity > 0:
			ericholcomb += 1
	if ("woody myers" in tw["full_text"].lower() ):
		blob = TextBlob(tw["full_text"])
		if blob.sentiment.polarity > 0:
			woodymyers += 1
	if ("donald rainwater" in tw["full_text"].lower() ):
		blob = TextBlob(tw["full_text"])
		if blob.sentiment.polarity > 0:
			donaldrainwater += 1
	if ("mike parson" in tw["full_text"].lower() ):
		blob = TextBlob(tw["full_text"])
		if blob.sentiment.polarity > 0:
			mikeparson += 1
	if ("nicole galloway" in tw["full_text"].lower() ):
		blob = TextBlob(tw["full_text"])
		if blob.sentiment.polarity > 0:
			nicolegalloway += 1
	if ("mike cooney" in tw["full_text"].lower() ):
		blob = TextBlob(tw["full_text"])
		if blob.sentiment.polarity > 0:
			mikecooney += 1
	if ("gregg gianforte" in tw["full_text"].lower() ):
		blob = TextBlob(tw["full_text"])
		if blob.sentiment.polarity > 0:
			greggianforte += 1
	if ("chris sununu" in tw["full_text"].lower() ):
		blob = TextBlob(tw["full_text"])
		if blob.sentiment.polarity > 0:
			chrissununu += 1
	if ("dan feltes" in tw["full_text"].lower() ):
		blob = TextBlob(tw["full_text"])
		if blob.sentiment.polarity > 0:
			danfeltes += 1
	if ("roy cooper" in tw["full_text"].lower() ):
		blob = TextBlob(tw["full_text"])
		if blob.sentiment.polarity > 0:
			roycooper += 1
	if ("dan forest" in tw["full_text"].lower() ):
		blob = TextBlob(tw["full_text"])
		if blob.sentiment.polarity > 0:
			danforest += 1
	if ("doug burgum" in tw["full_text"].lower() ):
		blob = TextBlob(tw["full_text"])
		if blob.sentiment.polarity > 0:
			dougburgum += 1
	if ("shelley lenz" in tw["full_text"].lower() ):
		blob = TextBlob(tw["full_text"])
		if blob.sentiment.polarity > 0:
			shelleylenz += 1
	if ("spencer cox" in tw["full_text"].lower() ):
		blob = TextBlob(tw["full_text"])
		if blob.sentiment.polarity > 0:
			spencercox += 1
	if ("christopher peterson" in tw["full_text"].lower() ):
		blob = TextBlob(tw["full_text"])
		if blob.sentiment.polarity > 0:
			christopherpeterson += 1
	if ("phil scott" in tw["full_text"].lower() ):
		blob = TextBlob(tw["full_text"])
		if blob.sentiment.polarity > 0:
			philscott += 1
	if ("david zuckerman" in tw["full_text"].lower() ):
		blob = TextBlob(tw["full_text"])
		if blob.sentiment.polarity > 0:
			davidzuckerman += 1
	if ("jay inslee" in tw["full_text"].lower() ):
		blob = TextBlob(tw["full_text"])
		if blob.sentiment.polarity > 0:
			jayinslee += 1
	if ("loren culp" in tw["full_text"].lower() ):
		blob = TextBlob(tw["full_text"])
		if blob.sentiment.polarity > 0:
			lorenculp += 1
	if ("jim justice" in tw["full_text"].lower() ):
		blob = TextBlob(tw["full_text"])
		if blob.sentiment.polarity > 0:
			jimjustice += 1
	if ("ben salango" in tw["full_text"].lower() ):
		blob = TextBlob(tw["full_text"])
		if blob.sentiment.polarity > 0:
			bensalango += 1
	if ("daniel luz" in tw["full_text"].lower() ):
		blob = TextBlob(tw["full_text"])
		if blob.sentiment.polarity > 0:
			danielluz += 1

print("Delaware:")
print("John Carney (D): ", (johncarney/(johncarney+juliannemurray)))
print("Julianne Murray (R): ", (juliannemurray/(johncarney+juliannemurray)))
print("")
print("Indiana:")
print("Eric Holcomb (R): ", (ericholcomb/(ericholcomb+woodymyers+donaldrainwater)))
print("Woody Myers (D): ",  (woodymyers/(ericholcomb+woodymyers+donaldrainwater)))
print("Donald Rainwater (L): ",  (donaldrainwater/(ericholcomb+woodymyers+donaldrainwater)))
print("")
print("Missouri:")
print("Mike Parson (R): ", (mikeparson/(mikeparson+nicolegalloway)))
print("Nicole Galloway (D): ", (nicolegalloway/(mikeparson+nicolegalloway)))
print("")
print("Montana:")
print("Mike Cooney (D): ", (mikecooney/(mikecooney+greggianforte)))
print("Greg Gianforte (R): ", (greggianforte/(mikecooney+greggianforte)))
print("")
print("New Hampshire:")
print("Chris Sununu (R): ", (chrissununu/(chrissununu+danfeltes)))
print("Dan Feltes (D): ", (danfeltes/(chrissununu+danfeltes)))
print("")
print("North Carolina:")
print("Roy Cooper (D): ", (roycooper/(roycooper+danforest)))
print("Dan Forest (R): ", (danforest/(roycooper+danforest)))
print("")
print("North Dakota:")
print("Doug Burgum (R): ", (dougburgum/(dougburgum+shelleylenz)))
print("Shelley Lenz (D): ", (shelleylenz/(dougburgum+shelleylenz)))
print("")
print("Utah:")
print("Spencer Cox (R): ", (spencercox/(spencercox+christopherpeterson)))
print("Christopher Peterson (D): ", (christopherpeterson/(spencercox+christopherpeterson)))
print("")
print("Vermont:")
print("Phil Scott (R): ", (philscott/(philscott+davidzuckerman)))
print("David Zuckerman (P): ", (davidzuckerman/(philscott+davidzuckerman)))
print("")
print("Washington:")
print("Jay Inslee (D): ", (jayinslee/(jayinslee+lorenculp)))
print("Loren Culp (R): ", (lorenculp/(jayinslee+lorenculp)))
print("")
print("West Virginia:")
print("Jim Justice (R): ", (jimjustice/(jimjustice+bensalango)))
print("Ben Salango (D): ", (bensalango/(jimjustice+bensalango)))




