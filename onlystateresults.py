from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint

trumpmo, bidenmo = set(), set()
trumpco, bidenco = set(), set()
trumpmn, bidenmn = set(), set()
trumpin, bidenin = set(), set()
trumpmd, bidenmd = set(), set()
trumpsd, bidensd = set(), set()
trumpnd, bidennd = set(), set()
trumpde, bidende = set(), set()
trumpne, bidenne = set(), set()
trumpmi, bidenmi = set(), set()
trumpma, bidenma = set(), set()
trumpva, bidenva = set(), set()
trumpme, bidenme, bidenme1, trumpme1, trumpme2, bidenme2 = set(), set(), set(), set(), set(), set()
trumpwi, bidenwi = set(), set()
trumpwv, bidenwv = set(), set()
trumpia, bidenia = set(), set()
trumphi, bidenhi = set(), set() 
trumpri, bidenri = set(), set()
trumpwa, bidenwa = set(), set()
trumpfl, bidenfl = set(), set()
trumpal, bidenal = set(), set()
trumpil, bidenil = set(), set()
trumpca, bidenca = set(), set()
trumpga, bidenga = set(), set()
trumpaz, bidenaz = set(), set()
trumpak, bidenak = set(), set()
trumpar, bidenar = set(), set()
trumpnj, bidennj = set(), set()
trumpnv, bidennv = set(), set() 
trumpnh, bidennh = set(), set()
trumpnc, bidennc = set(), set()
trumptx, bidentx = set(), set()
trumptn, bidentn = set(), set()
trumpnm, bidennm = set(), set()
trumpny, bidenny = set(), set()
trumpwy, bidenwy = set(), set()
trumppa, bidenpa = set(), set()
trumpct, bidenct = set(), set()
trumput, bidenut = set(), set()
trumpoh, bidenoh = set(), set()
trumpor, bidenor = set(), set()

