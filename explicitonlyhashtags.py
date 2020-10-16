from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient(port=27017)
db=client.TWITTERUSA
trumpmaryland = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'full_text': { "$regex": '#trumpforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#trumpforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Maryland', "$options" :'i' }},{'user.location': { "$regex": ', MD'}},{'user.location':{ "$regex": 'Gaithersburg', "$options" :'i' }},{'user.location':{ "$regex": 'Annapolis', "$options" :'i' }}]}]}).distinct("user.id")
trumpmdcount = 0
for user in trumpmaryland:
	trumpmdcount = trumpmdcount + 1
bidenmaryland = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'full_text': { "$regex": '#bidenforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#bidenforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Maryland', "$options" :'i' }},{'user.location': { "$regex": ', MD'}},{'user.location':{ "$regex": 'Gaithersburg', "$options" :'i' }},{'user.location':{ "$regex": 'Annapolis', "$options" :'i' }}]}]}).distinct("user.id")
bidenmdcount = 0
for user in bidenmaryland:
	bidenmdcount = bidenmdcount + 1
print("Maryland:")
print("Trump: ", (trumpmdcount/(trumpmdcount+bidenmdcount)))
print("Biden: ",(bidenmdcount/(trumpmdcount+bidenmdcount)))

trumpcalifornia = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'full_text': { "$regex": '#trumpforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#trumpforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'California', "$options" :'i' }},{'user.location': { "$regex": ', CA'}},{'user.location':{ "$regex": 'Los Angeles', "$options" :'i' }},{'user.location':{ "$regex": 'San Diego', "$options" :'i' }},{'user.location':{ "$regex": 'San Jose', "$options" :'i' }},{'user.location':{ "$regex": 'San Francisco', "$options" :'i' }},{'user.location':{ "$regex": 'Fresno', "$options" :'i' }},{'user.location':{ "$regex": 'Sacramento', "$options" :'i' }},{'user.location':{ "$regex": 'Oakland', "$options" :'i' }},{'user.location':{ "$regex": 'Bakersfield', "$options" :'i' }},{'user.location':{ "$regex": 'Anaheim', "$options" :'i' }},{'user.location':{ "$regex": 'Santa Ana', "$options" :'i' }},{'user.location':{ "$regex": 'Riverside', "$options" :'i' }},{'user.location':{ "$regex": 'Stockton', "$options" :'i' }},{'user.location':{ "$regex": 'Irvine', "$options" :'i' }},{'user.location':{ "$regex": 'Chula Vista', "$options" :'i' }},{'user.location':{ "$regex": 'Fremont', "$options" :'i' }},{'user.location':{ "$regex": 'San Bernardino', "$options" :'i' }},{'user.location':{ "$regex": 'Modesto', "$options" :'i' }},{'user.location':{ "$regex": 'Fontana', "$options" :'i' }},{'user.location':{ "$regex": 'Santa Clarita', "$options" :'i' }},{'user.location':{ "$regex": 'Oxnard', "$options" :'i' }},{'user.location':{ "$regex": 'Moreno Valley', "$options" :'i' }},{'user.location':{ "$regex": 'Huntington Beach', "$options" :'i' }},{'user.location':{ "$regex": 'Rancho Cucamonga', "$options" :'i' }}]}]}).distinct("user.id")
trumpcacount = 0
for user in trumpcalifornia:
	trumpcacount = trumpcacount + 1
bidencalifornia = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'full_text': { "$regex": '#bidenforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#bidenforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'California', "$options" :'i' }},{'user.location': { "$regex": ', CA'}},{'user.location':{ "$regex": 'Los Angeles', "$options" :'i' }},{'user.location':{ "$regex": 'San Diego', "$options" :'i' }},{'user.location':{ "$regex": 'San Jose', "$options" :'i' }},{'user.location':{ "$regex": 'San Francisco', "$options" :'i' }},{'user.location':{ "$regex": 'Fresno', "$options" :'i' }},{'user.location':{ "$regex": 'Sacramento', "$options" :'i' }},{'user.location':{ "$regex": 'Oakland', "$options" :'i' }},{'user.location':{ "$regex": 'Bakersfield', "$options" :'i' }},{'user.location':{ "$regex": 'Anaheim', "$options" :'i' }},{'user.location':{ "$regex": 'Santa Ana', "$options" :'i' }},{'user.location':{ "$regex": 'Riverside', "$options" :'i' }},{'user.location':{ "$regex": 'Stockton', "$options" :'i' }},{'user.location':{ "$regex": 'Irvine', "$options" :'i' }},{'user.location':{ "$regex": 'Chula Vista', "$options" :'i' }},{'user.location':{ "$regex": 'Fremont', "$options" :'i' }},{'user.location':{ "$regex": 'San Bernardino', "$options" :'i' }},{'user.location':{ "$regex": 'Modesto', "$options" :'i' }},{'user.location':{ "$regex": 'Fontana', "$options" :'i' }},{'user.location':{ "$regex": 'Santa Clarita', "$options" :'i' }},{'user.location':{ "$regex": 'Oxnard', "$options" :'i' }},{'user.location':{ "$regex": 'Moreno Valley', "$options" :'i' }},{'user.location':{ "$regex": 'Huntington Beach', "$options" :'i' }},{'user.location':{ "$regex": 'Rancho Cucamonga', "$options" :'i' }}]}]}).distinct("user.id")
bidencacount = 0
for user in bidencalifornia:
	bidencacount = bidencacount + 1
print("California:")
print("Trump: ", (trumpcacount/(trumpcacount+bidencacount)))
print("Biden: ",(bidencacount/(trumpcacount+bidencacount)))


trumpcolorado = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'full_text': { "$regex": '#trumpforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#trumpforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Colorado', "$options" :'i' }},{'user.location': { "$regex": ', CO'}},{'user.location':{ "$regex": 'Fort Collins', "$options" :'i' }}]}]}).distinct("user.id")
trumpcocount = 0
for user in trumpcolorado:
	trumpcocount = trumpcocount + 1
