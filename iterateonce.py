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
trumpme, bidenme, trumpme1, bidenme1, trumpme2, bidenme2 = set(), set(), set(), set(), set(), set()
trumpwi, bidenwi = set(), set()
trumpwv, bidenwv, trumpwv1, bidenwv1, trumpwv2, bidenwv2, trumpwv3, bidenwv3 = set(), set(), set(), set(), set(), set(), set(), set()
trumpia, bidenia = set(), set()
trumphi, bidenhi, trumphi1, bidenhi1, trumphi2, bidenhi2 = set(), set(), set(), set(), set(), set()
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
trumpnv, bidennv, trumpclarknv, bidenclarknv, trumplincolnnv, bidenlincolnnv, trumpesmeraldanv, bidenesmeraldanv, trumpnyenv, bidennyenv, trumpmineralnv, bidenmineralnv, trumpdouglasnv, bidendouglasnv, trumpcarsoncitynv, bidencarsoncitynv, trumplyonnv, bidenlyonnv, trumpstoreynv, bidenstoreynv, trumpwhitepinenv, bidenwhitepinenv, trumpchurchillnv, bidenchurchillnv, trumpeurekanv, bideneurekanv, trumplandernv, bidenlandernv, trumpwashoenv, bidenwashoenv, trumphumboldtnv, bidenhumboldtnv, trumpelkonv, bidenelkonv, trumppershingnv, bidenpershingnv = set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set(), set()
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

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient(port=27017)
db=client.TWITTERUSA
collection = db['tweets']
cursor = collection.find({"retweeted_status.full_text":{"$exists": "true"}})
for tw in cursor:
	if ("#trump2020" in tw["retweeted_status"]["full_text"].lower() or "#teamtrump" in tw["retweeted_status"]["full_text"].lower() or "#trumpforpresident" in tw["retweeted_status"]["full_text"].lower() ):
		if(", MO" in tw["user"]["location"] or "missouri" in tw["user"]["location"].lower()):
				trumpmo.add(tw["user"]["id"])
		if(", IA" in tw["user"]["location"] or "iowa" in tw["user"]["location"].lower()):
				trumpia.add(tw["user"]["id"])
		if(", CA" in tw["user"]["location"] or "california" in tw["user"]["location"].lower() or "los angeles" in tw["user"]["location"].lower() or "san francisco" in tw["user"]["location"].lower()):
				trumpca.add(tw["user"]["id"])
		if(", CT" in tw["user"]["location"] or "connecticut" in tw["user"]["location"].lower()):
				trumpct.add(tw["user"]["id"])
		if(", PA" in tw["user"]["location"] or "pennsylvania" in tw["user"]["location"].lower()):
				trumppa.add(tw["user"]["id"])
		if(", OH" in tw["user"]["location"] or "ohio" in tw["user"]["location"].lower()):
				trumpoh.add(tw["user"]["id"])
		if(", FL" in tw["user"]["location"] or "florida" in tw["user"]["location"].lower() or "orlando" in tw["user"]["location"].lower() or "miami" in tw["user"]["location"].lower()):
				trumpfl.add(tw["user"]["id"])
		if(", WA" in tw["user"]["location"] or "washington" in tw["user"]["location"].lower()):
				trumpwa.add(tw["user"]["id"])
		if(", HI" in tw["user"]["location"] or "hawaii" in tw["user"]["location"].lower() or "honolulu" in tw["user"]["location"].lower()):
				trumphi.add(tw["user"]["id"])
				if("honolulu" in tw["user"]["location"].lower() or "ewa gentry" in tw["user"]["location"].lower() or "mililani" in tw["user"]["location"].lower() or "pearl city" in tw["user"]["location"].lower() or "waipahu" in tw["user"]["location"].lower()):
					trumphi1.add(tw["user"]["id"])
				if("Hilo" in tw["user"]["location"] or "kailua" in tw["user"]["location"].lower() or "kaneoha" in tw["user"]["location"].lower() or "kahului" in tw["user"]["location"].lower() or "Kihei" in tw["user"]["location"]):
					trumphi2.add(tw["user"]["id"])
		if(", NJ" in tw["user"]["location"] or "new jersey" in tw["user"]["location"].lower()):
				trumpnj.add(tw["user"]["id"])
		if(", NY" in tw["user"]["location"] or "new york" in tw["user"]["location"].lower()):
				trumpny.add(tw["user"]["id"])
		if(", RI" in tw["user"]["location"] or "rhode island" in tw["user"]["location"].lower()):
				trumpri.add(tw["user"]["id"])
		if(", MN" in tw["user"]["location"] or "minnesota" in tw["user"]["location"].lower()):
				trumpmn.add(tw["user"]["id"])
		if(", MI" in tw["user"]["location"] or "michigan" in tw["user"]["location"].lower()):
				trumpmi.add(tw["user"]["id"])
		if(", WI" in tw["user"]["location"] or "wisconsin" in tw["user"]["location"].lower()):
				trumpwi.add(tw["user"]["id"])
		if(", OR" in tw["user"]["location"] or "oregon" in tw["user"]["location"].lower()):
				trumpor.add(tw["user"]["id"])
		if(", MD" in tw["user"]["location"] or "maryland" in tw["user"]["location"].lower()):
				trumpmd.add(tw["user"]["id"])
		if(", MA" in tw["user"]["location"] or "massachusetts" in tw["user"]["location"].lower() or "boston" in tw["user"]["location"].lower()):
				trumpma.add(tw["user"]["id"])
		if(", ME" in tw["user"]["location"] or "maine" in tw["user"]["location"].lower()):
				trumpme.add(tw["user"]["id"])
				if("portland" in tw["user"]["location"].lower() or "augusta" in tw["user"]["location"].lower() or "brunswick" in tw["user"]["location"].lower() or "Saco" in tw["user"]["location"]):
					trumpme1.add(tw["user"]["id"])
				if("lewiston" in tw["user"]["location"].lower() or "bangor" in tw["user"]["location"].lower() or "auburn" in tw["user"]["location"].lower() or "presque isle" in tw["user"]["location"].lower()):
					trumpme2.add(tw["user"]["id"])
		if(", NC" in tw["user"]["location"] or "north carolina" in tw["user"]["location"].lower()):
				trumpnc.add(tw["user"]["id"])
		if(", NH" in tw["user"]["location"] or "new hampshire" in tw["user"]["location"].lower()):
				trumpnh.add(tw["user"]["id"])
		if(", NV" in tw["user"]["location"] or "nevada" in tw["user"]["location"].lower() or "las vegas" in tw["user"]["location"].lower()):
				trumpnv.add(tw["user"]["id"])
				if("washoe county" in tw["user"]["location"].lower() or "Reno" in tw["user"]["location"]):
					trumpwashoenv.add(tw["user"]["id"])
				if("humboldt county" in tw["user"]["location"].lower() or "winnemucca" in tw["user"]["location"].lower()):
					trumphumboldtnv.add(tw["user"]["id"])
				if("elko county" in tw["user"]["location"].lower() or "Elko" in tw["user"]["location"]):
					trumpelkonv.add(tw["user"]["id"])
				if("pershing county" in tw["user"]["location"].lower() or "lovelock" in tw["user"]["location"].lower()):
					trumppershingnv.add(tw["user"]["id"])
				if("lander county" in tw["user"]["location"].lower() or "battle mountain" in tw["user"]["location"].lower()):
					trumplandernv.add(tw["user"]["id"])
				if("eureka county" in tw["user"]["location"].lower() or "eureka" in tw["user"]["location"].lower()):
					trumpeurekanv.add(tw["user"]["id"])
				if("churchill county" in tw["user"]["location"].lower() or "fallon" in tw["user"]["location"].lower()):
					trumpchurchillnv.add(tw["user"]["id"])
				if("white pine county" in tw["user"]["location"].lower() or "Ely" in tw["user"]["location"]):
					trumpwhitepinenv.add(tw["user"]["id"])
				if("storey county" in tw["user"]["location"].lower() or "virginia city" in tw["user"]["location"].lower()):
					trumpstoreynv.add(tw["user"]["id"])
				if("lyon county" in tw["user"]["location"].lower() or "fernley" in tw["user"]["location"].lower()):
					trumplyonnv.add(tw["user"]["id"])
				if("carson city" in tw["user"]["location"].lower()):
					trumpcarsoncitynv.add(tw["user"]["id"])
				if("douglas county" in tw["user"]["location"].lower() or "gardnerville ranchos" in tw["user"]["location"].lower()):
					trumpdouglasnv.add(tw["user"]["id"])
				if("mineral county" in tw["user"]["location"].lower() or "hawthorne" in tw["user"]["location"].lower()):
					trumpmineralnv.add(tw["user"]["id"])
				if("nye county" in tw["user"]["location"].lower() or "pahrump" in tw["user"]["location"].lower()):
					trumpnyenv.add(tw["user"]["id"])
				if("esmeralda county" in tw["user"]["location"].lower() or "goldfield" in tw["user"]["location"].lower()):
					trumpesmeraldanv.add(tw["user"]["id"])
				if("lincoln county" in tw["user"]["location"].lower() or "caliente" in tw["user"]["location"].lower()):
					trumplincolnnv.add(tw["user"]["id"])
				if("clark county" in tw["user"]["location"].lower() or "las vegas" in tw["user"]["location"].lower()):
					trumpclarknv.add(tw["user"]["id"])
		if(", CO" in tw["user"]["location"] or "colorado" in tw["user"]["location"].lower()):
				trumpco.add(tw["user"]["id"])
		if(", NM" in tw["user"]["location"] or "new mexico" in tw["user"]["location"].lower()):
				trumpnm.add(tw["user"]["id"])
		if(", AZ" in tw["user"]["location"] or "arizona" in tw["user"]["location"].lower()):
				trumpaz.add(tw["user"]["id"])
		if(", GA" in tw["user"]["location"] or "georgia" in tw["user"]["location"].lower()):
				trumpga.add(tw["user"]["id"])
		if(", TX" in tw["user"]["location"] or "texas" in tw["user"]["location"].lower()):
				trumptx.add(tw["user"]["id"])
		if(", IN" in tw["user"]["location"] or "indiana" in tw["user"]["location"].lower()):
				trumpin.add(tw["user"]["id"])
		if(", VA" in tw["user"]["location"] or "virginia" in tw["user"]["location"].lower()):
				trumpva.add(tw["user"]["id"])
		if(", IL" in tw["user"]["location"] or "illinois" in tw["user"]["location"].lower() or "chicago" in tw["user"]["location"].lower()):
				trumpil.add(tw["user"]["id"])
		if(", DE" in tw["user"]["location"] or "delaware" in tw["user"]["location"].lower()):
				trumpde.add(tw["user"]["id"])
		if(", UT" in tw["user"]["location"] or "utah" in tw["user"]["location"].lower()):
				trumput.add(tw["user"]["id"])
		if(", NE" in tw["user"]["location"] or "nebraska" in tw["user"]["location"].lower()):
				trumpne.add(tw["user"]["id"])
		if(", AK" in tw["user"]["location"] or "alaska" in tw["user"]["location"].lower()):
				trumpak.add(tw["user"]["id"])
		if(", WY" in tw["user"]["location"] or "wyoming" in tw["user"]["location"].lower()):
				trumpwy.add(tw["user"]["id"])
		if(", AL" in tw["user"]["location"] or "alabama" in tw["user"]["location"].lower()):
				trumpal.add(tw["user"]["id"])
		if(", TN" in tw["user"]["location"] or "tennessee" in tw["user"]["location"].lower()):
				trumptn.add(tw["user"]["id"])
		if(", ND" in tw["user"]["location"] or "north dakota" in tw["user"]["location"].lower()):
				trumpnd.add(tw["user"]["id"])
		if(", SD" in tw["user"]["location"] or "south dakota" in tw["user"]["location"].lower()):
				trumpsd.add(tw["user"]["id"])
		if(", WV" in tw["user"]["location"] or "west virginia" in tw["user"]["location"].lower()):
				trumpwv.add(tw["user"]["id"])
				if("morgantown" in tw["user"]["location"].lower() or "parkersburg" in tw["user"]["location"].lower() or "wheeling" in tw["user"]["location"].lower() or "weirton" in tw["user"]["location"].lower() or "fairmont" in tw["user"]["location"].lower()):
					trumpwv1.add(tw["user"]["id"])
				if("charleston" in tw["user"]["location"].lower() or "martinsburg" in tw["user"]["location"].lower() or "teays valley" in tw["user"]["location"].lower() or "south charleston" in tw["user"]["location"].lower() or "saint albans" in tw["user"]["location"].lower()):
					trumpwv2.add(tw["user"]["id"])
				if("huntington" in tw["user"]["location"].lower() or "beckley" in tw["user"]["location"].lower() or "bluefield" in tw["user"]["location"].lower() or "oak hill" in tw["user"]["location"].lower() or "pea ridge" in tw["user"]["location"].lower()):
					trumpwv3.add(tw["user"]["id"])
		if(", AR" in tw["user"]["location"] or "arkansas" in tw["user"]["location"].lower()):
				trumpar.add(tw["user"]["id"])
	if ("#biden2020" in tw["retweeted_status"]["full_text"].lower() or "#teamjoe" in tw["retweeted_status"]["full_text"].lower() or "#bidenforpresident" in tw["retweeted_status"]["full_text"].lower() ):
		if(", MO" in tw["user"]["location"] or "missouri" in tw["user"]["location"].lower()):
				bidenmo.add(tw["user"]["id"])
		if(", IA" in tw["user"]["location"] or "iowa" in tw["user"]["location"].lower()):
				bidenia.add(tw["user"]["id"])
		if(", CA" in tw["user"]["location"] or "california" in tw["user"]["location"].lower() or "los angeles" in tw["user"]["location"].lower() or "san francisco" in tw["user"]["location"].lower()):
				bidenca.add(tw["user"]["id"])
		if(", CT" in tw["user"]["location"] or "connecticut" in tw["user"]["location"].lower()):
				bidenct.add(tw["user"]["id"])
		if(", PA" in tw["user"]["location"] or "pennsylvania" in tw["user"]["location"].lower()):
				bidenpa.add(tw["user"]["id"])
		if(", OH" in tw["user"]["location"] or "ohio" in tw["user"]["location"].lower()):
				bidenoh.add(tw["user"]["id"])
		if(", FL" in tw["user"]["location"] or "florida" in tw["user"]["location"].lower() or "orlando" in tw["user"]["location"].lower() or "miami" in tw["user"]["location"].lower()):
				bidenfl.add(tw["user"]["id"])
		if(", WA" in tw["user"]["location"] or "washington" in tw["user"]["location"].lower()):
				bidenwa.add(tw["user"]["id"])
		if(", HI" in tw["user"]["location"] or "hawaii" in tw["user"]["location"].lower() or "honolulu" in tw["user"]["location"].lower()):
				bidenhi.add(tw["user"]["id"])
				if("honolulu" in tw["user"]["location"].lower() or "ewa gentry" in tw["user"]["location"].lower() or "mililani" in tw["user"]["location"].lower() or "pearl city" in tw["user"]["location"].lower() or "waipahu" in tw["user"]["location"].lower()):
					bidenhi1.add(tw["user"]["id"])
				if("Hilo" in tw["user"]["location"] or "kailua" in tw["user"]["location"].lower() or "kaneoha" in tw["user"]["location"].lower() or "kahului" in tw["user"]["location"].lower() or "Kihei" in tw["user"]["location"]):
					bidenhi2.add(tw["user"]["id"])
		if(", NJ" in tw["user"]["location"] or "new jersey" in tw["user"]["location"].lower()):
				bidennj.add(tw["user"]["id"])
		if(", NY" in tw["user"]["location"] or "new york" in tw["user"]["location"].lower()):
				bidenny.add(tw["user"]["id"])
		if(", RI" in tw["user"]["location"] or "rhode island" in tw["user"]["location"].lower()):
				bidenri.add(tw["user"]["id"])
		if(", MN" in tw["user"]["location"] or "minnesota" in tw["user"]["location"].lower()):
				bidenmn.add(tw["user"]["id"])
		if(", MI" in tw["user"]["location"] or "michigan" in tw["user"]["location"].lower()):
				bidenmi.add(tw["user"]["id"])
		if(", WI" in tw["user"]["location"] or "wisconsin" in tw["user"]["location"].lower()):
				bidenwi.add(tw["user"]["id"])
		if(", OR" in tw["user"]["location"] or "oregon" in tw["user"]["location"].lower()):
				bidenor.add(tw["user"]["id"])
		if(", MD" in tw["user"]["location"] or "maryland" in tw["user"]["location"].lower()):
				bidenmd.add(tw["user"]["id"])
		if(", MA" in tw["user"]["location"] or "massachusetts" in tw["user"]["location"].lower() or "boston" in tw["user"]["location"].lower()):
				bidenma.add(tw["user"]["id"])
		if(", ME" in tw["user"]["location"] or "maine" in tw["user"]["location"].lower()):
				bidenme.add(tw["user"]["id"])
				if("portland" in tw["user"]["location"].lower() or "augusta" in tw["user"]["location"].lower() or "brunswick" in tw["user"]["location"].lower() or "Saco" in tw["user"]["location"]):
					bidenme1.add(tw["user"]["id"])
				if("lewiston" in tw["user"]["location"].lower() or "bangor" in tw["user"]["location"].lower() or "auburn" in tw["user"]["location"].lower() or "presque isle" in tw["user"]["location"].lower()):
					bidenme2.add(tw["user"]["id"])
		if(", NC" in tw["user"]["location"] or "north carolina" in tw["user"]["location"].lower()):
				bidennc.add(tw["user"]["id"])
		if(", NH" in tw["user"]["location"] or "new hampshire" in tw["user"]["location"].lower()):
				bidennh.add(tw["user"]["id"])
		if(", NV" in tw["user"]["location"] or "nevada" in tw["user"]["location"].lower() or "las vegas" in tw["user"]["location"].lower()):
				bidennv.add(tw["user"]["id"])
				if("washoe county" in tw["user"]["location"].lower() or "Reno" in tw["user"]["location"]):
					bidenwashoenv.add(tw["user"]["id"])
				if("humboldt county" in tw["user"]["location"].lower() or "winnemucca" in tw["user"]["location"].lower()):
					bidenhumboldtnv.add(tw["user"]["id"])
				if("elko county" in tw["user"]["location"].lower() or "Elko" in tw["user"]["location"]):
					bidenelkonv.add(tw["user"]["id"])
				if("pershing county" in tw["user"]["location"].lower() or "lovelock" in tw["user"]["location"].lower()):
					bidenpershingnv.add(tw["user"]["id"])
				if("lander county" in tw["user"]["location"].lower() or "battle mountain" in tw["user"]["location"].lower()):
					bidenlandernv.add(tw["user"]["id"])
				if("eureka county" in tw["user"]["location"].lower() or "eureka" in tw["user"]["location"].lower()):
					bideneurekanv.add(tw["user"]["id"])
				if("churchill county" in tw["user"]["location"].lower() or "fallon" in tw["user"]["location"].lower()):
					bidenchurchillnv.add(tw["user"]["id"])
				if("white pine county" in tw["user"]["location"].lower() or "Ely" in tw["user"]["location"]):
					bidenwhitepinenv.add(tw["user"]["id"])
				if("storey county" in tw["user"]["location"].lower() or "virginia city" in tw["user"]["location"].lower()):
					bidenstoreynv.add(tw["user"]["id"])
				if("lyon county" in tw["user"]["location"].lower() or "fernley" in tw["user"]["location"].lower()):
					bidenlyonnv.add(tw["user"]["id"])
				if("carson city" in tw["user"]["location"].lower()):
					bidencarsoncitynv.add(tw["user"]["id"])
				if("douglas county" in tw["user"]["location"].lower() or "gardnerville ranchos" in tw["user"]["location"].lower()):
					bidendouglasnv.add(tw["user"]["id"])
				if("mineral county" in tw["user"]["location"].lower() or "hawthorne" in tw["user"]["location"].lower()):
					bidenmineralnv.add(tw["user"]["id"])
				if("nye county" in tw["user"]["location"].lower() or "pahrump" in tw["user"]["location"].lower()):
					bidennyenv.add(tw["user"]["id"])
				if("esmeralda county" in tw["user"]["location"].lower() or "goldfield" in tw["user"]["location"].lower()):
					bidenesmeraldanv.add(tw["user"]["id"])
				if("lincoln county" in tw["user"]["location"].lower() or "caliente" in tw["user"]["location"].lower()):
					bidenlincolnnv.add(tw["user"]["id"])
				if("clark county" in tw["user"]["location"].lower() or "las vegas" in tw["user"]["location"].lower()):
					bidenclarknv.add(tw["user"]["id"])
		if(", CO" in tw["user"]["location"] or "colorado" in tw["user"]["location"].lower()):
				bidenco.add(tw["user"]["id"])
		if(", NM" in tw["user"]["location"] or "new mexico" in tw["user"]["location"].lower()):
				bidennm.add(tw["user"]["id"])
		if(", AZ" in tw["user"]["location"] or "arizona" in tw["user"]["location"].lower()):
				bidenaz.add(tw["user"]["id"])
		if(", GA" in tw["user"]["location"] or "georgia" in tw["user"]["location"].lower()):
				bidenga.add(tw["user"]["id"])
		if(", TX" in tw["user"]["location"] or "texas" in tw["user"]["location"].lower()):
				bidentx.add(tw["user"]["id"])
		if(", IN" in tw["user"]["location"] or "indiana" in tw["user"]["location"].lower()):
				bidenin.add(tw["user"]["id"])
		if(", VA" in tw["user"]["location"] or "virginia" in tw["user"]["location"].lower()):
				bidenva.add(tw["user"]["id"])
		if(", IL" in tw["user"]["location"] or "illinois" in tw["user"]["location"].lower() or "chicago" in tw["user"]["location"].lower()):
				bidenil.add(tw["user"]["id"])
		if(", DE" in tw["user"]["location"] or "delaware" in tw["user"]["location"].lower()):
				bidende.add(tw["user"]["id"])
		if(", UT" in tw["user"]["location"] or "utah" in tw["user"]["location"].lower()):
				bidenut.add(tw["user"]["id"])
		if(", NE" in tw["user"]["location"] or "nebraska" in tw["user"]["location"].lower()):
				bidenne.add(tw["user"]["id"])
		if(", AK" in tw["user"]["location"] or "alaska" in tw["user"]["location"].lower()):
				bidenak.add(tw["user"]["id"])
		if(", WY" in tw["user"]["location"] or "wyoming" in tw["user"]["location"].lower()):
				bidenwy.add(tw["user"]["id"])
		if(", AL" in tw["user"]["location"] or "alabama" in tw["user"]["location"].lower()):
				bidenal.add(tw["user"]["id"])
		if(", TN" in tw["user"]["location"] or "tennessee" in tw["user"]["location"].lower()):
				bidentn.add(tw["user"]["id"])
		if(", ND" in tw["user"]["location"] or "north dakota" in tw["user"]["location"].lower()):
				bidennd.add(tw["user"]["id"])
		if(", SD" in tw["user"]["location"] or "south dakota" in tw["user"]["location"].lower()):
				bidensd.add(tw["user"]["id"])
		if(", WV" in tw["user"]["location"] or "west virginia" in tw["user"]["location"].lower()):
				bidenwv.add(tw["user"]["id"])
				if("morgantown" in tw["user"]["location"].lower() or "parkersburg" in tw["user"]["location"].lower() or "wheeling" in tw["user"]["location"].lower() or "weirton" in tw["user"]["location"].lower() or "fairmont" in tw["user"]["location"].lower()):
					bidenwv1.add(tw["user"]["id"])
				if("charleston" in tw["user"]["location"].lower() or "martinsburg" in tw["user"]["location"].lower() or "teays valley" in tw["user"]["location"].lower() or "south charleston" in tw["user"]["location"].lower() or "saint albans" in tw["user"]["location"].lower()):
					bidenwv2.add(tw["user"]["id"])
				if("huntington" in tw["user"]["location"].lower() or "beckley" in tw["user"]["location"].lower() or "bluefield" in tw["user"]["location"].lower() or "oak hill" in tw["user"]["location"].lower() or "pea ridge" in tw["user"]["location"].lower()):
					bidenwv3.add(tw["user"]["id"])
		if(", AR" in tw["user"]["location"] or "arkansas" in tw["user"]["location"].lower()):
				bidenar.add(tw["user"]["id"])