# connect to MongoDB change the << MONGODB URL >> to reflect your own connection string
client = MongoClient(port=27017)
db=client.TWITTERUSA
collection = db['tweets']
cursor = collection.find({"retweeted_status.full_text":{"$exists": "true"}})
for tw in cursor:
	if ("#trump2020" in tw["retweeted_status"]["full_text"].lower() or "#teamtrump" in tw["retweeted_status"]["full_text"].lower() or "#trumpforpresident" in tw["retweeted_status"]["full_text"].lower() or "#kag" in tw["retweeted_status"]["full_text"].lower()  or "#votered" in tw["retweeted_status"]["full_text"].lower() ):
		if(" MO" in tw["user"]["location"] or "missouri" in tw["user"]["location"].lower()):
				trumpmo.add(tw["user"]["id"])
		if(" IA" in tw["user"]["location"] or "iowa" in tw["user"]["location"].lower()):
				trumpia.add(tw["user"]["id"])
		if(" CA" in tw["user"]["location"] or "california" in tw["user"]["location"].lower() or "los angeles" in tw["user"]["location"].lower() or "san francisco" in tw["user"]["location"].lower()):
				trumpca.add(tw["user"]["id"])
		if(" CT" in tw["user"]["location"] or "connecticut" in tw["user"]["location"].lower()):
				trumpct.add(tw["user"]["id"])
		if(" PA" in tw["user"]["location"] or "pennsylvania" in tw["user"]["location"].lower()):
				trumppa.add(tw["user"]["id"])
		if(" OH" in tw["user"]["location"] or "ohio" in tw["user"]["location"].lower()):
				trumpoh.add(tw["user"]["id"])
		if(" FL" in tw["user"]["location"] or "florida" in tw["user"]["location"].lower() or "orlando" in tw["user"]["location"].lower() or "miami" in tw["user"]["location"].lower()):
				trumpfl.add(tw["user"]["id"])
		if(" WA" in tw["user"]["location"] or "washington" in tw["user"]["location"].lower()):
				trumpwa.add(tw["user"]["id"])
		if(" HI" in tw["user"]["location"] or "hawaii" in tw["user"]["location"].lower() or "honolulu" in tw["user"]["location"].lower()):
				trumphi.add(tw["user"]["id"])
		if(" NJ" in tw["user"]["location"] or "new jersey" in tw["user"]["location"].lower()):
				trumpnj.add(tw["user"]["id"])
		if(" NY" in tw["user"]["location"] or "new york" in tw["user"]["location"].lower()):
				trumpny.add(tw["user"]["id"])
		if(" RI" in tw["user"]["location"] or "rhode island" in tw["user"]["location"].lower()):
				trumpri.add(tw["user"]["id"])
		if(" MN" in tw["user"]["location"] or "minnesota" in tw["user"]["location"].lower()):
				trumpmn.add(tw["user"]["id"])
		if(" MI" in tw["user"]["location"] or "michigan" in tw["user"]["location"].lower()):
				trumpmi.add(tw["user"]["id"])
		if(" WI" in tw["user"]["location"] or "wisconsin" in tw["user"]["location"].lower()):
				trumpwi.add(tw["user"]["id"])
		if(" OR" in tw["user"]["location"] or "oregon" in tw["user"]["location"].lower()):
				trumpor.add(tw["user"]["id"])
		if(" MD" in tw["user"]["location"] or "maryland" in tw["user"]["location"].lower()):
				trumpmd.add(tw["user"]["id"])
		if(" MA" in tw["user"]["location"] or "massachusetts" in tw["user"]["location"].lower() or "boston" in tw["user"]["location"].lower()):
				trumpma.add(tw["user"]["id"])
		if(" ME" in tw["user"]["location"] or "maine" in tw["user"]["location"].lower()):
				trumpme.add(tw["user"]["id"])
				if("portland" in tw["user"]["location"].lower() or "augusta" in tw["user"]["location"].lower() or "brunswick" in tw["user"]["location"].lower() or "Saco" in tw["user"]["location"]):
					trumpme1.add(tw["user"]["id"])
				if("lewiston" in tw["user"]["location"].lower() or "bangor" in tw["user"]["location"].lower() or "auburn" in tw["user"]["location"].lower() or "presque isle" in tw["user"]["location"].lower()):
					trumpme2.add(tw["user"]["id"])
		if(" NC" in tw["user"]["location"] or "north carolina" in tw["user"]["location"].lower()):
				trumpnc.add(tw["user"]["id"])
		if(" NH" in tw["user"]["location"] or "new hampshire" in tw["user"]["location"].lower()):
				trumpnh.add(tw["user"]["id"])
		if(" NV" in tw["user"]["location"] or "nevada" in tw["user"]["location"].lower() or "las vegas" in tw["user"]["location"].lower()):
				trumpnv.add(tw["user"]["id"])
		if(" CO" in tw["user"]["location"] or "colorado" in tw["user"]["location"].lower()):
				trumpco.add(tw["user"]["id"])
		if(" NM" in tw["user"]["location"] or "new mexico" in tw["user"]["location"].lower()):
				trumpnm.add(tw["user"]["id"])
		if(" AZ" in tw["user"]["location"] or "arizona" in tw["user"]["location"].lower()):
				trumpaz.add(tw["user"]["id"])
		if(" GA" in tw["user"]["location"] or "georgia" in tw["user"]["location"].lower()):
				trumpga.add(tw["user"]["id"])
		if(" TX" in tw["user"]["location"] or "texas" in tw["user"]["location"].lower()):
				trumptx.add(tw["user"]["id"])
		if(" IN" in tw["user"]["location"] or "indiana" in tw["user"]["location"].lower()):
				trumpin.add(tw["user"]["id"])
		if(" VA" in tw["user"]["location"] or "virginia" in tw["user"]["location"].lower()):
				trumpva.add(tw["user"]["id"])
		if(" IL" in tw["user"]["location"] or "illinois" in tw["user"]["location"].lower() or "chicago" in tw["user"]["location"].lower()):
				trumpil.add(tw["user"]["id"])
		if(" DE" in tw["user"]["location"] or "delaware" in tw["user"]["location"].lower()):
				trumpde.add(tw["user"]["id"])
		if(" UT" in tw["user"]["location"] or "utah" in tw["user"]["location"].lower()):
				trumput.add(tw["user"]["id"])
		if(" NE" in tw["user"]["location"] or "nebraska" in tw["user"]["location"].lower()):
				trumpne.add(tw["user"]["id"])
		if(" AK" in tw["user"]["location"] or "alaska" in tw["user"]["location"].lower()):
				trumpak.add(tw["user"]["id"])
		if(" WY" in tw["user"]["location"] or "wyoming" in tw["user"]["location"].lower()):
				trumpwy.add(tw["user"]["id"])
		if(" AL" in tw["user"]["location"] or "alabama" in tw["user"]["location"].lower()):
				trumpal.add(tw["user"]["id"])
		if(" TN" in tw["user"]["location"] or "tennessee" in tw["user"]["location"].lower()):
				trumptn.add(tw["user"]["id"])
		if(" ND" in tw["user"]["location"] or "north dakota" in tw["user"]["location"].lower()):
				trumpnd.add(tw["user"]["id"])
		if(" SD" in tw["user"]["location"] or "south dakota" in tw["user"]["location"].lower()):
				trumpsd.add(tw["user"]["id"])
		if(" WV" in tw["user"]["location"] or "west virginia" in tw["user"]["location"].lower()):
				trumpwv.add(tw["user"]["id"])
		if(" AR" in tw["user"]["location"] or "arkansas" in tw["user"]["location"].lower()):
				trumpar.add(tw["user"]["id"])
	if ("#biden2020" in tw["retweeted_status"]["full_text"].lower() or "#teamjoe" in tw["retweeted_status"]["full_text"].lower() or "#bidenforpresident" in tw["retweeted_status"]["full_text"].lower()  or "#gojoe"  in tw["retweeted_status"]["full_text"].lower() or "#bluewave2020"  in tw["retweeted_status"]["full_text"].lower() or "#voteblue" in tw["retweeted_status"]["full_text"].lower() ):
		if(" MO" in tw["user"]["location"] or "missouri" in tw["user"]["location"].lower()):
				bidenmo.add(tw["user"]["id"])
		if(" IA" in tw["user"]["location"] or "iowa" in tw["user"]["location"].lower()):
				bidenia.add(tw["user"]["id"])
		if(" CA" in tw["user"]["location"] or "california" in tw["user"]["location"].lower() or "los angeles" in tw["user"]["location"].lower() or "san francisco" in tw["user"]["location"].lower()):
				bidenca.add(tw["user"]["id"])
		if(" CT" in tw["user"]["location"] or "connecticut" in tw["user"]["location"].lower()):
				bidenct.add(tw["user"]["id"])
		if(" PA" in tw["user"]["location"] or "pennsylvania" in tw["user"]["location"].lower()):
				bidenpa.add(tw["user"]["id"])
		if(" OH" in tw["user"]["location"] or "ohio" in tw["user"]["location"].lower()):
				bidenoh.add(tw["user"]["id"])
		if(" FL" in tw["user"]["location"] or "florida" in tw["user"]["location"].lower() or "orlando" in tw["user"]["location"].lower() or "miami" in tw["user"]["location"].lower()):
				bidenfl.add(tw["user"]["id"])
		if(" WA" in tw["user"]["location"] or "washington" in tw["user"]["location"].lower()):
				bidenwa.add(tw["user"]["id"])
		if(" HI" in tw["user"]["location"] or "hawaii" in tw["user"]["location"].lower() or "honolulu" in tw["user"]["location"].lower()):
				bidenhi.add(tw["user"]["id"])
		if(" NJ" in tw["user"]["location"] or "new jersey" in tw["user"]["location"].lower()):
				bidennj.add(tw["user"]["id"])
		if(" NY" in tw["user"]["location"] or "new york" in tw["user"]["location"].lower()):
				bidenny.add(tw["user"]["id"])
		if(" RI" in tw["user"]["location"] or "rhode island" in tw["user"]["location"].lower()):
				bidenri.add(tw["user"]["id"])
		if(" MN" in tw["user"]["location"] or "minnesota" in tw["user"]["location"].lower()):
				bidenmn.add(tw["user"]["id"])
		if(" MI" in tw["user"]["location"] or "michigan" in tw["user"]["location"].lower()):
				bidenmi.add(tw["user"]["id"])
		if(" WI" in tw["user"]["location"] or "wisconsin" in tw["user"]["location"].lower()):
				bidenwi.add(tw["user"]["id"])
		if(" OR" in tw["user"]["location"] or "oregon" in tw["user"]["location"].lower()):
				bidenor.add(tw["user"]["id"])
		if(" MD" in tw["user"]["location"] or "maryland" in tw["user"]["location"].lower()):
				bidenmd.add(tw["user"]["id"])
		if(" MA" in tw["user"]["location"] or "massachusetts" in tw["user"]["location"].lower() or "boston" in tw["user"]["location"].lower()):
				bidenma.add(tw["user"]["id"])
		if(" ME" in tw["user"]["location"] or "maine" in tw["user"]["location"].lower()):
				bidenme.add(tw["user"]["id"])
				if("portland" in tw["user"]["location"].lower() or "augusta" in tw["user"]["location"].lower() or "brunswick" in tw["user"]["location"].lower() or "Saco" in tw["user"]["location"]):
					bidenme1.add(tw["user"]["id"])
				if("lewiston" in tw["user"]["location"].lower() or "bangor" in tw["user"]["location"].lower() or "auburn" in tw["user"]["location"].lower() or "presque isle" in tw["user"]["location"].lower()):
					bidenme2.add(tw["user"]["id"])
		if(" NC" in tw["user"]["location"] or "north carolina" in tw["user"]["location"].lower()):
				bidennc.add(tw["user"]["id"])
		if(" NH" in tw["user"]["location"] or "new hampshire" in tw["user"]["location"].lower()):
				bidennh.add(tw["user"]["id"])
		if(" NV" in tw["user"]["location"] or "nevada" in tw["user"]["location"].lower() or "las vegas" in tw["user"]["location"].lower()):
				bidennv.add(tw["user"]["id"])
		if(" CO" in tw["user"]["location"] or "colorado" in tw["user"]["location"].lower()):
				bidenco.add(tw["user"]["id"])
		if(" NM" in tw["user"]["location"] or "new mexico" in tw["user"]["location"].lower()):
				bidennm.add(tw["user"]["id"])
		if(" AZ" in tw["user"]["location"] or "arizona" in tw["user"]["location"].lower()):
				bidenaz.add(tw["user"]["id"])
		if(" GA" in tw["user"]["location"] or "georgia" in tw["user"]["location"].lower()):
				bidenga.add(tw["user"]["id"])
		if(" TX" in tw["user"]["location"] or "texas" in tw["user"]["location"].lower()):
				bidentx.add(tw["user"]["id"])
		if(" IN" in tw["user"]["location"] or "indiana" in tw["user"]["location"].lower()):
				bidenin.add(tw["user"]["id"])
		if(" VA" in tw["user"]["location"] or "virginia" in tw["user"]["location"].lower()):
				bidenva.add(tw["user"]["id"])
		if(" IL" in tw["user"]["location"] or "illinois" in tw["user"]["location"].lower() or "chicago" in tw["user"]["location"].lower()):
				bidenil.add(tw["user"]["id"])
		if(" DE" in tw["user"]["location"] or "delaware" in tw["user"]["location"].lower()):
				bidende.add(tw["user"]["id"])
		if(" UT" in tw["user"]["location"] or "utah" in tw["user"]["location"].lower()):
				bidenut.add(tw["user"]["id"])
		if(" NE" in tw["user"]["location"] or "nebraska" in tw["user"]["location"].lower()):
				bidenne.add(tw["user"]["id"])
		if(" AK" in tw["user"]["location"] or "alaska" in tw["user"]["location"].lower()):
				bidenak.add(tw["user"]["id"])
		if(" WY" in tw["user"]["location"] or "wyoming" in tw["user"]["location"].lower()):
				bidenwy.add(tw["user"]["id"])
		if(" AL" in tw["user"]["location"] or "alabama" in tw["user"]["location"].lower()):
				bidenal.add(tw["user"]["id"])
		if(" TN" in tw["user"]["location"] or "tennessee" in tw["user"]["location"].lower()):
				bidentn.add(tw["user"]["id"])
		if(" ND" in tw["user"]["location"] or "north dakota" in tw["user"]["location"].lower()):
				bidennd.add(tw["user"]["id"])
		if(" SD" in tw["user"]["location"] or "south dakota" in tw["user"]["location"].lower()):
				bidensd.add(tw["user"]["id"])
		if(" WV" in tw["user"]["location"] or "west virginia" in tw["user"]["location"].lower()):
				bidenwv.add(tw["user"]["id"])
		if(" AR" in tw["user"]["location"] or "arkansas" in tw["user"]["location"].lower()):
				bidenar.add(tw["user"]["id"])