bidencolorado = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'full_text': { "$regex": '#bidenforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#bidenforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Colorado', "$options" :'i' }},{'user.location': { "$regex": ', CO'}},{'user.location':{ "$regex": 'Fort Collins', "$options" :'i' }}]}]}).distinct("user.id")
bidencocount = 0
for user in bidencolorado:
	bidencocount = bidencocount + 1
print("Colorado:")
print("Trump: ", (trumpcocount/(trumpcocount+bidencocount)))
print("Biden: ",(bidencocount/(trumpcocount+bidencocount)))

trumporegon = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'full_text': { "$regex": '#trumpforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#trumpforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Oregon', "$options" :'i' }},{'user.location': { "$regex": ', OR'}}]}]}).distinct("user.id")
trumporcount = 0
for user in trumporegon:
	trumporcount = trumporcount + 1
bidenoregon = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'full_text': { "$regex": '#bidenforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#bidenforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Oregon', "$options" :'i' }},{'user.location': { "$regex": ', OR'}}]}]}).distinct("user.id")
bidenorcount = 0
for user in bidenoregon:
	bidenorcount = bidenorcount + 1
print("Oregon:")
print("Trump: ", (trumporcount/(trumporcount+bidenorcount)))
print("Biden: ",(bidenorcount/(trumporcount+bidenorcount)))

trumpnewyork = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'full_text': { "$regex": '#trumpforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#trumpforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'New York', "$options" :'i' }},{'user.location': { "$regex": ', NY'}},{'user.location':{ "$regex": 'Buffalo', "$options" :'i' }}]}]}).distinct("user.id")
trumpnycount = 0
for user in trumpnewyork:
	trumpnycount = trumpnycount + 1
bidennewyork = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'full_text': { "$regex": '#bidenforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#bidenforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'New York', "$options" :'i' }},{'user.location': { "$regex": ', NY'}},{'user.location':{ "$regex": 'Buffalo', "$options" :'i' }}]}]}).distinct("user.id")
bidennycount = 0
for user in bidennewyork:
	bidennycount = bidennycount + 1
print("New York:")
print("Trump: ", (trumpnycount/(trumpnycount+bidennycount)))
print("Biden: ",(bidennycount/(trumpnycount+bidennycount)))

trumpnewjersey = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'full_text': { "$regex": '#trumpforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#trumpforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'New Jersey', "$options" :'i' }},{'user.location': { "$regex": ', NJ'}},{'user.location':{ "$regex": 'Trenton', "$options" :'i' }}]}]}).distinct("user.id")
trumpnjcount = 0
for user in trumpnewjersey:
	trumpnjcount = trumpnjcount + 1
bidennewjersey = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'full_text': { "$regex": '#bidenforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#bidenforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'New Jersey', "$options" :'i' }},{'user.location': { "$regex": ', NJ'}},{'user.location':{ "$regex": 'Trenton', "$options" :'i' }}]}]}).distinct("user.id")
bidennjcount = 0
for user in bidennewjersey:
	bidennjcount = bidennjcount + 1
print("New Jersey:")
print("Trump: ", (trumpnjcount/(trumpnjcount+bidennjcount)))
print("Biden: ",(bidennjcount/(trumpnjcount+bidennjcount)))

trumpnewhampshire = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'full_text': { "$regex": '#trumpforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#trumpforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'New Hampshire', "$options" :'i' }},{'user.location': { "$regex": ', NH'}}]}]}).distinct("user.id")
trumpnhcount = 0
for user in trumpnewhampshire:
	trumpnhcount = trumpnhcount + 1
bidennewyhampshire = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'full_text': { "$regex": '#bidenforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#bidenforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'New Hampshire', "$options" :'i' }},{'user.location': { "$regex": ', NH'}}]}]}).distinct("user.id")
bidennhcount = 0
for user in bidennewyhampshire:
	bidennhcount = bidennhcount + 1
print("New Hampshire:")
print("Trump: ", (trumpnhcount/(trumpnhcount+bidennhcount)))
print("Biden: ",(bidennhcount/(trumpnhcount+bidennhcount)))

trumpnevada = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'full_text': { "$regex": '#trumpforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#trumpforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Nevada', "$options" :'i' }},{'user.location': { "$regex": ', NV'}},{'user.location':{ "$regex": 'North Las Vegas', "$options" :'i' }},{'user.location':{ "$regex": 'Reno'}},{'user.location':{ "$regex": 'Sparks', "$options" :'i' }}]}]}).distinct("user.id")
trumpnvcount = 0
for user in trumpnevada:
	trumpnvcount = trumpnvcount + 1
bidennevada = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'full_text': { "$regex": '#bidenforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#bidenforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Nevada', "$options" :'i' }},{'user.location': { "$regex": ', NV'}},{'user.location':{ "$regex": 'North Las Vegas', "$options" :'i' }},{'user.location':{ "$regex": 'Reno'}},{'user.location':{ "$regex": 'Sparks', "$options" :'i' }}]}]}).distinct("user.id")
bidennvcount = 0
for user in bidennevada:
	bidennvcount = bidennvcount + 1
print("Nevada:")
print("Trump: ", (trumpnvcount/(trumpnvcount+bidennvcount)))
print("Biden: ",(bidennvcount/(trumpnvcount+bidennvcount)))