cursor = collection.find({"retweeted_status.full_text":{"$exists": "false"}})
for tw in cursor:
	if ("#trump2020" in tw["full_text"].lower() or "#teamtrump" in tw["full_text"].lower() or "#trumpforpresident" in tw["full_text"].lower() ):
		if(", MO" in tw["user"]["location"] or "missouri" in tw["user"]["location"].lower()):
				trumpmo.add(tw["user"]["id"])
		if(", IA" in tw["user"]["location"] or "iowa" in tw["user"]["location"].lower()):
				trumpia.add(tw["user"]["id"])
		if(", CA" in tw["user"]["location"] or "california" in tw["user"]["location"].lower() or "los angeles" in tw["user"]["location"].lower() or "san francisco" in tw["user"]["location"].lower()):
				trumpca.add(tw["user"]["id"])
		if(", CT" in tw["user"]["location"] or "connecticut" in tw["user"]["location"].lower()):
				trumpct.add(tw["user"]["id"])
		if(", PA" in tw["user"]["location"] or "pennsylvania" in tw["user"]["location"].lower()):
				trumppa.add(tw["user"]["id"])
		if(", OH" in tw["user"]["location"] or "ohio" in tw["user"]["location"].lower()):
				trumpoh.add(tw["user"]["id"])
		if(", FL" in tw["user"]["location"] or "florida" in tw["user"]["location"].lower() or "orlando" in tw["user"]["location"].lower() or "miami" in tw["user"]["location"].lower()):
				trumpfl.add(tw["user"]["id"])
		if(", WA" in tw["user"]["location"] or "washington" in tw["user"]["location"].lower()):
				trumpwa.add(tw["user"]["id"])
		if(", HI" in tw["user"]["location"] or "hawaii" in tw["user"]["location"].lower() or "honolulu" in tw["user"]["location"].lower()):
				trumphi.add(tw["user"]["id"])
				if("honolulu" in tw["user"]["location"].lower() or "ewa gentry" in tw["user"]["location"].lower() or "mililani" in tw["user"]["location"].lower() or "pearl city" in tw["user"]["location"].lower() or "waipahu" in tw["user"]["location"].lower()):
					trumphi1.add(tw["user"]["id"])
				if("Hilo" in tw["user"]["location"] or "kailua" in tw["user"]["location"].lower() or "kaneoha" in tw["user"]["location"].lower() or "kahului" in tw["user"]["location"].lower() or "Kihei" in tw["user"]["location"]):
					trumphi2.add(tw["user"]["id"])
		if(", NJ" in tw["user"]["location"] or "new jersey" in tw["user"]["location"].lower()):
				trumpnj.add(tw["user"]["id"])
		if(", NY" in tw["user"]["location"] or "new york" in tw["user"]["location"].lower()):
				trumpny.add(tw["user"]["id"])
		if(", RI" in tw["user"]["location"] or "rhode island" in tw["user"]["location"].lower()):
				trumpri.add(tw["user"]["id"])
		if(", MN" in tw["user"]["location"] or "minnesota" in tw["user"]["location"].lower()):
				trumpmn.add(tw["user"]["id"])
		if(", MI" in tw["user"]["location"] or "michigan" in tw["user"]["location"].lower()):
				trumpmi.add(tw["user"]["id"])
		if(", WI" in tw["user"]["location"] or "wisconsin" in tw["user"]["location"].lower()):
				trumpwi.add(tw["user"]["id"])
		if(", OR" in tw["user"]["location"] or "oregon" in tw["user"]["location"].lower()):
				trumpor.add(tw["user"]["id"])
		if(", MD" in tw["user"]["location"] or "maryland" in tw["user"]["location"].lower()):
				trumpmd.add(tw["user"]["id"])
		if(", MA" in tw["user"]["location"] or "massachusetts" in tw["user"]["location"].lower() or "boston" in tw["user"]["location"].lower()):
				trumpma.add(tw["user"]["id"])
		if(", ME" in tw["user"]["location"] or "maine" in tw["user"]["location"].lower()):
				trumpme.add(tw["user"]["id"])
				if("portland" in tw["user"]["location"].lower() or "augusta" in tw["user"]["location"].lower() or "brunswick" in tw["user"]["location"].lower() or "Saco" in tw["user"]["location"]):
					trumpme1.add(tw["user"]["id"])
				if("lewiston" in tw["user"]["location"].lower() or "bangor" in tw["user"]["location"].lower() or "auburn" in tw["user"]["location"].lower() or "presque isle" in tw["user"]["location"].lower()):
					trumpme2.add(tw["user"]["id"])
		if(", NC" in tw["user"]["location"] or "north carolina" in tw["user"]["location"].lower()):
				trumpnc.add(tw["user"]["id"])
		if(", NH" in tw["user"]["location"] or "new hampshire" in tw["user"]["location"].lower()):
				trumpnh.add(tw["user"]["id"])
		if(", NV" in tw["user"]["location"] or "nevada" in tw["user"]["location"].lower() or "las vegas" in tw["user"]["location"].lower()):
				trumpnv.add(tw["user"]["id"])
				if("washoe county" in tw["user"]["location"].lower() or "Reno" in tw["user"]["location"]):
					trumpwashoenv.add(tw["user"]["id"])
				if("humboldt county" in tw["user"]["location"].lower() or "winnemucca" in tw["user"]["location"].lower()):
					trumphumboldtnv.add(tw["user"]["id"])
				if("elko county" in tw["user"]["location"].lower() or "Elko" in tw["user"]["location"]):
					trumpelkonv.add(tw["user"]["id"])
				if("pershing county" in tw["user"]["location"].lower() or "lovelock" in tw["user"]["location"].lower()):
					trumppershingnv.add(tw["user"]["id"])
				if("lander county" in tw["user"]["location"].lower() or "battle mountain" in tw["user"]["location"].lower()):
					trumplandernv.add(tw["user"]["id"])
				if("eureka county" in tw["user"]["location"].lower() or "eureka" in tw["user"]["location"].lower()):
					trumpeurekanv.add(tw["user"]["id"])
				if("churchill county" in tw["user"]["location"].lower() or "fallon" in tw["user"]["location"].lower()):
					trumpchurchillnv.add(tw["user"]["id"])
				if("white pine county" in tw["user"]["location"].lower() or "Ely" in tw["user"]["location"]):
					trumpwhitepinenv.add(tw["user"]["id"])
				if("storey county" in tw["user"]["location"].lower() or "virginia city" in tw["user"]["location"].lower()):
					trumpstoreynv.add(tw["user"]["id"])
				if("lyon county" in tw["user"]["location"].lower() or "fernley" in tw["user"]["location"].lower()):
					trumplyonnv.add(tw["user"]["id"])
				if("carson city" in tw["user"]["location"].lower()):
					trumpcarsoncitynv.add(tw["user"]["id"])
				if("douglas county" in tw["user"]["location"].lower() or "gardnerville ranchos" in tw["user"]["location"].lower()):
					trumpdouglasnv.add(tw["user"]["id"])
				if("mineral county" in tw["user"]["location"].lower() or "hawthorne" in tw["user"]["location"].lower()):
					trumpmineralnv.add(tw["user"]["id"])
				if("nye county" in tw["user"]["location"].lower() or "pahrump" in tw["user"]["location"].lower()):
					trumpnyenv.add(tw["user"]["id"])
				if("esmeralda county" in tw["user"]["location"].lower() or "goldfield" in tw["user"]["location"].lower()):
					trumpesmeraldanv.add(tw["user"]["id"])
				if("lincoln county" in tw["user"]["location"].lower() or "caliente" in tw["user"]["location"].lower()):
					trumplincolnnv.add(tw["user"]["id"])
				if("clark county" in tw["user"]["location"].lower() or "las vegas" in tw["user"]["location"].lower()):
					trumpclarknv.add(tw["user"]["id"])
		if(", CO" in tw["user"]["location"] or "colorado" in tw["user"]["location"].lower()):
				trumpco.add(tw["user"]["id"])
		if(", NM" in tw["user"]["location"] or "new mexico" in tw["user"]["location"].lower()):
				trumpnm.add(tw["user"]["id"])
		if(", AZ" in tw["user"]["location"] or "arizona" in tw["user"]["location"].lower()):
				trumpaz.add(tw["user"]["id"])
		if(", GA" in tw["user"]["location"] or "georgia" in tw["user"]["location"].lower()):
				trumpga.add(tw["user"]["id"])
		if(", TX" in tw["user"]["location"] or "texas" in tw["user"]["location"].lower()):
				trumptx.add(tw["user"]["id"])
		if(", IN" in tw["user"]["location"] or "indiana" in tw["user"]["location"].lower()):
				trumpin.add(tw["user"]["id"])
		if(", VA" in tw["user"]["location"] or "virginia" in tw["user"]["location"].lower()):
				trumpva.add(tw["user"]["id"])
		if(", IL" in tw["user"]["location"] or "illinois" in tw["user"]["location"].lower() or "chicago" in tw["user"]["location"].lower()):
				trumpil.add(tw["user"]["id"])
		if(", DE" in tw["user"]["location"] or "delaware" in tw["user"]["location"].lower()):
				trumpde.add(tw["user"]["id"])
		if(", UT" in tw["user"]["location"] or "utah" in tw["user"]["location"].lower()):
				trumput.add(tw["user"]["id"])
		if(", NE" in tw["user"]["location"] or "nebraska" in tw["user"]["location"].lower()):
				trumpne.add(tw["user"]["id"])
		if(", AK" in tw["user"]["location"] or "alaska" in tw["user"]["location"].lower()):
				trumpak.add(tw["user"]["id"])
		if(", WY" in tw["user"]["location"] or "wyoming" in tw["user"]["location"].lower()):
				trumpwy.add(tw["user"]["id"])
		if(", AL" in tw["user"]["location"] or "alabama" in tw["user"]["location"].lower()):
				trumpal.add(tw["user"]["id"])
		if(", TN" in tw["user"]["location"] or "tennessee" in tw["user"]["location"].lower()):
				trumptn.add(tw["user"]["id"])
		if(", ND" in tw["user"]["location"] or "north dakota" in tw["user"]["location"].lower()):
				trumpnd.add(tw["user"]["id"])
		if(", SD" in tw["user"]["location"] or "south dakota" in tw["user"]["location"].lower()):
				trumpsd.add(tw["user"]["id"])
		if(", WV" in tw["user"]["location"] or "west virginia" in tw["user"]["location"].lower()):
				trumpwv.add(tw["user"]["id"])
				if("morgantown" in tw["user"]["location"].lower() or "parkersburg" in tw["user"]["location"].lower() or "wheeling" in tw["user"]["location"].lower() or "weirton" in tw["user"]["location"].lower() or "fairmont" in tw["user"]["location"].lower()):
					trumpwv1.add(tw["user"]["id"])
				if("charleston" in tw["user"]["location"].lower() or "martinsburg" in tw["user"]["location"].lower() or "teays valley" in tw["user"]["location"].lower() or "south charleston" in tw["user"]["location"].lower() or "saint albans" in tw["user"]["location"].lower()):
					trumpwv2.add(tw["user"]["id"])
				if("huntington" in tw["user"]["location"].lower() or "beckley" in tw["user"]["location"].lower() or "bluefield" in tw["user"]["location"].lower() or "oak hill" in tw["user"]["location"].lower() or "pea ridge" in tw["user"]["location"].lower()):
					trumpwv3.add(tw["user"]["id"])
		if(", AR" in tw["user"]["location"] or "arkansas" in tw["user"]["location"].lower()):
				trumpar.add(tw["user"]["id"])
	if ("#biden2020" in tw["full_text"].lower() or "#teamjoe" in tw["full_text"].lower() or "#bidenforpresident" in tw["full_text"].lower() ):
		if(", MO" in tw["user"]["location"] or "missouri" in tw["user"]["location"].lower()):
				bidenmo.add(tw["user"]["id"])
		if(", IA" in tw["user"]["location"] or "iowa" in tw["user"]["location"].lower()):
				bidenia.add(tw["user"]["id"])
		if(", CA" in tw["user"]["location"] or "california" in tw["user"]["location"].lower() or "los angeles" in tw["user"]["location"].lower() or "san francisco" in tw["user"]["location"].lower()):
				bidenca.add(tw["user"]["id"])
		if(", CT" in tw["user"]["location"] or "connecticut" in tw["user"]["location"].lower()):
				bidenct.add(tw["user"]["id"])
		if(", PA" in tw["user"]["location"] or "pennsylvania" in tw["user"]["location"].lower()):
				bidenpa.add(tw["user"]["id"])
		if(", OH" in tw["user"]["location"] or "ohio" in tw["user"]["location"].lower()):
				bidenoh.add(tw["user"]["id"])
		if(", FL" in tw["user"]["location"] or "florida" in tw["user"]["location"].lower() or "orlando" in tw["user"]["location"].lower() or "miami" in tw["user"]["location"].lower()):
				bidenfl.add(tw["user"]["id"])
		if(", WA" in tw["user"]["location"] or "washington" in tw["user"]["location"].lower()):
				bidenwa.add(tw["user"]["id"])
		if(", HI" in tw["user"]["location"] or "hawaii" in tw["user"]["location"].lower() or "honolulu" in tw["user"]["location"].lower()):
				bidenhi.add(tw["user"]["id"])
				if("honolulu" in tw["user"]["location"].lower() or "ewa gentry" in tw["user"]["location"].lower() or "mililani" in tw["user"]["location"].lower() or "pearl city" in tw["user"]["location"].lower() or "waipahu" in tw["user"]["location"].lower()):
					bidenhi1.add(tw["user"]["id"])
				if("Hilo" in tw["user"]["location"] or "kailua" in tw["user"]["location"].lower() or "kaneoha" in tw["user"]["location"].lower() or "kahului" in tw["user"]["location"].lower() or "Kihei" in tw["user"]["location"]):
					bidenhi2.add(tw["user"]["id"])
		if(", NJ" in tw["user"]["location"] or "new jersey" in tw["user"]["location"].lower()):
				bidennj.add(tw["user"]["id"])
		if(", NY" in tw["user"]["location"] or "new york" in tw["user"]["location"].lower()):
				bidenny.add(tw["user"]["id"])
		if(", RI" in tw["user"]["location"] or "rhode island" in tw["user"]["location"].lower()):
				bidenri.add(tw["user"]["id"])
		if(", MN" in tw["user"]["location"] or "minnesota" in tw["user"]["location"].lower()):
				bidenmn.add(tw["user"]["id"])
		if(", MI" in tw["user"]["location"] or "michigan" in tw["user"]["location"].lower()):
				bidenmi.add(tw["user"]["id"])
		if(", WI" in tw["user"]["location"] or "wisconsin" in tw["user"]["location"].lower()):
				bidenwi.add(tw["user"]["id"])
		if(", OR" in tw["user"]["location"] or "oregon" in tw["user"]["location"].lower()):
				bidenor.add(tw["user"]["id"])
		if(", MD" in tw["user"]["location"] or "maryland" in tw["user"]["location"].lower()):
				bidenmd.add(tw["user"]["id"])
		if(", MA" in tw["user"]["location"] or "massachusetts" in tw["user"]["location"].lower() or "boston" in tw["user"]["location"].lower()):
				bidenma.add(tw["user"]["id"])
		if(", ME" in tw["user"]["location"] or "maine" in tw["user"]["location"].lower()):
				bidenme.add(tw["user"]["id"])
				if("portland" in tw["user"]["location"].lower() or "augusta" in tw["user"]["location"].lower() or "brunswick" in tw["user"]["location"].lower() or "Saco" in tw["user"]["location"]):
					bidenme1.add(tw["user"]["id"])
				if("lewiston" in tw["user"]["location"].lower() or "bangor" in tw["user"]["location"].lower() or "auburn" in tw["user"]["location"].lower() or "presque isle" in tw["user"]["location"].lower()):
					bidenme2.add(tw["user"]["id"])
		if(", NC" in tw["user"]["location"] or "north carolina" in tw["user"]["location"].lower()):
				bidennc.add(tw["user"]["id"])
		if(", NH" in tw["user"]["location"] or "new hampshire" in tw["user"]["location"].lower()):
				bidennh.add(tw["user"]["id"])
		if(", NV" in tw["user"]["location"] or "nevada" in tw["user"]["location"].lower() or "las vegas" in tw["user"]["location"].lower()):
				bidennv.add(tw["user"]["id"])
				if("washoe county" in tw["user"]["location"].lower() or "Reno" in tw["user"]["location"]):
					bidenwashoenv.add(tw["user"]["id"])
				if("humboldt county" in tw["user"]["location"].lower() or "winnemucca" in tw["user"]["location"].lower()):
					bidenhumboldtnv.add(tw["user"]["id"])
				if("elko county" in tw["user"]["location"].lower() or "Elko" in tw["user"]["location"]):
					bidenelkonv.add(tw["user"]["id"])
				if("pershing county" in tw["user"]["location"].lower() or "lovelock" in tw["user"]["location"].lower()):
					bidenpershingnv.add(tw["user"]["id"])
				if("lander county" in tw["user"]["location"].lower() or "battle mountain" in tw["user"]["location"].lower()):
					bidenlandernv.add(tw["user"]["id"])
				if("eureka county" in tw["user"]["location"].lower() or "eureka" in tw["user"]["location"].lower()):
					bideneurekanv.add(tw["user"]["id"])
				if("churchill county" in tw["user"]["location"].lower() or "fallon" in tw["user"]["location"].lower()):
					bidenchurchillnv.add(tw["user"]["id"])
				if("white pine county" in tw["user"]["location"].lower() or "Ely" in tw["user"]["location"]):
					bidenwhitepinenv.add(tw["user"]["id"])
				if("storey county" in tw["user"]["location"].lower() or "virginia city" in tw["user"]["location"].lower()):
					bidenstoreynv.add(tw["user"]["id"])
				if("lyon county" in tw["user"]["location"].lower() or "fernley" in tw["user"]["location"].lower()):
					bidenlyonnv.add(tw["user"]["id"])
				if("carson city" in tw["user"]["location"].lower()):
					bidencarsoncitynv.add(tw["user"]["id"])
				if("douglas county" in tw["user"]["location"].lower() or "gardnerville ranchos" in tw["user"]["location"].lower()):
					bidendouglasnv.add(tw["user"]["id"])
				if("mineral county" in tw["user"]["location"].lower() or "hawthorne" in tw["user"]["location"].lower()):
					bidenmineralnv.add(tw["user"]["id"])
				if("nye county" in tw["user"]["location"].lower() or "pahrump" in tw["user"]["location"].lower()):
					bidennyenv.add(tw["user"]["id"])
				if("esmeralda county" in tw["user"]["location"].lower() or "goldfield" in tw["user"]["location"].lower()):
					bidenesmeraldanv.add(tw["user"]["id"])
				if("lincoln county" in tw["user"]["location"].lower() or "caliente" in tw["user"]["location"].lower()):
					bidenlincolnnv.add(tw["user"]["id"])
				if("clark county" in tw["user"]["location"].lower() or "las vegas" in tw["user"]["location"].lower()):
					bidenclarknv.add(tw["user"]["id"])
		if(", CO" in tw["user"]["location"] or "colorado" in tw["user"]["location"].lower()):
				bidenco.add(tw["user"]["id"])
		if(", NM" in tw["user"]["location"] or "new mexico" in tw["user"]["location"].lower()):
				bidennm.add(tw["user"]["id"])
		if(", AZ" in tw["user"]["location"] or "arizona" in tw["user"]["location"].lower()):
				bidenaz.add(tw["user"]["id"])
		if(", GA" in tw["user"]["location"] or "georgia" in tw["user"]["location"].lower()):
				bidenga.add(tw["user"]["id"])
		if(", TX" in tw["user"]["location"] or "texas" in tw["user"]["location"].lower()):
				bidentx.add(tw["user"]["id"])
		if(", IN" in tw["user"]["location"] or "indiana" in tw["user"]["location"].lower()):
				bidenin.add(tw["user"]["id"])
		if(", VA" in tw["user"]["location"] or "virginia" in tw["user"]["location"].lower()):
				bidenva.add(tw["user"]["id"])
		if(", IL" in tw["user"]["location"] or "illinois" in tw["user"]["location"].lower() or "chicago" in tw["user"]["location"].lower()):
				bidenil.add(tw["user"]["id"])
		if(", DE" in tw["user"]["location"] or "delaware" in tw["user"]["location"].lower()):
				bidende.add(tw["user"]["id"])
		if(", UT" in tw["user"]["location"] or "utah" in tw["user"]["location"].lower()):
				bidenut.add(tw["user"]["id"])
		if(", NE" in tw["user"]["location"] or "nebraska" in tw["user"]["location"].lower()):
				bidenne.add(tw["user"]["id"])
		if(", AK" in tw["user"]["location"] or "alaska" in tw["user"]["location"].lower()):
				bidenak.add(tw["user"]["id"])
		if(", WY" in tw["user"]["location"] or "wyoming" in tw["user"]["location"].lower()):
				bidenwy.add(tw["user"]["id"])
		if(", AL" in tw["user"]["location"] or "alabama" in tw["user"]["location"].lower()):
				bidenal.add(tw["user"]["id"])
		if(", TN" in tw["user"]["location"] or "tennessee" in tw["user"]["location"].lower()):
				bidentn.add(tw["user"]["id"])
		if(", ND" in tw["user"]["location"] or "north dakota" in tw["user"]["location"].lower()):
				bidennd.add(tw["user"]["id"])
		if(", SD" in tw["user"]["location"] or "south dakota" in tw["user"]["location"].lower()):
				bidensd.add(tw["user"]["id"])
		if(", WV" in tw["user"]["location"] or "west virginia" in tw["user"]["location"].lower()):
				bidenwv.add(tw["user"]["id"])
				if("morgantown" in tw["user"]["location"].lower() or "parkersburg" in tw["user"]["location"].lower() or "wheeling" in tw["user"]["location"].lower() or "weirton" in tw["user"]["location"].lower() or "fairmont" in tw["user"]["location"].lower()):
					bidenwv1.add(tw["user"]["id"])
				if("charleston" in tw["user"]["location"].lower() or "martinsburg" in tw["user"]["location"].lower() or "teays valley" in tw["user"]["location"].lower() or "south charleston" in tw["user"]["location"].lower() or "saint albans" in tw["user"]["location"].lower()):
					bidenwv2.add(tw["user"]["id"])
				if("huntington" in tw["user"]["location"].lower() or "beckley" in tw["user"]["location"].lower() or "bluefield" in tw["user"]["location"].lower() or "oak hill" in tw["user"]["location"].lower() or "pea ridge" in tw["user"]["location"].lower()):
					bidenwv3.add(tw["user"]["id"])
		if(", AR" in tw["user"]["location"] or "arkansas" in tw["user"]["location"].lower()):
				bidenar.add(tw["user"]["id"])