cursor = collection.find({"retweeted_status.full_text":{"$exists": "false"}})
for tw in cursor:
	if ("#trump2020" in tw["full_text"].lower() or "#teamtrump" in tw["full_text"].lower() or "#trumpforpresident" in tw["full_text"].lower()  or "#kag" in tw["full_text"].lower()  or "#votered" in tw["full_text"].lower()):
		if(" MO" in tw["user"]["location"] or "missouri" in tw["user"]["location"].lower()):
				trumpmo.add(tw["user"]["id"])
		if(" IA" in tw["user"]["location"] or "iowa" in tw["user"]["location"].lower()):
				trumpia.add(tw["user"]["id"])
		if(" CA" in tw["user"]["location"] or "california" in tw["user"]["location"].lower() or "los angeles" in tw["user"]["location"].lower() or "san francisco" in tw["user"]["location"].lower()):
				trumpca.add(tw["user"]["id"])
		if(" CT" in tw["user"]["location"] or "connecticut" in tw["user"]["location"].lower()):
				trumpct.add(tw["user"]["id"])
		if(" PA" in tw["user"]["location"] or "pennsylvania" in tw["user"]["location"].lower()):
				trumppa.add(tw["user"]["id"])
		if(" OH" in tw["user"]["location"] or "ohio" in tw["user"]["location"].lower()):
				trumpoh.add(tw["user"]["id"])
		if(" FL" in tw["user"]["location"] or "florida" in tw["user"]["location"].lower() or "orlando" in tw["user"]["location"].lower() or "miami" in tw["user"]["location"].lower()):
				trumpfl.add(tw["user"]["id"])
		if(" WA" in tw["user"]["location"] or "washington" in tw["user"]["location"].lower()):
				trumpwa.add(tw["user"]["id"])
		if(" HI" in tw["user"]["location"] or "hawaii" in tw["user"]["location"].lower() or "honolulu" in tw["user"]["location"].lower()):
				trumphi.add(tw["user"]["id"])
		if(" NJ" in tw["user"]["location"] or "new jersey" in tw["user"]["location"].lower()):
				trumpnj.add(tw["user"]["id"])
		if(" NY" in tw["user"]["location"] or "new york" in tw["user"]["location"].lower()):
				trumpny.add(tw["user"]["id"])
		if(" RI" in tw["user"]["location"] or "rhode island" in tw["user"]["location"].lower()):
				trumpri.add(tw["user"]["id"])
		if(" MN" in tw["user"]["location"] or "minnesota" in tw["user"]["location"].lower()):
				trumpmn.add(tw["user"]["id"])
		if(" MI" in tw["user"]["location"] or "michigan" in tw["user"]["location"].lower()):
				trumpmi.add(tw["user"]["id"])
		if(" WI" in tw["user"]["location"] or "wisconsin" in tw["user"]["location"].lower()):
				trumpwi.add(tw["user"]["id"])
		if(" OR" in tw["user"]["location"] or "oregon" in tw["user"]["location"].lower()):
				trumpor.add(tw["user"]["id"])
		if(" MD" in tw["user"]["location"] or "maryland" in tw["user"]["location"].lower()):
				trumpmd.add(tw["user"]["id"])
		if(" MA" in tw["user"]["location"] or "massachusetts" in tw["user"]["location"].lower() or "boston" in tw["user"]["location"].lower()):
				trumpma.add(tw["user"]["id"])
		if(" ME" in tw["user"]["location"] or "maine" in tw["user"]["location"].lower()):
				trumpme.add(tw["user"]["id"])
				if("portland" in tw["user"]["location"].lower() or "augusta" in tw["user"]["location"].lower() or "brunswick" in tw["user"]["location"].lower() or "Saco" in tw["user"]["location"]):
					trumpme1.add(tw["user"]["id"])
				if("lewiston" in tw["user"]["location"].lower() or "bangor" in tw["user"]["location"].lower() or "auburn" in tw["user"]["location"].lower() or "presque isle" in tw["user"]["location"].lower()):
					trumpme2.add(tw["user"]["id"])
		if(" NC" in tw["user"]["location"] or "north carolina" in tw["user"]["location"].lower()):
				trumpnc.add(tw["user"]["id"])
		if(" NH" in tw["user"]["location"] or "new hampshire" in tw["user"]["location"].lower()):
				trumpnh.add(tw["user"]["id"])
		if(" NV" in tw["user"]["location"] or "nevada" in tw["user"]["location"].lower() or "las vegas" in tw["user"]["location"].lower()):
				trumpnv.add(tw["user"]["id"])
		if(" CO" in tw["user"]["location"] or "colorado" in tw["user"]["location"].lower()):
				trumpco.add(tw["user"]["id"])
		if(" NM" in tw["user"]["location"] or "new mexico" in tw["user"]["location"].lower()):
				trumpnm.add(tw["user"]["id"])
		if(" AZ" in tw["user"]["location"] or "arizona" in tw["user"]["location"].lower()):
				trumpaz.add(tw["user"]["id"])
		if(" GA" in tw["user"]["location"] or "georgia" in tw["user"]["location"].lower()):
				trumpga.add(tw["user"]["id"])
		if(" TX" in tw["user"]["location"] or "texas" in tw["user"]["location"].lower()):
				trumptx.add(tw["user"]["id"])
		if(" IN" in tw["user"]["location"] or "indiana" in tw["user"]["location"].lower()):
				trumpin.add(tw["user"]["id"])
		if(" VA" in tw["user"]["location"] or "virginia" in tw["user"]["location"].lower()):
				trumpva.add(tw["user"]["id"])
		if(" IL" in tw["user"]["location"] or "illinois" in tw["user"]["location"].lower() or "chicago" in tw["user"]["location"].lower()):
				trumpil.add(tw["user"]["id"])
		if(" DE" in tw["user"]["location"] or "delaware" in tw["user"]["location"].lower()):
				trumpde.add(tw["user"]["id"])
		if(" UT" in tw["user"]["location"] or "utah" in tw["user"]["location"].lower()):
				trumput.add(tw["user"]["id"])
		if(" NE" in tw["user"]["location"] or "nebraska" in tw["user"]["location"].lower()):
				trumpne.add(tw["user"]["id"])
		if(" AK" in tw["user"]["location"] or "alaska" in tw["user"]["location"].lower()):
				trumpak.add(tw["user"]["id"])
		if(" WY" in tw["user"]["location"] or "wyoming" in tw["user"]["location"].lower()):
				trumpwy.add(tw["user"]["id"])
		if(" AL" in tw["user"]["location"] or "alabama" in tw["user"]["location"].lower()):
				trumpal.add(tw["user"]["id"])
		if(" TN" in tw["user"]["location"] or "tennessee" in tw["user"]["location"].lower()):
				trumptn.add(tw["user"]["id"])
		if(" ND" in tw["user"]["location"] or "north dakota" in tw["user"]["location"].lower()):
				trumpnd.add(tw["user"]["id"])
		if(" SD" in tw["user"]["location"] or "south dakota" in tw["user"]["location"].lower()):
				trumpsd.add(tw["user"]["id"])
		if(" WV" in tw["user"]["location"] or "west virginia" in tw["user"]["location"].lower()):
				trumpwv.add(tw["user"]["id"])
		if(" AR" in tw["user"]["location"] or "arkansas" in tw["user"]["location"].lower()):
				trumpar.add(tw["user"]["id"])
	if ("#biden2020" in tw["full_text"].lower() or "#teamjoe" in tw["full_text"].lower() or "#bidenforpresident" in tw["full_text"].lower()  or "#gojoe"  in tw["full_text"].lower() or "#bluewave2020"  in tw["full_text"].lower() or "#voteblue" in tw["full_text"].lower() ):
		if(" MO" in tw["user"]["location"] or "missouri" in tw["user"]["location"].lower()):
				bidenmo.add(tw["user"]["id"])
		if(" IA" in tw["user"]["location"] or "iowa" in tw["user"]["location"].lower()):
				bidenia.add(tw["user"]["id"])
		if(" CA" in tw["user"]["location"] or "california" in tw["user"]["location"].lower() or "los angeles" in tw["user"]["location"].lower() or "san francisco" in tw["user"]["location"].lower()):
				bidenca.add(tw["user"]["id"])
		if(" CT" in tw["user"]["location"] or "connecticut" in tw["user"]["location"].lower()):
				bidenct.add(tw["user"]["id"])
		if(" PA" in tw["user"]["location"] or "pennsylvania" in tw["user"]["location"].lower()):
				bidenpa.add(tw["user"]["id"])
		if(" OH" in tw["user"]["location"] or "ohio" in tw["user"]["location"].lower()):
				bidenoh.add(tw["user"]["id"])
		if(" FL" in tw["user"]["location"] or "florida" in tw["user"]["location"].lower() or "orlando" in tw["user"]["location"].lower() or "miami" in tw["user"]["location"].lower()):
				bidenfl.add(tw["user"]["id"])
		if(" WA" in tw["user"]["location"] or "washington" in tw["user"]["location"].lower()):
				bidenwa.add(tw["user"]["id"])
		if(" HI" in tw["user"]["location"] or "hawaii" in tw["user"]["location"].lower() or "honolulu" in tw["user"]["location"].lower()):
				bidenhi.add(tw["user"]["id"])
		if(" NJ" in tw["user"]["location"] or "new jersey" in tw["user"]["location"].lower()):
				bidennj.add(tw["user"]["id"])
		if(" NY" in tw["user"]["location"] or "new york" in tw["user"]["location"].lower()):
				bidenny.add(tw["user"]["id"])
		if(" RI" in tw["user"]["location"] or "rhode island" in tw["user"]["location"].lower()):
				bidenri.add(tw["user"]["id"])
		if(" MN" in tw["user"]["location"] or "minnesota" in tw["user"]["location"].lower()):
				bidenmn.add(tw["user"]["id"])
		if(" MI" in tw["user"]["location"] or "michigan" in tw["user"]["location"].lower()):
				bidenmi.add(tw["user"]["id"])
		if(" WI" in tw["user"]["location"] or "wisconsin" in tw["user"]["location"].lower()):
				bidenwi.add(tw["user"]["id"])
		if(" OR" in tw["user"]["location"] or "oregon" in tw["user"]["location"].lower()):
				bidenor.add(tw["user"]["id"])
		if(" MD" in tw["user"]["location"] or "maryland" in tw["user"]["location"].lower()):
				bidenmd.add(tw["user"]["id"])
		if(" MA" in tw["user"]["location"] or "massachusetts" in tw["user"]["location"].lower() or "boston" in tw["user"]["location"].lower()):
				bidenma.add(tw["user"]["id"])
		if(" ME" in tw["user"]["location"] or "maine" in tw["user"]["location"].lower()):
				bidenme.add(tw["user"]["id"])
				if("portland" in tw["user"]["location"].lower() or "augusta" in tw["user"]["location"].lower() or "brunswick" in tw["user"]["location"].lower() or "Saco" in tw["user"]["location"]):
					bidenme1.add(tw["user"]["id"])
				if("lewiston" in tw["user"]["location"].lower() or "bangor" in tw["user"]["location"].lower() or "auburn" in tw["user"]["location"].lower() or "presque isle" in tw["user"]["location"].lower()):
					bidenme2.add(tw["user"]["id"])
		if(" NC" in tw["user"]["location"] or "north carolina" in tw["user"]["location"].lower()):
				bidennc.add(tw["user"]["id"])
		if(" NH" in tw["user"]["location"] or "new hampshire" in tw["user"]["location"].lower()):
				bidennh.add(tw["user"]["id"])
		if(" NV" in tw["user"]["location"] or "nevada" in tw["user"]["location"].lower() or "las vegas" in tw["user"]["location"].lower()):
				bidennv.add(tw["user"]["id"])
		if(" CO" in tw["user"]["location"] or "colorado" in tw["user"]["location"].lower()):
				bidenco.add(tw["user"]["id"])
		if(" NM" in tw["user"]["location"] or "new mexico" in tw["user"]["location"].lower()):
				bidennm.add(tw["user"]["id"])
		if(" AZ" in tw["user"]["location"] or "arizona" in tw["user"]["location"].lower()):
				bidenaz.add(tw["user"]["id"])
		if(" GA" in tw["user"]["location"] or "georgia" in tw["user"]["location"].lower()):
				bidenga.add(tw["user"]["id"])
		if(" TX" in tw["user"]["location"] or "texas" in tw["user"]["location"].lower()):
				bidentx.add(tw["user"]["id"])
		if(" IN" in tw["user"]["location"] or "indiana" in tw["user"]["location"].lower()):
				bidenin.add(tw["user"]["id"])
		if(" VA" in tw["user"]["location"] or "virginia" in tw["user"]["location"].lower()):
				bidenva.add(tw["user"]["id"])
		if(" IL" in tw["user"]["location"] or "illinois" in tw["user"]["location"].lower() or "chicago" in tw["user"]["location"].lower()):
				bidenil.add(tw["user"]["id"])
		if(" DE" in tw["user"]["location"] or "delaware" in tw["user"]["location"].lower()):
				bidende.add(tw["user"]["id"])
		if(" UT" in tw["user"]["location"] or "utah" in tw["user"]["location"].lower()):
				bidenut.add(tw["user"]["id"])
		if(" NE" in tw["user"]["location"] or "nebraska" in tw["user"]["location"].lower()):
				bidenne.add(tw["user"]["id"])
		if(" AK" in tw["user"]["location"] or "alaska" in tw["user"]["location"].lower()):
				bidenak.add(tw["user"]["id"])
		if(" WY" in tw["user"]["location"] or "wyoming" in tw["user"]["location"].lower()):
				bidenwy.add(tw["user"]["id"])
		if(" AL" in tw["user"]["location"] or "alabama" in tw["user"]["location"].lower()):
				bidenal.add(tw["user"]["id"])
		if(" TN" in tw["user"]["location"] or "tennessee" in tw["user"]["location"].lower()):
				bidentn.add(tw["user"]["id"])
		if(" ND" in tw["user"]["location"] or "north dakota" in tw["user"]["location"].lower()):
				bidennd.add(tw["user"]["id"])
		if(" SD" in tw["user"]["location"] or "south dakota" in tw["user"]["location"].lower()):
				bidensd.add(tw["user"]["id"])
		if(" WV" in tw["user"]["location"] or "west virginia" in tw["user"]["location"].lower()):
				bidenwv.add(tw["user"]["id"])
		if(" AR" in tw["user"]["location"] or "arkansas" in tw["user"]["location"].lower()):
				bidenar.add(tw["user"]["id"])

 