trumpmichigan = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'full_text': { "$regex": '#trumpforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#trumpforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Michigan', "$options" :'i' }},{'user.location': { "$regex": ', MI'}},{'user.location':{ "$regex": 'Sterling Heights', "$options" :'i' }},{'user.location':{ "$regex": 'Ann Arbor', "$options" :'i' }}]}]}).distinct("user.id")
trumpmicount = 0
for user in trumpmichigan:
	trumpmicount = trumpmicount + 1
bidenmichigan = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'full_text': { "$regex": '#bidenforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#bidenforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Michigan', "$options" :'i' }},{'user.location': { "$regex": ', MI'}},{'user.location':{ "$regex": 'Sterling Heights', "$options" :'i' }},{'user.location':{ "$regex": 'Ann Arbor', "$options" :'i' }}]}]}).distinct("user.id")
bidenmicount = 0
for user in bidenmichigan:
	bidenmicount = bidenmicount + 1
print("Michigan:")
print("Trump: ", (trumpmicount/(trumpmicount+bidenmicount)))
print("Biden: ",(bidenmicount/(trumpmicount+bidenmicount)))

trumpminnesota = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'full_text': { "$regex": '#trumpforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#trumpforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Minnesota', "$options" :'i' }},{'user.location': { "$regex": ', MN'}},{'user.location':{ "$regex": 'Saint Paul', "$options" :'i' }}]}]}).distinct("user.id")
trumpmncount = 0
for user in trumpminnesota:
	trumpmncount = trumpmncount + 1
bidenminnesota = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'full_text': { "$regex": '#bidenforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#bidenforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Minnesota', "$options" :'i' }},{'user.location': { "$regex": ', MN'}},{'user.location':{ "$regex": 'Saint Paul', "$options" :'i' }}]}]}).distinct("user.id")
bidenmncount = 0
for user in bidenminnesota:
	bidenmncount = bidenmncount + 1
print("Minnesota:")
print("Trump: ", (trumpmncount/(trumpmncount+bidenmncount)))
print("Biden: ",(bidenmncount/(trumpmncount+bidenmncount)))

trumpwashington = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'full_text': { "$regex": '#trumpforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#trumpforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Washington', "$options" :'i' }},{'user.location': { "$regex": ', WA'}},{'user.location':{ "$regex": 'Seattle', "$options" :'i' }},{'user.location':{ "$regex": 'Spokane', "$options" :'i' }},{'user.location':{ "$regex": 'Tacoma', "$options" :'i' }},{'user.location':{ "$regex": 'Vancouver', "$options" :'i' }}]}]}).distinct("user.id")
trumpwacount = 0
for user in trumpwashington:
	trumpwacount = trumpwacount + 1
bidenwashington = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'full_text': { "$regex": '#bidenforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#bidenforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Washington', "$options" :'i' }},{'user.location': { "$regex": ', WA'}},{'user.location':{ "$regex": 'Seattle', "$options" :'i' }},{'user.location':{ "$regex": 'Spokane', "$options" :'i' }},{'user.location':{ "$regex": 'Tacoma', "$options" :'i' }},{'user.location':{ "$regex": 'Vancouver', "$options" :'i' }}]}]}).distinct("user.id")
bidenwacount = 0
for user in bidenwashington:
	bidenwacount = bidenwacount + 1
print("Washington:")
print("Trump: ", (trumpwacount/(trumpwacount+bidenwacount)))
print("Biden: ",(bidenwacount/(trumpwacount+bidenwacount)))

trumpflorida = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'full_text': { "$regex": '#trumpforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#trumpforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Florida', "$options" :'i' }},{'user.location': { "$regex": ', FL'}},{'user.location':{ "$regex": 'Miami'}},{'user.location':{ "$regex": 'Tampa'}},{'user.location':{ "$regex": 'Orlando', "$options" :'i' }},{'user.location':{ "$regex": 'Hialeah', "$options" :'i' }},{'user.location':{ "$regex": 'Port St. Lucie', "$options" :'i' }},{'user.location':{ "$regex": 'Cape Coral', "$options" :'i' }},{'user.location':{ "$regex": 'Fort Lauderdale', "$options" :'i' }},{'user.location':{ "$regex": 'Pembroke Pines', "$options" :'i' }},{'user.location':{ "$regex": 'Hollywood', "$options" :'i' }},{'user.location':{ "$regex": 'Coral Springs', "$options" :'i' }},{'user.location':{ "$regex": 'Palm Bay', "$options" :'i' }},{'user.location':{ "$regex": 'Pompano Beach', "$options" :'i' }},{'user.location':{ "$regex": 'West Palm Beach', "$options" :'i' }},{'user.location':{ "$regex": 'Davie'}}]}]}).distinct("user.id")
trumpflcount = 0
for user in trumpflorida:
	trumpflcount = trumpflcount + 1
bidenflorida = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'full_text': { "$regex": '#bidenforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#bidenforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Florida', "$options" :'i' }},{'user.location': { "$regex": ', FL'}},{'user.location':{ "$regex": 'Miami'}},{'user.location':{ "$regex": 'Tampa'}},{'user.location':{ "$regex": 'Orlando', "$options" :'i' }},{'user.location':{ "$regex": 'Hialeah', "$options" :'i' }},{'user.location':{ "$regex": 'Port St. Lucie', "$options" :'i' }},{'user.location':{ "$regex": 'Cape Coral', "$options" :'i' }},{'user.location':{ "$regex": 'Fort Lauderdale', "$options" :'i' }},{'user.location':{ "$regex": 'Pembroke Pines', "$options" :'i' }},{'user.location':{ "$regex": 'Hollywood', "$options" :'i' }},{'user.location':{ "$regex": 'Coral Springs', "$options" :'i' }},{'user.location':{ "$regex": 'Palm Bay', "$options" :'i' }},{'user.location':{ "$regex": 'Pompano Beach', "$options" :'i' }},{'user.location':{ "$regex": 'West Palm Beach', "$options" :'i' }},{'user.location':{ "$regex": 'Davie'}}]}]}).distinct("user.id")
bidenflcount = 0
for user in bidenflorida:
	bidenflcount = bidenflcount + 1