print("Missouri")
print("Trump: ", (len(trumpmo)/(len(trumpmo)+len(bidenmo))))
print("Biden: ",(len(bidenmo)/(len(trumpmo)+len(bidenmo))))
print("Colorado")
print("Trump: ", (len(trumpco)/(len(trumpco)+len(bidenco))))
print("Biden: ",(len(bidenco)/(len(trumpco)+len(bidenco))))
print("Minnesota")
print("Trump: ", (len(trumpmn)/(len(trumpmn)+len(bidenmn))))
print("Biden: ",(len(bidenmn)/(len(trumpmn)+len(bidenmn))))
print("Indiana")
print("Trump: ", (len(trumpin)/(len(trumpin)+len(bidenin))))
print("Biden: ",(len(bidenin)/(len(trumpin)+len(bidenin))))
print("")
print("Maine")
print("Trump: ", (len(trumpme)/(len(trumpme)+len(bidenme))))
print("Biden: ",(len(bidenme)/(len(trumpme)+len(bidenme))))
print("Maine 1")
print("Trump: ", (len(trumpme1)/(len(trumpme1)+len(bidenme1))))
print("votes ", len(trumpme1))
print("Biden: ",(len(bidenme1)/(len(trumpme1)+len(bidenme1))))
print("votes ", len(bidenme1))
print("Maine 2")
print("Trump: ", (len(trumpme2)/(len(trumpme2)+len(bidenme2))))
print("votes ", len(trumpme2))
print("Biden: ",(len(bidenme2)/(len(trumpme2)+len(bidenme2))))
print("votes ", len(bidenme2))
print("")
print("Delaware")
print("Trump: ", (len(trumpde)/(len(trumpde)+len(bidende))))
print("Biden: ",(len(bidende)/(len(trumpde)+len(bidende))))
print("Maryland")
print("Trump: ", (len(trumpmd)/(len(trumpmd)+len(bidenmd))))
print("Biden: ",(len(bidenmd)/(len(trumpmd)+len(bidenmd))))
print("South Dakota")
print("Trump: ", (len(trumpsd)/(len(trumpsd)+len(bidensd))))
print("Biden: ",(len(bidensd)/(len(trumpsd)+len(bidensd))))
print("Massachusetts")
print("Trump: ", (len(trumpma)/(len(trumpma)+len(bidenma))))
print("Biden: ",(len(bidenma)/(len(trumpma)+len(bidenma))))
print("Michigan")
print("Trump: ", (len(trumpmi)/(len(trumpmi)+len(bidenmi))))
print("Biden: ",(len(bidenmi)/(len(trumpmi)+len(bidenmi))))
print("California")
print("Trump: ", (len(trumpca)/(len(trumpca)+len(bidenca))))
print("Biden: ",(len(bidenca)/(len(trumpca)+len(bidenca))))
print("Virginia")
print("Trump: ", (len(trumpva)/(len(trumpva)+len(bidenva))))
print("Biden: ",(len(bidenva)/(len(trumpva)+len(bidenva))))
print("Georgia")
print("Trump: ", (len(trumpga)/(len(trumpga)+len(bidenga))))
print("Biden: ",(len(bidenga)/(len(trumpga)+len(bidenga))))
print("Florida")
print("Trump: ", (len(trumpfl)/(len(trumpfl)+len(bidenfl))))
print("Biden: ",(len(bidenfl)/(len(trumpfl)+len(bidenfl))))
print("Pennsylvania")
print("Trump: ", (len(trumppa)/(len(trumppa)+len(bidenpa))))
print("Biden: ",(len(bidenpa)/(len(trumppa)+len(bidenpa))))
print("Arizona")
print("Trump: ", (len(trumpaz)/(len(trumpaz)+len(bidenaz))))
print("Biden: ",(len(bidenaz)/(len(trumpaz)+len(bidenaz))))
print("Arkansas")
print("Trump: ", (len(trumpar)/(len(trumpar)+len(bidenar))))
print("Biden: ",(len(bidenar)/(len(trumpar)+len(bidenar))))
print("Alaska")
print("Trump: ", (len(trumpak)/(len(trumpak)+len(bidenak))))
print("Biden: ",(len(bidenak)/(len(trumpak)+len(bidenak))))
print("Alabama")
print("Trump: ", (len(trumpal)/(len(trumpal)+len(bidenal))))
print("Biden: ",(len(bidenal)/(len(trumpal)+len(bidenal))))
print("Washington")
print("Trump: ", (len(trumpwa)/(len(trumpwa)+len(bidenwa))))
print("Biden: ",(len(bidenwa)/(len(trumpwa)+len(bidenwa))))
print("")
print("West Virginia")
print("Trump: ", (len(trumpwv)/(len(trumpwv)+len(bidenwv))))
print("Biden: ",(len(bidenwv)/(len(trumpwv)+len(bidenwv))))
print("West Virginia 1")
print("Trump: ", (len(trumpwv1)/(len(trumpwv1)+len(bidenwv1))))
print("votes ", len(trumpwv1))
print("Biden: ",(len(bidenwv1)/(len(trumpwv1)+len(bidenwv1))))
print("votes ", len(bidenwv1))
print("West Virginia 2")
print("Trump: ", (len(trumpwv2)/(len(trumpwv2)+len(bidenwv2))))
print("votes ", len(trumpwv2))
print("Biden: ",(len(bidenwv2)/(len(trumpwv2)+len(bidenwv2))))
print("votes ", len(bidenwv2))
print("West Virginia 3")
print("Trump: ", (len(trumpwv3)/(len(trumpwv3)+len(bidenwv3))))
print("votes ", len(trumpwv3))
print("Biden: ",(len(bidenwv3)/(len(trumpwv3)+len(bidenwv3))))
print("votes ", len(bidenwv3))
print("")
print("New Jersey")
print("Trump: ", (len(trumpnj)/(len(trumpnj)+len(bidennj))))
print("Biden: ",(len(bidennj)/(len(trumpnj)+len(bidennj))))
print("New Mexico")
print("Trump: ", (len(trumpnm)/(len(trumpnm)+len(bidennm))))
print("Biden: ",(len(bidennm)/(len(trumpnm)+len(bidennm))))
print("Nebraska")
print("Trump: ", (len(trumpne)/(len(trumpne)+len(bidenne))))
print("Biden: ",(len(bidenne)/(len(trumpne)+len(bidenne))))
print("New Hampshire")
print("Trump: ", (len(trumpnh)/(len(trumpnh)+len(bidennh))))
print("Biden: ",(len(bidennh)/(len(trumpnh)+len(bidennh))))
print("")
print("Nevada")
print("Trump: ", (len(trumpnv)/(len(trumpnv)+len(bidennv))))
print("Biden: ",(len(bidennv)/(len(trumpnv)+len(bidennv))))
trumpvotesnevada = 0
bidenvotesnevada = 0
if(len(trumpwashoenv) > 0 or len(bidenwashoenv) > 0):
	trumpvoteswashoenv = ((len(trumpwashoenv)/(len(bidenwashoenv)+len(trumpwashoenv)))*191561)
	bidenvoteswashoenv = ((len(bidenwashoenv)/(len(bidenwashoenv)+len(trumpwashoenv)))*191561)
	trumpvotesnevada = trumpvotesnevada + trumpvoteswashoenv
	bidenvotesnevada = bidenvotesnevada + bidenvoteswashoenv
	print("washoe county")
	print("Trump: ", trumpvoteswashoenv)
	print("Biden: ", bidenvoteswashoenv)
