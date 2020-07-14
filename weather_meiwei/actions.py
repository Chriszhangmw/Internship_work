from rasa_sdk.forms import FormAction
from typing import Dict, Text, Any, List, Union
from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionWeather(FormAction):
	def name(self):
		return 'weather_form'

	@staticmethod
	def required_slots(tracker: Tracker) -> List[Text]:
		#这个地方可以考虑用查询
		return ["location", "date_time"]

	def submit(self, dispatcher: CollectingDispatcher,
			   tracker: Tracker,
			   domain: Dict[Text, Any]) -> List[Dict]:
		location = tracker.get_slot("location")
		date_time = tracker.get_slot("date_time")

		city = location
		temperature_c = '27'
		humidity = '33'
		wind_mph = '8m/s'
		response = """the city  {} in {}. The temperature is {} degrees, the humidity is {}% and the wind speed is {} mph.""".format(city, date_time,temperature_c, humidity, wind_mph)

		dispatcher.utter_message(response)

		return [SlotSet("location", None), SlotSet("date_time", None)]
		
	# def run(self, dispatcher, tracker, domain):
	# 	import requests
	# 	loc = tracker.get_slot('location')
	# 	params = {
	# 		'access_key': '7362a8270e7fe3f3505f0e2efaaaca51',
	# 		'query': loc
	# 	}
	# 	# api_result = requests.get('http://api.weatherstack.com/current', params)
	# 	# current = api_result.json()
	# 	# city = current['location']['name']
	# 	#
	# 	# temperature_c = current['current']['temperature']
	# 	# humidity = current['current']['humidity']
	# 	# wind_mph = current['current']['wind_speed']
	# 	city = loc
	# 	temperature_c = '27'
	# 	humidity = '33'
	# 	wind_mph = '8m/s'
	# 	response = """the city  {} at the moment. The temperature is {} degrees, the humidity is {}% and the wind speed is {} mph.""".format(
	# 		city, temperature_c, humidity, wind_mph)
	#
	# 	dispatcher.utter_message(response)
	# 	return [SlotSet('location', loc)]