if(len(trumpmo) > 0 or len(bidenmo) > 0):
   print("Missouri")
   print("Trump: ",(len(trumpmo)/(len(trumpmo)+len(bidenmo))))
   print("Biden: ",(len(bidenmo)/(len(trumpmo)+len(bidenmo))))
 
if(len(trumpco) > 0 or len(bidenco) > 0):
   print("Colorado")
   print("Trump: ",(len(trumpco)/(len(trumpco)+len(bidenco))))
   print("Biden: ",(len(bidenco)/(len(trumpco)+len(bidenco))))
 
if(len(trumpmn) > 0 or len(bidenmn) > 0):
   print("Minnesota")
   print("Trump: ",(len(trumpmn)/(len(trumpmn)+len(bidenmn))))
   print("Biden: ",(len(bidenmn)/(len(trumpmn)+len(bidenmn))))
 
if(len(trumpin) > 0 or len(bidenin) > 0):
   print("Indiana")
   print("Trump: ", (len(trumpin)/(len(trumpin)+len(bidenin))))
   print("Biden: ",(len(bidenin)/(len(trumpin)+len(bidenin))))
   print("")
 
if(len(trumpme) > 0 or len(bidenme) > 0):
   print("Maine")
   print("Trump: ", (len(trumpme)/(len(trumpme)+len(bidenme))))
   print("Biden: ",(len(bidenme)/(len(trumpme)+len(bidenme))))
 