print("Florida:")
print("Trump: ", (trumpflcount/(trumpflcount+bidenflcount)))
print("Biden: ",(bidenflcount/(trumpflcount+bidenflcount)))

trumppennsylvania = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'full_text': { "$regex": '#trumpforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#trumpforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Pennsylvania', "$options" :'i' }},{'user.location': { "$regex": ', PA'}},{'user.location':{ "$regex": 'Philadelphia', "$options" :'i' }}]}]}).distinct("user.id")
trumppacount = 0
for user in trumppennsylvania:
	trumppacount = trumppacount + 1
bidenpennsylvania = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'full_text': { "$regex": '#bidenforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#bidenforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Pennsylvania', "$options" :'i' }},{'user.location': { "$regex": ', PA'}},{'user.location':{ "$regex": 'Philadelphia', "$options" :'i' }}]}]}).distinct("user.id")
bidenpacount = 0
for user in bidenpennsylvania:
	bidenpacount = bidenpacount + 1
print("Pennsylvania:")
print("Trump: ", (trumppacount/(trumppacount+bidenpacount)))
print("Biden: ",(bidenpacount/(trumppacount+bidenpacount)))

trumpillinois = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'full_text': { "$regex": '#trumpforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#trumpforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Illinois', "$options" :'i' }},{'user.location': { "$regex": ', IL'}},{'user.location':{ "$regex": 'Chicago', "$options" :'i' }},{'user.location':{ "$regex": 'Naperville', "$options" :'i' }}]}]}).distinct("user.id")
trumpilcount = 0
for user in trumpillinois:
	trumpilcount = trumpilcount + 1
bidenillinois = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'full_text': { "$regex": '#bidenforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#bidenforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Illinois', "$options" :'i' }},{'user.location': { "$regex": ', IL'}},{'user.location':{ "$regex": 'Chicago', "$options" :'i' }},{'user.location':{ "$regex": 'Naperville', "$options" :'i' }}]}]}).distinct("user.id")
bidenilcount = 0
for user in bidenillinois:
	bidenilcount = bidenilcount + 1
print("Illinois:")
print("Trump: ", (trumpilcount/(trumpilcount+bidenilcount)))
print("Biden: ",(bidenilcount/(trumpilcount+bidenilcount)))

trumpwisconsin = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'full_text': { "$regex": '#trumpforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#trumpforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Wisconsin', "$options" :'i' }},{'user.location': { "$regex": ', WI'}},{'user.location':{ "$regex": 'Green Bay', "$options" :'i' }},{'user.location':{ "$regex": 'Kenosha', "$options" :'i' }}]}]}).distinct("user.id")
trumpwicount = 0
for user in trumpwisconsin:
	trumpwicount = trumpwicount + 1
bidenwisconsin = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'full_text': { "$regex": '#bidenforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#bidenforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Wisconsin', "$options" :'i' }},{'user.location': { "$regex": ', WI'}},{'user.location':{ "$regex": 'Green Bay', "$options" :'i' }},{'user.location':{ "$regex": 'Kenosha', "$options" :'i' }}]}]}).distinct("user.id")
bidenwicount = 0
for user in bidenwisconsin:
	bidenwicount = bidenwicount + 1
print("Wisconsin:")
print("Trump: ", (trumpwicount/(trumpwicount+bidenwicount)))
print("Biden: ",(bidenwicount/(trumpwicount+bidenwicount)))

trumpmassachusetts = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'full_text': { "$regex": '#trumpforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#trumpforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Massachusetts', "$options" :'i' }},{'user.location': { "$regex": ', MA'}},{'user.location':{ "$regex": 'Boston', "$options" :'i' }},{'user.location':{ "$regex": 'Lowell', "$options" :'i' }}]}]}).distinct("user.id")
trumpmacount = 0
for user in trumpmassachusetts:
	trumpmacount = trumpmacount + 1
bidenmassachusetts = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'full_text': { "$regex": '#bidenforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#bidenforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Massachusetts', "$options" :'i' }},{'user.location': { "$regex": ', MA'}},{'user.location':{ "$regex": 'Boston', "$options" :'i' }},{'user.location':{ "$regex": 'Lowell', "$options" :'i' }}]}]}).distinct("user.id")
bidenmacount = 0
for user in bidenmassachusetts:
	bidenmacount = bidenmacount + 1
print("Massachusetts:")
print("Trump: ", (trumpmacount/(trumpmacount+bidenmacount)))
print("Biden: ",(bidenmacount/(trumpmacount+bidenmacount)))

trumphawaii = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'full_text': { "$regex": '#trumpforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#trumpforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Hawaii', "$options" :'i' }},{'user.location': { "$regex": ', HI'}},{'user.location':{ "$regex": 'Honolulu', "$options" :'i' }},{'user.location':{ "$regex": 'Hilo'}},{'user.location':{ "$regex": 'Kailua', "$options" :'i' }}]}]}).distinct("user.id")
trumphicount = 0
for user in trumphawaii:
	trumphicount = trumphicount + 1