if(len(trumphumboldtnv) > 0 or len(bidenhumboldtnv) > 0):
	trumpvoteshumboldtnv = ((len(trumphumboldtnv)/(len(bidenhumboldtnv)+len(trumphumboldtnv)))*5907)
	bidenvoteshumboldtnv = ((len(bidenhumboldtnv)/(len(bidenhumboldtnv)+len(trumphumboldtnv)))*5907)
	trumpvotesnevada = trumpvotesnevada + trumpvoteshumboldtnv
	bidenvotesnevada = bidenvotesnevada + bidenvoteshumboldtnv
	print("Humboldt county")
	print("Trump: ", trumpvoteshumboldtnv)
	print("Biden: ", bidenvoteshumboldtnv)
if(len(trumpelkonv) > 0 or len(bidenelkonv) > 0):
	trumpvoteselkonv = ((len(trumpelkonv)/(len(bidenelkonv)+len(trumpelkonv)))*16942)
	bidenvoteselkonv = ((len(bidenelkonv)/(len(bidenelkonv)+len(trumpelkonv)))*16942)
	trumpvotesnevada = trumpvotesnevada + trumpvoteselkonv
	bidenvotesnevada = bidenvotesnevada + bidenvoteselkonv
	print("Elko county")
	print("Trump: ", trumpvoteselkonv)
	print("Biden: ", bidenvoteselkonv)
