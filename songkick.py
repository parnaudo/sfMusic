import requests
import json
import datetime
from random import randint
#Independent,Mezzanine,Fillmore,Warfield,Slims,Fox,Great American Music Hall,Bottom of the Hill,Rickshaw, The Chapel,Brick and Mortar,New Parrish, Greek Theater
venues = [324,329,6239,949,953251,1261,248,14791,2029634,841]
#venues = [324,841]
#NEED A BETTER KEY!
def toEpoch(dt, epoch=datetime.datetime(1970,1,1)):
    td = dt - epoch
    # return td.total_seconds()
    return (td.microseconds + (td.seconds + td.days * 86400) * 10**6) / 10**6 
output = {}
count = 0
for venue in venues:
	print "Venue:",venue
	url = 'http://api.songkick.com/api/3.0/venues/{0}/calendar.json?apikey=iQWY8WbevwmBCzR4'.format(venue)
	r = requests.get(url)

	data = r.json()
	#print data['resultsPage']['results']

	for row in data['resultsPage']['results']['event']:
		start_date = datetime.datetime.strptime(row['start']['date'], '%Y-%m-%d')
		epoch_timestamp = int(toEpoch(start_date)) + randint(0,1000)
		output_string = row['start']['date'],row['displayName']
	#	output_string = row['displayName'],row['venue']['displayName'],startDate,row['start']['time']
		output[epoch_timestamp]= output_string
		count += 1
		# print row['displayName'],row['venue']['displayName'],startDate,row['start']['time']

# print output	
# print whatsthis
for row in sorted(output,key=output.get):
	print  row,output[row]
print "found: ",count