bidenhawaii = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'full_text': { "$regex": '#bidenforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#bidenforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Hawaii', "$options" :'i' }},{'user.location': { "$regex": ', HI'}},{'user.location':{ "$regex": 'Honolulu', "$options" :'i' }},{'user.location':{ "$regex": 'Hilo'}},{'user.location':{ "$regex": 'Kailua', "$options" :'i' }}]}]}).distinct("user.id")
bidenhicount = 0
for user in bidenhawaii:
	bidenhicount = bidenhicount + 1
print("Hawaii:")
print("Trump: ", (trumphicount/(trumphicount+bidenhicount)))
print("Biden: ",(bidenhicount/(trumphicount+bidenhicount)))

trumpvirginia = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'full_text': { "$regex": '#trumpforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#trumpforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Virginia', "$options" :'i' }},{'user.location': { "$regex": ', VA'}},{'user.location':{ "$regex": 'Chesapeake', "$options" :'i' }},{'user.location':{ "$regex": 'Newport News', "$options" :'i' }}]}]}).distinct("user.id")
trumpvacount = 0
for user in trumpvirginia:
	trumpvacount = trumpvacount + 1
bidenvirginia = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'full_text': { "$regex": '#bidenforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#bidenforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Virginia', "$options" :'i' }},{'user.location': { "$regex": ', VA'}},{'user.location':{ "$regex": 'Chesapeake', "$options" :'i' }},{'user.location':{ "$regex": 'Newport News', "$options" :'i' }}]}]}).distinct("user.id")
bidenvacount = 0
for user in bidenvirginia:
	bidenvacount = bidenvacount + 1
print("Virginia:")
print("Trump: ", (trumpvacount/(trumpvacount+bidenvacount)))
print("Biden: ",(bidenvacount/(trumpvacount+bidenvacount)))

trumpohio = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'full_text': { "$regex": '#trumpforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#trumpforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Ohio', "$options" :'i' }},{'user.location': { "$regex": ', OH'}},{'user.location':{ "$regex": 'Cincinnati', "$options" :'i' }},{'user.location':{ "$regex": 'Toledo', "$options" :'i' }}]}]}).distinct("user.id")
trumpohcount = 0
for user in trumpohio:
	trumpohcount = trumpohcount + 1
bidenohio = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'full_text': { "$regex": '#bidenforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#bidenforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Ohio', "$options" :'i' }},{'user.location': { "$regex": ', OH'}},{'user.location':{ "$regex": 'Cincinnati', "$options" :'i' }},{'user.location':{ "$regex": 'Toledo', "$options" :'i' }}]}]}).distinct("user.id")
bidenohcount = 0
for user in bidenohio:
	bidenohcount = bidenohcount + 1
print("Ohio:")
print("Trump: ", (trumpohcount/(trumpohcount+bidenohcount)))
print("Biden: ",(bidenohcount/(trumpohcount+bidenohcount)))

trumpdelaware = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'full_text': { "$regex": '#trumpforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#trumpforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Delaware', "$options" :'i' }},{'user.location': { "$regex": ', DE'}}]}]}).distinct("user.id")
trumpdecount = 0
for user in trumpdelaware:
	trumpdecount = trumpdecount + 1
bidendelaware = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'full_text': { "$regex": '#bidenforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#bidenforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Delaware', "$options" :'i' }},{'user.location': { "$regex": ', DE'}}]}]}).distinct("user.id")
bidendecount = 0
for user in bidendelaware:
	bidendecount = bidendecount + 1
print("Delaware:")
print("Trump: ", (trumpdecount/(trumpdecount+bidendecount)))
print("Biden: ",(bidendecount/(trumpdecount+bidendecount)))

trumpvermont = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'full_text': { "$regex": '#trumpforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#trumpforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Vermont', "$options" :'i' }},{'user.location': { "$regex": ', VT'}},{'user.location':{ "$regex": 'South Burlington', "$options" :'i' }}]}]}).distinct("user.id")
trumpvtcount = 0
for user in trumpvermont:
	trumpvtcount = trumpvtcount + 1
bidenvermont = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'full_text': { "$regex": '#bidenforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#bidenforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Vermont', "$options" :'i' }},{'user.location': { "$regex": ', VT'}},{'user.location':{ "$regex": 'South Burlington', "$options" :'i' }}]}]}).distinct("user.id")
bidenvtcount = 0
for user in bidenvermont:
	bidenvtcount = bidenvtcount + 1
print("Vermont:")
print("Trump: ", (trumpvtcount/(trumpvtcount+bidenvtcount)))
print("Biden: ",(bidenvtcount/(trumpvtcount+bidenvtcount)))

trumpoklahoma = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'full_text': { "$regex": '#trumpforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#trumpforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Oklahoma', "$options" :'i' }},{'user.location': { "$regex": ', OK'}},{'user.location':{ "$regex": 'Tulsa'}},{'user.location':{ "$regex": 'Norman', "$options" :'i' }},{'user.location':{ "$regex": 'Broken Arrow', "$options" :'i' }}]}]}).distinct("user.id")
trumpokcount = 0
for user in trumpoklahoma:
	trumpokcount = trumpokcount + 1
bidenoklahoma = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'full_text': { "$regex": '#bidenforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#bidenforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Oklahoma', "$options" :'i' }},{'user.location': { "$regex": ', OK'}},{'user.location':{ "$regex": 'Tulsa'}},{'user.location':{ "$regex": 'Norman', "$options" :'i' }},{'user.location':{ "$regex": 'Broken Arrow', "$options" :'i' }}]}]}).distinct("user.id")
bidenokcount = 0
for user in bidenoklahoma:
	bidenokcount = bidenokcount + 1
