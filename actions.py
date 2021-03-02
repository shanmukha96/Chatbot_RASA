from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
from rasa_sdk.events import AllSlotsReset
from rasa_sdk.events import Restarted
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.message import EmailMessage
import zomatopy
import json
import smtplib 
import pprint, json
import zomatopy
import requests


cities = ['ahmedabad','bengaluru',' bangalore', 'chennai','madras', 'delhi','new delhi', 'hyderabad',
		 'kolkata', 'culcatta' ,'mumbai','bombay', 'pune', 'agra', 'ajmer','aligarh', 'amravati','amaravati', 'amritsar',
		  'asansol', 'aurangabad', 'bareilly', 'belgaum', 'bhavnagar', 'bhiwandi', 'bhopal', 
		  'bhubaneswar', 'bikaner', 'bilaspur', 'bokaro', 'chandigarh', 'coimbatore', 
		  'cuttack', 'dehradun', 'dhanbad', 'bhilai', 'durgapur', 'erode', 'faridabad', 
		  'firozabad', 'ghaziabad', 'gorakhpur', 'gulbarga', 'guntur', 'gwalior', 'gurgaon', 
		  'guwahati', 'hamirpur', 'hubli–dharwad', 'indore', 'jabalpur', 'jaipur', 'jalandhar', 
		  'jammu', 'jamnagar', 'jamshedpur', 'jhansi', 'jodhpur', 'kakinada', 'kannur', 
		  'kanpur', 'kochi', 'kolhapur', 'kollam', 'kozhikode', 'kurnool', 'ludhiana', 
		  'lucknow', 'madurai', 'malappuram', 'mathura', 'goa', 'mangalore', 'meerut', 
		  'moradabad', 'mysore', 'nagpur', 'nanded', 'nashik', 'nellore', 'noida', 'patna', 
		  'pondicherry', 'purulia prayagraj', 'raipur', 'rajkot', 'rajahmundry', 'ranchi', 
		  'rourkela', 'salem', 'sangli', 'shimla', 'siliguri', 'solapur', 'srinagar', 'surat', 
		  'thiruvananthapuram', 'thrissur', 'tiruchirappalli', 'tiruppur', 'ujjain', 'bijapur',
		   'vadodara', 'varanasi', 'vasai-virar', 'vijayawada','vijaywada', 'visakhapatnam', 'vellore', 
		   'warangal']


res=''
res1=''

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'


	def fetch(self,loc='bangalore',cuisine='north indian',price='high'):
		
		#adjust the price range
		price_min = 0
		price_max = 99999
		if price == 'low':
			price_max = 300
		elif price == 'mid':
			price_min = 300
			price_max = 700
		elif price == 'high':
			price_min = 700
		else:
			price_min = 300
			price_max = 9999
		
		# provide API key and initialise a 'zomato app' object
		config={ "user_key": "4734a24a9caf5cd3ae0a0e9161e66212"}
		zomato = zomatopy.initialize_app(config)
		cuisines_dict={'american': 1,'chinese': 25, 'north indian': 50, 'italian': 55, 'mexican': 73, 'south indian': 85, 'thai': 95}

		# get_location gets the lat-long coordinates of 'loc'
		loc_detail=zomato.get_location(loc, 1)
		loc_detail=json.loads(loc_detail)
		if loc_detail['status'] == 'success':
			data =  zomato.restaurant_search( query='', latitude=loc_detail['location_suggestions'][0]['latitude'], longitude=loc_detail['location_suggestions'][0]['longitude'], cuisines=str(cuisines_dict.get(cuisine)), limit=100)
			data = json.loads(data)
			global res
			if data['results_found'] > 0:
				added=0
				for i in data['restaurants']:
					if i['restaurant']['average_cost_for_two'] > price_min and i['restaurant']['average_cost_for_two'] < price_max and added < 5:
						res = res + "\n\nRestaurant: "+str(i['restaurant']['name'])+" in "+str(i['restaurant']['location']['address'])+"\nCost for 2 people: "+str(i['restaurant']['average_cost_for_two'])+"\nRating :"+str(i['restaurant']['user_rating']['aggregate_rating'])
						added = added +1
				if len(res) == 0:
					SlotSet('results_found',False)
					return "no results found"
			return "Showing you the top rated restaurants:"+ res

		else:
			return 0


			


	def run(self, dispatcher, tracker, domain):
		#config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
		#zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		if loc == None:
			return dispatcher.utter_message('Location got is None')
		if loc.lower() not in cities:
			dispatcher.utter_message("Sorry, we don't operate in your location.")
			return [AllSlotsReset()]
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')
		res=''
		if cuisine == None or price == None:
				dispatcher.utter_message("I didn't get all details, deafault results will be shown")
				cuisine = 'north'
				price = 'mid'
		
		else:
			res = self.fetch(loc,cuisine,price)
			dispatcher.utter_message(res+"\n\n\n")
			 