if(len(trumppershingnv) > 0 or len(bidenpershingnv) > 0):
	trumpvotespershingnv = ((len(trumppershingnv)/(len(bidenpershingnv)+len(trumppershingnv)))*1833)
	bidenvotespershingnv = ((len(bidenpershingnv)/(len(bidenpershingnv)+len(trumppershingnv)))*1833)
	trumpvotesnevada = trumpvotesnevada + trumpvotespershingnv
	bidenvotesnevada = bidenvotesnevada + bidenvotespershingnv
	print("Pershing county")
	print("Trump: ", trumpvotespershingnv)
	print("Biden: ", bidenvotespershingnv)
if(len(trumplandernv) > 0 or len(bidenlandernv) > 0):
	trumpvoteslandernv = ((len(trumplandernv)/(len(bidenlandernv)+len(trumplandernv)))*2231)
	bidenvoteslandernv = ((len(bidenlandernv)/(len(bidenlandernv)+len(trumplandernv)))*2231)
	trumpvotesnevada = trumpvotesnevada + trumpvoteslandernv
	bidenvotesnevada = bidenvotesnevada + bidenvoteslandernv
	print("Lander county")
	print("Trump: ", trumpvoteslandernv)
	print("Biden: ", bidenvoteslandernv)
if(len(trumpeurekanv) > 0 or len(bideneurekanv) > 0):
	trumpvoteseurekanv = ((len(trumpeurekanv)/(len(bideneurekanv)+len(trumpeurekanv)))*797)
	bidenvoteseurekanv = ((len(bideneurekanv)/(len(bideneurekanv)+len(trumpeurekanv)))*797)
	trumpvotesnevada = trumpvotesnevada + trumpvoteseurekanv
	bidenvotesnevada = bidenvotesnevada + bidenvoteseurekanv
	print("Eureka county")
	print("Trump: ", trumpvoteseurekanv)
	print("Biden: ", bidenvoteseurekanv)