print("Oklahoma:")
print("Trump: ", (trumpokcount/(trumpokcount+bidenokcount)))
print("Biden: ",(bidenokcount/(trumpokcount+bidenokcount)))

trumparizona = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'full_text': { "$regex": '#trumpforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#trumpforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Arizona', "$options" :'i' }},{'user.location': { "$regex": ', AZ'}},{'user.location':{ "$regex": 'Phoenix', "$options" :'i' }},{'user.location':{ "$regex": 'Tucson', "$options" :'i' }},{'user.location':{ "$regex": 'Mesa'}},{'user.location':{ "$regex": 'Scottsdale', "$options" :'i' }}]}]}).distinct("user.id")
trumpazcount = 0
for user in trumparizona:
	trumpazcount = trumpazcount + 1
bidenarizona = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'full_text': { "$regex": '#bidenforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#bidenforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Arizona', "$options" :'i' }},{'user.location': { "$regex": ', AZ'}},{'user.location':{ "$regex": 'Phoenix', "$options" :'i' }},{'user.location':{ "$regex": 'Tucson', "$options" :'i' }},{'user.location':{ "$regex": 'Mesa'}},{'user.location':{ "$regex": 'Scottsdale', "$options" :'i' }}]}]}).distinct("user.id")
bidenazcount = 0
for user in bidenarizona:
	bidenazcount = bidenazcount + 1
print("Arizona:")
print("Trump: ", (trumpazcount/(trumpazcount+bidenazcount)))
print("Biden: ",(bidenazcount/(trumpazcount+bidenazcount)))

trumptexas = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'full_text': { "$regex": '#trumpforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#trumpforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Texas', "$options" :'i' }},{'user.location': { "$regex": ', TX'}},{'user.location':{ "$regex": 'Houston', "$options" :'i' }},{'user.location':{ "$regex": 'San Antonio', "$options" :'i' }},{'user.location':{ "$regex": 'Dallas', "$options" :'i' }},{'user.location':{ "$regex": 'Fort Worth', "$options" :'i' }}]}]}).distinct("user.id")
trumptxcount = 0
for user in trumptexas:
	trumptxcount = trumptxcount + 1
bidentexas = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'full_text': { "$regex": '#bidenforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#bidenforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Texas', "$options" :'i' }},{'user.location': { "$regex": ', TX'}},{'user.location':{ "$regex": 'Houston', "$options" :'i' }},{'user.location':{ "$regex": 'San Antonio', "$options" :'i' }},{'user.location':{ "$regex": 'Dallas', "$options" :'i' }},{'user.location':{ "$regex": 'Fort Worth', "$options" :'i' }}]}]}).distinct("user.id")
bidentxcount = 0
for user in bidentexas:
	bidentxcount = bidentxcount + 1
print("Texas:")
print("Trump: ", (trumptxcount/(trumptxcount+bidentxcount)))
print("Biden: ",(bidentxcount/(trumptxcount+bidentxcount)))

trumpconnecticut = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'full_text': { "$regex": '#trumpforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#trumpforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Connecticut', "$options" :'i' }},{'user.location': { "$regex": ', CT'}}]}]}).distinct("user.id")
trumpctcount = 0
for user in trumpconnecticut:
	trumpctcount = trumpctcount + 1
bidenconnecticut = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'full_text': { "$regex": '#bidenforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#bidenforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Connecticut', "$options" :'i' }},{'user.location': { "$regex": ', CT'}}]}]}).distinct("user.id")
bidenctcount = 0
for user in bidenconnecticut:
	bidenctcount = bidenctcount + 1
print("Connecticut:")
print("Trump: ", (trumpctcount/(trumpctcount+bidenctcount)))
print("Biden: ",(bidenctcount/(trumpctcount+bidenctcount)))

trumpiowa = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'full_text': { "$regex": '#trumpforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#trumpforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Iowa', "$options" :'i' }},{'user.location': { "$regex": ', IA'}}]}]}).distinct("user.id")
trumpiacount = 0
for user in trumpiowa:
	trumpiacount = trumpiacount + 1
bideniowa = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'full_text': { "$regex": '#bidenforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#bidenforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Iowa', "$options" :'i' }},{'user.location': { "$regex": ', IA'}}]}]}).distinct("user.id")
bideniacount = 0
for user in bideniowa:
	bideniacount = bideniacount + 1
print("Iowa:")
print("Trump: ", (trumpiacount/(trumpiacount+bideniacount)))
print("Biden: ",(bideniacount/(trumpiacount+bideniacount)))

trumpnorthcarolina = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'full_text': { "$regex": '#trumpforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#trumpforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'North Carolina', "$options" :'i' }},{'user.location': { "$regex": ', NC'}},{'user.location':{ "$regex": 'Raleigh', "$options" :'i' }},{'user.location':{ "$regex": 'Winston-Salem', "$options" :'i' }}]}]}).distinct("user.id")
trumpnccount = 0
for user in trumpnorthcarolina:
	trumpnccount = trumpnccount + 1
bidennorthcarolina = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'full_text': { "$regex": '#bidenforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#bidenforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'North Carolina', "$options" :'i' }},{'user.location': { "$regex": ', NC'}},{'user.location':{ "$regex": 'Raleigh', "$options" :'i' }},{'user.location':{ "$regex": 'Winston-Salem', "$options" :'i' }}]}]}).distinct("user.id")
bidennccount = 0
for user in bidennorthcarolina:
	bidennccount = bidennccount + 1
print("North Carolina:")
print("Trump: ", (trumpnccount/(trumpnccount+bidennccount)))
print("Biden: ",(bidennccount/(trumpnccount+bidennccount)))

trumpgeorgia = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'full_text': { "$regex": '#trumpforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#trumpforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Georgia', "$options" :'i' }},{'user.location': { "$regex": ', GA'}},{'user.location':{ "$regex": 'Macon'}},{'user.location':{ "$regex": 'Savannah', "$options" :'i' }}]}]}).distinct("user.id")
trumpgacount = 0
for user in trumpgeorgia:
	trumpgacount = trumpgacount + 1