if(len(trumpme) > 0 or len(bidenme) > 0):
   print("Maine 1")
   print("Trump: ", (len(trumpme1)/(len(trumpme1)+len(bidenme1))))
   print("votes ", len(trumpme1))
   print("Biden: ",(len(bidenme1)/(len(trumpme1)+len(bidenme1))))
   print("votes ", len(bidenme1))
 
if(len(trumpme) > 0 or len(bidenme) > 0):
   print("Maine 2")
   print("Trump: ",(len(trumpme2)/(len(trumpme2)+len(bidenme2))))
   print("votes ", len(trumpme2))
   print("Biden: ",(len(bidenme2)/(len(trumpme2)+len(bidenme2))))
   print("votes ", len(bidenme2))
   print("")
 
if(len(trumpde) > 0 or len(bidende) > 0):
   print("Delaware")
   print("Trump: ",(len(trumpde)/(len(trumpde)+len(bidende))))
   print("Biden: ",(len(bidende)/(len(trumpde)+len(bidende))))
 
if(len(trumpmd) > 0 or len(bidenmd) > 0):
   print("Maryland")
   print("Trump: ",(len(trumpmd)/(len(trumpmd)+len(bidenmd))))
   print("Biden: ",(len(bidenmd)/(len(trumpmd)+len(bidenmd))))
 