if(len(trumpchurchillnv) > 0 or len(bidenchurchillnv) > 0):
	trumpvoteschurchillnv = ((len(trumpchurchillnv)/(len(bidenchurchillnv)+len(trumpchurchillnv)))*10038)
	bidenvoteschurchillnv = ((len(bidenchurchillnv)/(len(bidenchurchillnv)+len(trumpchurchillnv)))*10038)
	trumpvotesnevada = trumpvotesnevada + trumpvoteschurchillnv
	bidenvotesnevada = bidenvotesnevada + bidenvoteschurchillnv
	print("Churchill county")
	print("Trump: ", trumpvoteschurchillnv)
	print("Biden: ", bidenvoteschurchillnv)
if(len(trumpwhitepinenv) > 0 or len(bidenwhitepinenv) > 0):
	trumpvoteswhitepinenv = ((len(trumpwhitepinenv)/(len(bidenwhitepinenv)+len(trumpwhitepinenv)))*3430)
	bidenvoteswhitepinenv = ((len(bidenwhitepinenv)/(len(bidenwhitepinenv)+len(trumpwhitepinenv)))*3430)
	trumpvotesnevada = trumpvotesnevada + trumpvoteswhitepinenv
	bidenvotesnevada = bidenvotesnevada + bidenvoteswhitepinenv
	print("White Pine county")
	print("Trump: ", trumpvoteswhitepinenv)
	print("Biden: ", bidenvoteswhitepinenv)