bidengeorgia = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'full_text': { "$regex": '#bidenforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#bidenforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Georgia', "$options" :'i' }},{'user.location': { "$regex": ', GA'}},{'user.location':{ "$regex": 'Macon'}},{'user.location':{ "$regex": 'Savannah', "$options" :'i' }}]}]}).distinct("user.id")
bidengacount = 0
for user in bidengeorgia:
	bidengacount = bidengacount + 1
print("Georgia:")
print("Trump: ", (trumpgacount/(trumpgacount+bidengacount)))
print("Biden: ",(bidengacount/(trumpgacount+bidengacount)))

trumpsouthcarolina = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'full_text': { "$regex": '#trumpforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#trumpforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'South Carolina', "$options" :'i' }},{'user.location': { "$regex": ', SC'}},{'user.location':{ "$regex": 'North Charleston', "$options" :'i' }}]}]}).distinct("user.id")
trumpsccount = 0
for user in trumpsouthcarolina:
	trumpsccount = trumpsccount + 1
bidensouthcarolina = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'full_text': { "$regex": '#bidenforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#bidenforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'South Carolina', "$options" :'i' }},{'user.location': { "$regex": ', SC'}},{'user.location':{ "$regex": 'North Charleston', "$options" :'i' }}]}]}).distinct("user.id")
bidensccount = 0
for user in bidensouthcarolina:
	bidensccount = bidensccount + 1
print("South Carolina:")
print("Trump: ", (trumpsccount/(trumpsccount+bidensccount)))
print("Biden: ",(bidensccount/(trumpsccount+bidensccount)))

trumputa = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'full_text': { "$regex": '#trumpforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#trumpforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Utah', "$options" :'i' }},{'user.location': { "$regex": ', UT'}},{'user.location':{ "$regex": 'Salt Lake City', "$options" :'i' }},{'user.location':{ "$regex": 'West Valley City', "$options" :'i' }},{'user.location':{ "$regex": 'Provo'}},{'user.location':{ "$regex": 'West Jordan', "$options" :'i' }},{'user.location':{ "$regex": 'Orem'}}]}]}).distinct("user.id")
trumputcount = 0
for user in trumputa:
	trumputcount = trumputcount + 1
bidenuta = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'full_text': { "$regex": '#bidenforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#bidenforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Utah', "$options" :'i' }},{'user.location': { "$regex": ', UT'}},{'user.location':{ "$regex": 'Salt Lake City', "$options" :'i' }},{'user.location':{ "$regex": 'West Valley City', "$options" :'i' }},{'user.location':{ "$regex": 'Provo'}},{'user.location':{ "$regex": 'West Jordan', "$options" :'i' }},{'user.location':{ "$regex": 'Orem'}}]}]}).distinct("user.id")
bidenutcount = 0
for user in bidenuta:
	bidenutcount = bidenutcount + 1
print("Utah:")
print("Trump: ", (trumputcount/(trumputcount+bidenutcount)))
print("Biden: ",(bidenutcount/(trumputcount+bidenutcount)))

trumpida = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'full_text': { "$regex": '#trumpforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#trumpforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Idaho', "$options" :'i' }},{'user.location': { "$regex": ', ID'}},{'user.location':{ "$regex": 'Nampa'}}]}]}).distinct("user.id")
trumpidcount = 0
for user in trumpida:
	trumpidcount = trumpidcount + 1
bidenid = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'full_text': { "$regex": '#bidenforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#bidenforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Idaho', "$options" :'i' }},{'user.location': { "$regex": ', ID'}},{'user.location':{ "$regex": 'Nampa'}}]}]}).distinct("user.id")
bidenidcount = 0
for user in bidenid:
	bidenidcount = bidenidcount + 1
print("Idaho:")
print("Trump: ", (trumpidcount/(trumpidcount+bidenidcount)))
print("Biden: ",(bidenidcount/(trumpidcount+bidenidcount)))

trumpks = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'full_text': { "$regex": '#trumpforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#trumpforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Kansas', "$options" :'i' }},{'user.location': { "$regex": ', KS'}},{'user.location':{ "$regex": 'Overland Park', "$options" :'i' }}]}]}).distinct("user.id")
trumpkscount = 0
for user in trumpks:
	trumpkscount = trumpkscount + 1
bidenks = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'full_text': { "$regex": '#bidenforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#bidenforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Kansas', "$options" :'i' }},{'user.location': { "$regex": ', KS'}},{'user.location':{ "$regex": 'Overland Park', "$options" :'i' }}]}]}).distinct("user.id")
bidenkscount = 0
for user in bidenks:
	bidenkscount = bidenkscount + 1
print("Kansas:")
print("Trump: ", (trumpkscount/(trumpkscount+bidenkscount)))
print("Biden: ",(bidenkscount/(trumpkscount+bidenkscount)))

trumpne = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'full_text': { "$regex": '#trumpforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#trumpforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Nebraska', "$options" :'i' }},{'user.location': { "$regex": ', NE'}},{'user.location':{ "$regex": 'Omaha'}}]}]}).distinct("user.id")
trumpnecount = 0
for user in trumpne:
	trumpnecount = trumpnecount + 1