if(len(trumpsd) > 0 or len(bidensd) > 0):
   print("South Dakota")
   print("Trump: ",(len(trumpsd)/(len(trumpsd)+len(bidensd))))
   print("Biden: ",(len(bidensd)/(len(trumpsd)+len(bidensd))))
 
if(len(trumpma) > 0 or len(bidenma) > 0):
   print("Massachusetts")
   print("Trump: ",(len(trumpma)/(len(trumpma)+len(bidenma))))
   print("Biden: ",(len(bidenma)/(len(trumpma)+len(bidenma))))
 
if(len(trumpmi) > 0 or len(bidenmi) > 0):
   print("Michigan")
   print("Trump: ",(len(trumpmi)/(len(trumpmi)+len(bidenmi))))
   print("Biden: ",(len(bidenmi)/(len(trumpmi)+len(bidenmi))))
 
if(len(trumpca) > 0 or len(bidenca) > 0):
   print("California")
   print("Trump: ",(len(trumpca)/(len(trumpca)+len(bidenca))))
   print("Biden: ",(len(bidenca)/(len(trumpca)+len(bidenca))))
 
if(len(trumpva) > 0 or len(bidenva) > 0):
   print("Virginia")
   print("Trump: ",(len(trumpva)/(len(trumpva)+len(bidenva))))
   print("Biden: ",(len(bidenva)/(len(trumpva)+len(bidenva))))
 