if(len(trumpstoreynv) > 0 or len(bidenstoreynv) > 0):
	trumpvotesstoreynv = ((len(trumpstoreynv)/(len(bidenstoreynv)+len(trumpstoreynv)))*2368)
	bidenvotesstoreynv = ((len(bidenstoreynv)/(len(bidenstoreynv)+len(trumpstoreynv)))*2368)
	trumpvotesnevada = trumpvotesnevada + trumpvotesstoreynv
	bidenvotesnevada = bidenvotesnevada + bidenvotesstoreynv
	print("Storey county")
	print("Trump: ", trumpvotesstoreynv)
	print("Biden: ", bidenvotesstoreynv)
if(len(trumplyonnv) > 0 or len(bidenlyonnv) > 0):
	trumpvoteslyonnv = ((len(trumplyonnv)/(len(bidenlyonnv)+len(trumplyonnv)))*22151)
	bidenvoteslyonnv = ((len(bidenlyonnv)/(len(bidenlyonnv)+len(trumplyonnv)))*22151)
	trumpvotesnevada = trumpvotesnevada + trumpvoteslyonnv
	bidenvotesnevada = bidenvotesnevada + bidenvoteslyonnv
	print("Lyon county")
	print("Trump: ", trumpvoteslyonnv)
	print("Biden: ", bidenvoteslyonnv)