class ActionSendEmail(Action):
	def name(self):
		return 'action_send_email'


	def fetch(self,loc='delhi',cuisine='north indian',price='high'):
		
		#adjust the price range
		price_min = 0
		price_max = 99999
		if price == 'low':
			price_max = 300
		elif price == 'mid':
			price_min = 300
			price_max = 700
		elif price == 'high':
			price_min = 700
		else:
			price_min = 300
			price_max = 9999
		
		# provide API key and initialise a 'zomato app' object
		config={ "user_key": "4734a24a9caf5cd3ae0a0e9161e66212"}
		zomato = zomatopy.initialize_app(config)
		cuisines_dict={'american': 1,'chinese': 25, 'north indian': 50, 'italian': 55, 'mexican': 73, 'south indian': 85, 'thai': 95}

		# get_location gets the lat-long coordinates of 'loc'
		loc_detail=zomato.get_location(loc, 1)
		loc_detail=json.loads(loc_detail)
		if loc_detail['status'] == 'success':
			lat = loc_detail['location_suggestions'][0]['latitude']
			lon = loc_detail['location_suggestions'][0]['longitude']
			data =  zomato.restaurant_search( query='', latitude=lat, longitude=lon, cuisines=str(cuisines_dict.get(cuisine)), limit=200)
			data = json.loads(data)
			global res1
			if data['results_found'] > 0:
				added=0
				for i in data['restaurants']:
					if i['restaurant']['average_cost_for_two'] > price_min and i['restaurant']['average_cost_for_two'] < price_max and added < 5:
						res1 = res1 + "\n\nRestaurant: "+str(i['restaurant']['name'])+" in "+str(i['restaurant']['location']['address'])+"\nCost for 2 people: "+str(i['restaurant']['average_cost_for_two'])+"\nRating :"+str(i['restaurant']['user_rating']['aggregate_rating'])
						added = added +1
					if len(res1) == 0:
						return "can't get anything with your preferances"

				return "Showing you the top rated restaurants:\n \n"+ res1
			else:
				return "can't retrive data properly"

		else:
			return "results not found..!!"


			


	def run(self, dispatcher, tracker, domain):
		#config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
		#zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')
		res = self.fetch(loc,cuisine,price)
		email = tracker.get_slot('email')

		msg = EmailMessage()
		msg['Subject'] = 'Foodie Chatbot - Search Result'
		s = smtplib.SMTP('smtp.gmail.com', 587)
		s.starttls() 
		try:
			s.login("shanmukha.ravi@gmail.com", "phoenix999")
		except:
			dispatcher.utter_message('security issue while logging in')
			return [AllSlotsReset()]
		message = "Showing you the top rated restaurants:"
		message = message + res
		try:
			s.sendmail("shanmukha.ravi@gmail.com", str(email), message)
			s.quit()
			dispatcher.utter_message("")
			return [AllSlotsReset()]
		except:
			dispatcher.utter_message("Can't send the email. deleted your preferances")
			return [AllSlotsReset()]