if(len(trumpga) > 0 or len(bidenga) > 0):
   print("Georgia")
   print("Trump: ",(len(trumpga)/(len(trumpga)+len(bidenga))))
   print("Biden: ",(len(bidenga)/(len(trumpga)+len(bidenga))))
 
if(len(trumpfl) > 0 or len(bidenfl) > 0):
   print("Florida")
   print("Trump: ",(len(trumpfl)/(len(trumpfl)+len(bidenfl))))
   print("Biden: ",(len(bidenfl)/(len(trumpfl)+len(bidenfl))))
 
if(len(trumppa) > 0 or len(bidenpa) > 0):
   print("Pennsylvania")
   print("Trump: ",(len(trumppa)/(len(trumppa)+len(bidenpa))))
   print("Biden: ",(len(bidenpa)/(len(trumppa)+len(bidenpa))))
 
if(len(trumpaz) > 0 or len(bidenaz) > 0):
   print("Arizona")
   print("Trump: ",(len(trumpaz)/(len(trumpaz)+len(bidenaz))))
   print("Biden: ",(len(bidenaz)/(len(trumpaz)+len(bidenaz))))
 
if(len(trumpar) > 0 or len(bidenar) > 0):
   print("Arkansas")
   print("Trump: ",(len(trumpar)/(len(trumpar)+len(bidenar))))
   print("Biden: ",(len(bidenar)/(len(trumpar)+len(bidenar))))
 
if(len(trumpak) > 0 or len(bidenak) > 0):
   print("Alaska")
   print("Trump: ",(len(trumpak)/(len(trumpak)+len(bidenak))))
   print("Biden: ",(len(bidenak)/(len(trumpak)+len(bidenak))))
 
if(len(trumpal) > 0 or len(bidenal) > 0):
   print("Alabama")
   print("Trump: ",(len(trumpal)/(len(trumpal)+len(bidenal))))
   print("Biden: ",(len(bidenal)/(len(trumpal)+len(bidenal))))
 
if(len(trumpwa) > 0 or len(bidenwa) > 0):
   print("Washington")
   print("Trump: ",(len(trumpwa)/(len(trumpwa)+len(bidenwa))))
   print("Biden: ",(len(bidenwa)/(len(trumpwa)+len(bidenwa))))
   print("")
 
if(len(trumpwv) > 0 or len(bidenwv) > 0):
   print("West Virginia")
   print("Trump: ",(len(trumpwv)/(len(trumpwv)+len(bidenwv))))
   print("Biden: ",(len(bidenwv)/(len(trumpwv)+len(bidenwv))))
 
 