if(len(trumpcarsoncitynv) > 0 or len(bidencarsoncitynv) > 0):
	trumpvotescarsoncitynv = ((len(trumpcarsoncitynv)/(len(bidencarsoncitynv)+len(trumpcarsoncitynv)))*22735)
	bidenvotescarsoncitynv = ((len(bidencarsoncitynv)/(len(bidencarsoncitynv)+len(trumpcarsoncitynv)))*22735)
	trumpvotesnevada = trumpvotesnevada + trumpvotescarsoncitynv
	bidenvotesnevada = bidenvotesnevada + bidenvotescarsoncitynv
	print("Carson City")
	print("Trump: ", trumpvotescarsoncitynv)
	print("Biden: ", bidenvotescarsoncitynv)
if(len(trumpdouglasnv) > 0 or len(bidendouglasnv) > 0):
	trumpvotesdouglasnv = ((len(trumpdouglasnv)/(len(bidendouglasnv)+len(trumpdouglasnv)))*25859)
	bidenvotesdouglasnv = ((len(bidendouglasnv)/(len(bidendouglasnv)+len(trumpdouglasnv)))*25859)
	trumpvotesnevada = trumpvotesnevada + trumpvotesdouglasnv
	bidenvotesnevada = bidenvotesnevada + bidenvotesdouglasnv
	print("Douglas county")
	print("Trump: ", trumpvotesdouglasnv)
	print("Biden: ", bidenvotesdouglasnv)
if(len(trumpmineralnv) > 0 or len(bidenmineralnv) > 0):
	trumpvotesmineralnv = ((len(trumpmineralnv)/(len(bidenmineralnv)+len(trumpmineralnv)))*1816)
	bidenvotesmineralnv = ((len(bidenmineralnv)/(len(bidenmineralnv)+len(trumpmineralnv)))*1816)
	trumpvotesnevada = trumpvotesnevada + trumpvotesmineralnv
	bidenvotesnevada = bidenvotesnevada + bidenvotesmineralnv
	print("Mineral county")
	print("Trump: ", trumpvotesmineralnv)
	print("Biden: ", bidenvotesmineralnv)
if(len(trumpnyenv) > 0 or len(bidennyenv) > 0):
	trumpvotesnyenv = ((len(trumpnyenv)/(len(bidennyenv)+len(trumpnyenv)))*18415)
	bidenvotesnyenv = ((len(bidennyenv)/(len(bidennyenv)+len(trumpnyenv)))*18415)
	trumpvotesnevada = trumpvotesnevada + trumpvotesnyenv
	bidenvotesnevada = bidenvotesnevada + bidenvotesnyenv
	print("Nye county")
	print("Trump: ", trumpvotesnyenv)
	print("Biden: ", bidenvotesnyenv)
if(len(trumpesmeraldanv) > 0 or len(bidenesmeraldanv) > 0):
	trumpvotesesmeraldanv = ((len(trumpesmeraldanv)/(len(bidenesmeraldanv)+len(trumpesmeraldanv)))*394)
	bidenvotesesmeraldanv = ((len(bidenesmeraldanv)/(len(bidenesmeraldanv)+len(trumpesmeraldanv)))*394)
	trumpvotesnevada = trumpvotesnevada + trumpvotesesmeraldanv
	bidenvotesnevada = bidenvotesnevada + bidenvotesesmeraldanv
	print("Esmeralda county")
	print("Trump: ", trumpvotesesmeraldanv)
	print("Biden: ", bidenvotesesmeraldanv)
if(len(trumplincolnnv) > 0 or len(bidenlincolnnv) > 0):
	trumpvoteslincolnnv = ((len(trumplincolnnv)/(len(bidenlincolnnv)+len(trumplincolnnv)))*1956)
	bidenvoteslincolnnv = ((len(bidenlincolnnv)/(len(bidenlincolnnv)+len(trumplincolnnv)))*1956)
	trumpvotesnevada = trumpvotesnevada + trumpvoteslincolnnv
	bidenvotesnevada = bidenvotesnevada + bidenvoteslincolnnv
	print("Lincoln county")
	print("Trump: ", trumpvoteslincolnnv)
	print("Biden: ", bidenvoteslincolnnv)
if(len(trumpclarknv) > 0 or len(bidenclarknv) > 0):
	trumpvotesclarknv = ((len(trumpclarknv)/(len(bidenclarknv)+len(trumpclarknv)))*720639)
	bidenvotesclarknv = ((len(bidenclarknv)/(len(bidenclarknv)+len(trumpclarknv)))*720639)
	trumpvotesnevada = trumpvotesnevada + trumpvotesclarknv
	bidenvotesnevada = bidenvotesnevada + bidenvotesclarknv
	print("Clark county")
	print("Trump: ", trumpvotesclarknv)
	print("Biden: ", bidenvotesclarknv)
print("TOTAL NEVADA")
print("Trump votes: ", trumpvotesnevada)
print("Biden votes: ", bidenvotesnevada)
print("Trump: ", (trumpvotesnevada/(trumpvotesnevada+bidenvotesnevada)))
print("Biden: ", (bidenvotesnevada/(trumpvotesnevada+bidenvotesnevada)))

print("")
print("North Carolina")
print("Trump: ", (len(trumpnc)/(len(trumpnc)+len(bidennc))))
print("Biden: ",(len(bidennc)/(len(trumpnc)+len(bidennc))))
print("New York")
print("Trump: ", (len(trumpny)/(len(trumpny)+len(bidenny))))
print("Biden: ",(len(bidenny)/(len(trumpny)+len(bidenny))))
print("North Dakota")
print("Trump: ", (len(trumpnd)/(len(trumpnd)+len(bidennd))))
print("Biden: ",(len(bidennd)/(len(trumpnd)+len(bidennd))))
print("Wyoming")
print("Trump: ", (len(trumpwy)/(len(trumpwy)+len(bidenwy))))
print("Biden: ",(len(bidenwy)/(len(trumpwy)+len(bidenwy))))
print("Ohio")
print("Trump: ", (len(trumpoh)/(len(trumpoh)+len(bidenoh))))
print("Biden: ",(len(bidenoh)/(len(trumpoh)+len(bidenoh))))
print("Oregon")
print("Trump: ", (len(trumpor)/(len(trumpor)+len(bidenor))))
print("Biden: ",(len(bidenor)/(len(trumpor)+len(bidenor))))
print("")
print("Hawaii")
print("Trump: ", (len(trumphi)/(len(trumphi)+len(bidenhi))))
print("Biden: ",(len(bidenhi)/(len(trumphi)+len(bidenhi))))
print("Hawaii 1")
print("Trump: ", (len(trumphi1)/(len(trumphi1)+len(bidenhi1))))
print("votes ", len(trumphi1))
print("Biden: ",(len(bidenhi1)/(len(trumphi1)+len(bidenhi1))))
print("votes ", len(bidenhi1))
print("Hawaii 2")
print("Trump: ", (len(trumphi2)/(len(trumphi2)+len(bidenhi2))))
print("votes ", len(trumphi2))
print("Biden: ",(len(bidenhi2)/(len(trumphi2)+len(bidenhi2))))
print("votes ", len(bidenhi2))
print("")
print("Texas")
print("Trump: ", (len(trumptx)/(len(trumptx)+len(bidentx))))
print("Biden: ",(len(bidentx)/(len(trumptx)+len(bidentx))))
print("Tennessee")
print("Trump: ", (len(trumptn)/(len(trumptn)+len(bidentn))))
print("Biden: ",(len(bidentn)/(len(trumptn)+len(bidentn))))
print("Wisconsin")
print("Trump: ", (len(trumpwi)/(len(trumpwi)+len(bidenwi))))
print("Biden: ",(len(bidenwi)/(len(trumpwi)+len(bidenwi))))
print("Rhode Island")
print("Trump: ", (len(trumpri)/(len(trumpri)+len(bidenri))))
print("Biden: ",(len(bidenri)/(len(trumpri)+len(bidenri))))
print("Connecticut")
print("Trump: ", (len(trumpct)/(len(trumpct)+len(bidenct))))
print("Biden: ",(len(bidenct)/(len(trumpct)+len(bidenct))))
print("Utah")
print("Trump: ", (len(trumput)/(len(trumput)+len(bidenut))))
print("Biden: ",(len(bidenut)/(len(trumput)+len(bidenut))))
print("Iowa")
print("Trump: ", (len(trumpia)/(len(trumpia)+len(bidenia))))
print("Biden: ",(len(bidenia)/(len(trumpia)+len(bidenia))))
print("Illinois")
print("Trump: ", (len(trumpil)/(len(trumpil)+len(bidenil))))
print("Biden: ",(len(bidenil)/(len(trumpil)+len(bidenil))))