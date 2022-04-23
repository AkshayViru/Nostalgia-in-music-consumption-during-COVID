import csv
import requests
from bs4 import BeautifulSoup as bs
from datetime import date, timedelta

start_date = date(2022, 1, 1)
end_date = date(2022, 3, 31)
delta = timedelta(days=1)
countries_short = ['be', 'fr', 'it', 'es', 'se', 'gb']
countries_long = ['Belgium', 'France', 'Italy', 'Spain', 'Sweden', 'UnitedKingdom']
columns = ['Rank', 'Track ID']

def getTrackIDs(url):
	headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}
	x = requests.get(url, headers=headers)  
	htmlContent = bs(x.content,'html.parser')

	trackIDs = []
	idx = 1

	print(url)
	for link in htmlContent.find_all('a', href=True):
	    lst = str(link['href']).split('/')
	    if(len(lst[-1]) == 22):
	    	trackIDs.append([idx, lst[-1]])
	    	idx += 1

	return trackIDs

for i in range(len(countries_long)):
    s_date = start_date
    print(countries_long[i])
    
    while s_date <= end_date:
        print(s_date)
        url = 'https://spotifycharts.com/regional/'+countries_short[i]+'/daily/' + str(s_date)
        trackIDs = getTrackIDs(url)
        fileName = './dataset/'+countries_long[i]+'/2022/' + countries_short[i] + '_' + str(s_date) + '_data.csv'

        with open(fileName, 'w', newline='') as csvfile: 
        	csvwriter = csv.writer(csvfile) 
        	csvwriter.writerow(columns) 
        	csvwriter.writerows(trackIDs)

        s_date += delta