bidenne = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'full_text': { "$regex": '#bidenforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#bidenforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Nebraska', "$options" :'i' }},{'user.location': { "$regex": ', NE'}},{'user.location':{ "$regex": 'Omaha'}}]}]}).distinct("user.id")
bidennecount = 0
for user in bidenne:
	bidennecount = bidennecount + 1
print("Nebraska:")
print("Trump: ", (trumpnecount/(trumpnecount+bidennecount)))
print("Biden: ",(bidennecount/(trumpnecount+bidennecount)))

trumpri = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'full_text': { "$regex": '#trumpforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#trumpforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Rhode Island', "$options" :'i' }},{'user.location': { "$regex": ', RI'}},{'user.location':{ "$regex": 'Cranston', "$options" :'i' }},{'user.location':{ "$regex": 'Pawtucket', "$options" :'i' }}]}]}).distinct("user.id")
trumpricount = 0
for user in trumpri:
	trumpricount = trumpricount + 1
bidenri = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'full_text': { "$regex": '#bidenforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#bidenforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Rhode Island', "$options" :'i' }},{'user.location': { "$regex": ', RI'}},{'user.location':{ "$regex": 'Cranston', "$options" :'i' }},{'user.location':{ "$regex": 'Pawtucket', "$options" :'i' }}]}]}).distinct("user.id")
bidenricount = 0
for user in bidenri:
	bidenricount = bidenricount + 1
print("Rhode Island:")
print("Trump: ", (trumpricount/(trumpricount+bidenricount)))
print("Biden: ",(bidenricount/(trumpricount+bidenricount)))

trumpme = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'full_text': { "$regex": '#trumpforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#trumpforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Maine', "$options" :'i' }},{'user.location': { "$regex": ', ME'}},{'user.location':{ "$regex": 'South Portland', "$options" :'i' }}]}]}).distinct("user.id")
trumpmecount = 0
for user in trumpme:
	trumpmecount = trumpmecount + 1
bidenme = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'full_text': { "$regex": '#bidenforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#bidenforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Maine', "$options" :'i' }},{'user.location': { "$regex": ', ME'}},{'user.location':{ "$regex": 'South Portland', "$options" :'i' }}]}]}).distinct("user.id")
bidenmecount = 0
for user in bidenme:
	bidenmecount = bidenmecount + 1
print("Maine:")
print("Trump: ", (trumpmecount/(trumpmecount+bidenmecount)))
print("Biden: ",(bidenmecount/(trumpmecount+bidenmecount)))

trumpak = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'full_text': { "$regex": '#trumpforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#trumpforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Alaska', "$options" :'i' }},{'user.location': { "$regex": ', AK'}},{'user.location':{ "$regex": 'Anchorage', "$options" :'i' }},{'user.location':{ "$regex": 'Wasilla', "$options" :'i' }},{'user.location':{ "$regex": 'Sitka'}}]}]}).distinct("user.id")
trumpakcount = 0
for user in trumpak:
	trumpakcount = trumpakcount + 1
bidenak = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'full_text': { "$regex": '#bidenforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#bidenforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Alaska', "$options" :'i' }},{'user.location': { "$regex": ', AK'}},{'user.location':{ "$regex": 'Anchorage', "$options" :'i' }},{'user.location':{ "$regex": 'Wasilla', "$options" :'i' }},{'user.location':{ "$regex": 'Sitka'}}]}]}).distinct("user.id")
bidenakcount = 0
for user in bidenak:
	bidenakcount = bidenakcount + 1
print("Alaska:")
print("Trump: ", (trumpakcount/(trumpakcount+bidenakcount)))
print("Biden: ",(bidenakcount/(trumpakcount+bidenakcount)))

trumpmo = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'full_text': { "$regex": '#trumpforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#trumpforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Missouri', "$options" :'i' }},{'user.location': { "$regex": ', MO'}}]}]}).distinct("user.id")
trumpmocount = 0
for user in trumpmo:
	trumpmocount = trumpmocount + 1
bidenmo = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'full_text': { "$regex": '#bidenforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#bidenforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Missouri', "$options" :'i' }},{'user.location': { "$regex": ', MO'}}]}]}).distinct("user.id")
bidenmocount = 0
for user in bidenmo:
	bidenmocount = bidenmocount + 1
print("Missouri:")
print("Trump: ", (trumpmocount/(trumpmocount+bidenmocount)))
print("Biden: ",(bidenmocount/(trumpmocount+bidenmocount)))

trumpin = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#TeamTrump', "$options" :'i' }},{'full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'full_text': { "$regex": '#trumpforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Trump2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#trumpforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Indiana', "$options" :'i' }},{'user.location': { "$regex": ', IN'}},{'user.location':{ "$regex": 'Fort Wayne', "$options" :'i' }}]}]}).distinct("user.id")
trumpincount = 0
for user in trumpin:
	trumpincount = trumpincount + 1
bidenin = db.tweets.find({"$and":[{"$or":[{'retweeted_status.full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#TeamJoe', "$options" :'i' }},{'full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'full_text': { "$regex": '#bidenforpresident', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#Biden2020', "$options" :'i' }},{'retweeted_status.full_text': { "$regex": '#bidenforpresident', "$options" :'i' }}]},{"$or":[{'user.location':{ "$regex": 'Indiana', "$options" :'i' }},{'user.location': { "$regex": ', IN'}},{'user.location':{ "$regex": 'Fort Wayne', "$options" :'i' }}]}]}).distinct("user.id")
bidenincount = 0
for user in bidenin:
	bidenincount = bidenincount + 1
print("Indiana:")
print("Trump: ", (trumpincount/(trumpincount+bidenincount)))
print("Biden: ",(bidenincount/(trumpincount+bidenincount)))