if(len(trumpnj) > 0 or len(bidennj) > 0):
   print("New Jersey")
   print("Trump: ",(len(trumpnj)/(len(trumpnj)+len(bidennj))))
   print("Biden: ",(len(bidennj)/(len(trumpnj)+len(bidennj))))
 
if(len(trumpnm) > 0 or len(bidennm) > 0):
   print("New Mexico")
   print("Trump: ",(len(trumpnm)/(len(trumpnm)+len(bidennm))))
   print("Biden: ",(len(bidennm)/(len(trumpnm)+len(bidennm))))
 
if(len(trumpne) > 0 or len(bidenne) > 0):
   print("Nebraska")
   print("Trump: ",(len(trumpne)/(len(trumpne)+len(bidenne))))
   print("Biden: ",(len(bidenne)/(len(trumpne)+len(bidenne))))
 
if(len(trumpnh) > 0 or len(bidennh) > 0):
   print("New Hampshire")
   print("Trump: ",(len(trumpnh)/(len(trumpnh)+len(bidennh))))
   print("Biden: ",(len(bidennh)/(len(trumpnh)+len(bidennh))))
   print("")
 
if(len(trumpnv) > 0 or len(bidennv) > 0):
   print("Nevada")
   print("Trump: ",(len(trumpnv)/(len(trumpnv)+len(bidennv))))
   print("Biden: ",(len(bidennv)/(len(trumpnv)+len(bidennv))))
   print("")
 
if(len(trumpnc) > 0 or len(bidennc) > 0):
   print("North Carolina")
   print("Trump: ",(len(trumpnc)/(len(trumpnc)+len(bidennc))))
   print("Biden: ",(len(bidennc)/(len(trumpnc)+len(bidennc))))
 
if(len(trumpny) > 0 or len(bidenny) > 0):
   print("New York")
   print("Trump: ",(len(trumpny)/(len(trumpny)+len(bidenny))))
   print("Biden: ",(len(bidenny)/(len(trumpny)+len(bidenny))))
 
if(len(trumpnd) > 0 or len(bidennd) > 0):
   print("North Dakota")
   print("Trump: ",(len(trumpnd)/(len(trumpnd)+len(bidennd))))
   print("Biden: ",(len(bidennd)/(len(trumpnd)+len(bidennd))))
 
if(len(trumpwy) > 0 or len(bidenwy) > 0):
   print("Wyoming")
   print("Trump: ",(len(trumpwy)/(len(trumpwy)+len(bidenwy))))
   print("Biden: ",(len(bidenwy)/(len(trumpwy)+len(bidenwy))))
 
if(len(trumpoh) > 0 or len(bidenoh) > 0):
   print("Ohio")
   print("Trump: ",(len(trumpoh)/(len(trumpoh)+len(bidenoh))))
   print("Biden: ",(len(bidenoh)/(len(trumpoh)+len(bidenoh))))
 
if(len(trumpor) > 0 or len(bidenor) > 0):
   print("Oregon")
   print("Trump: ",(len(trumpor)/(len(trumpor)+len(bidenor))))
   print("Biden: ",(len(bidenor)/(len(trumpor)+len(bidenor))))
   print("")
 
if(len(trumphi) > 0 or len(bidenhi) > 0):
   print("Hawaii")
   print("Trump: ",(len(trumphi)/(len(trumphi)+len(bidenhi))))
   print("Biden: ",(len(bidenhi)/(len(trumphi)+len(bidenhi))))
   print("")
 
if(len(trumptx) > 0 or len(bidentx) > 0):
   print("Texas")
   print("Trump: ",(len(trumptx)/(len(trumptx)+len(bidentx))))
   print("Biden: ",(len(bidentx)/(len(trumptx)+len(bidentx))))
 
if(len(trumptn) > 0 or len(bidentn) > 0):
   print("Tennessee")
   print("Trump: ",(len(trumptn)/(len(trumptn)+len(bidentn))))
   print("Biden: ",(len(bidentn)/(len(trumptn)+len(bidentn))))
 
if(len(trumpwi) > 0 or len(bidenwi) > 0):
   print("Wisconsin")
   print("Trump: ",(len(trumpwi)/(len(trumpwi)+len(bidenwi))))
   print("Biden: ",(len(bidenwi)/(len(trumpwi)+len(bidenwi))))
 
if(len(trumpri) > 0 or len(bidenri) > 0):
   print("Rhode Island")
   print("Trump: ",(len(trumpri)/(len(trumpri)+len(bidenri))))
   print("Biden: ",(len(bidenri)/(len(trumpri)+len(bidenri))))
 
if(len(trumpct) > 0 or len(bidenct) > 0):
   print("Connecticut")
   print("Trump: ",(len(trumpct)/(len(trumpct)+len(bidenct))))
   print("Biden: ",(len(bidenct)/(len(trumpct)+len(bidenct))))
 
if(len(trumput) > 0 or len(bidenut) > 0):
   print("Utah")
   print("Trump: ",(len(trumput)/(len(trumput)+len(bidenut))))
   print("Biden: ",(len(bidenut)/(len(trumput)+len(bidenut))))
 
if(len(trumpia) > 0 or len(bidenia) > 0):
   print("Iowa")
   print("Trump: ",(len(trumpia)/(len(trumpia)+len(bidenia))))
   print("Biden: ",(len(bidenia)/(len(trumpia)+len(bidenia))))
 
if(len(trumpil) > 0 or len(bidenil) > 0):
   print("Illinois")
   print("Trump: ",(len(trumpil)/(len(trumpil)+len(bidenil))))
   print("Biden: ",(len(bidenil)/(len(trumpil)+len(bidenil))))
