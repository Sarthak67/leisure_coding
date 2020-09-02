import requests
import re
from bs4 import BeautifulSoup
import json
import pprint
import ast
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient["clubDB"]
clubDB = db["players"]

quote_page = 'http://www.squawka.com/football-stats/english-premier-league-season-2017-2018'

response = requests.post(quote_page)

teams=[]
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find( "table", {"id":"rd-league-standings"} )
rank= table.find_all("a",{"class":"fsclt-club-link"})
for r in rank:
	xx=str(r).split('<!--')
	teams.append(xx[0].split('href=')[1].split('>\n')[0])

#filename = 'Club'
#clubDB = db.DB()
#clubDB.open(filename, None, db.DB_HASH, db.DB_CREATE)


for t in teams:

	quote = t[1:len(t)-1]+'#performance-score#english-barclays-premier-league#season-2017/2018#819#all-matches#1-38#by-match'
	pos=['players-card Defe','players-card Midf','players-card Forw']
	player=[]
	lin=[]
	players = {}

	responsex = requests.post(quote)

	
	for i in pos:
		soupx = BeautifulSoup(responsex.text, 'html.parser')
		mydivs = soupx.findAll("li", {"class": i})
		#scripts = mydivs.find_all("span",{"class":"name"})
		soup1 = BeautifulSoup(str(mydivs), 'html.parser')
		scripts = soup1.findAll("span", {"class":"name"})
	
		for s in scripts:
			lin.append(s)
		for a in soup1.find_all('a', href=True):
			player.append(a['href'])
	player =[p for p in player if p]
	print(player)
	for link in player:
		dic={}
		dicc={}
		quote_page1 = link+'#performance-score#'+t[30:].split('/')[0]+'-(current)#english-barclays-premier-league#8#season-2017/2018#819#all-matches#1-38#by-match'
		print(quote_page1)
		classified= quote_page1.split("players/")
		clasClassified= classified[1].split("status#")
		response1 = requests.post(quote_page1)
		
		soup1 = BeautifulSoup(response1.text, 'html.parser')
		scripts1 = soup1.find_all('script')

		s= scripts1[34].text.split("/** Pie chart changes */")
		s1=s[0].split("/** End */")
		x =s1[0].split("/** Overtime */")
		j = x[1].split(";")

		for i in range(len(j)-1):
			x=j[i].split('=')
			dic[x[0].split(" ")[1].strip()]=x[1][2:]
		x=0

		for i in range(0,len(j)-1,2):
			dic[j[i].strip()]=j[i+1]
		#print(dic['obj_sq_awards'])
		#d = json.loads(j)

		#print(x)
		#pprint.pprint(dic['global_duels_won_overtime'])

		keys=['obj_sq_awards',
		'global_goal_scored_overtime',
		'global_keypasses_overtime',
		'global_shot_accuracy_overtime',
		'global_interception_overtime',
		'global_cards_overtime',
		'global_pass_len_overtime',
		'global_duels_won',
		'global_duels_won_overtime']

		for key in range(9):
			dic1={}
			x= dic[keys[key]].split('],[')
			m=(x[0].split(']'))
			m1=m[0].split(',')
			#print(key)

			for i in range(1,len(x)):
				y=x[i].split(',')
				dic2={}
				for k in range(len(y)):	
					dic2[m1[k].strip()[1:len(m1[k])-2]]=y[k].strip()
			

				dic1[y[0][1:len(y[0])-1]]=dic2


			dicc[keys[key]]=dic1


		dicc['obj_sq_awards']=ast.literal_eval("{"+str(dic['obj_sq_awards'].replace('"',"'")))
		dicc['global_duels_won']=ast.literal_eval("{"+str(dic['global_duels_won'].replace('"',"'")))
		players[clasClassified[0]]=dicc
	pprint.pprint(players)
	clubDB.insert_many(players)

client.close()