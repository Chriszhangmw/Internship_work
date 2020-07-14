from rasa_sdk.forms import FormAction
from typing import Dict, Text, Any, List, Union
from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


relation_required_entity_mapping = {
    "request_weather":["location", "date_time"],
    "request_cpu":["ip","direction"]
}

class ActionWeather(FormAction):
    def name(self):
        self.name = 'weather_form'
        return 'weather_form'

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        intent = tracker.latest_message['intent'].get('name')
        required_slots_list = relation_required_entity_mapping[intent]
        return required_slots_list

    def submit(self, dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        # intent = tracker.latest_message['intent'].get('name')

        location = tracker.get_slot("location")
        date_time = tracker.get_slot("date_time")

        city = location
        temperature_c = '27'
        humidity = '33'
        wind_mph = '8m/s'
        response = """the city  {} in {}. The temperature is {} degrees, the humidity is {}% and the wind speed is {} mph.""".format(
            city, date_time, temperature_c, humidity, wind_mph)

        dispatcher.utter_message(response)

        return [SlotSet("location", None), SlotSet("date_time", None)]


class ActionCpu(FormAction):
    def name(self):
        self.name = 'weather_form'
        return 'cpu_form'

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        intent = tracker.latest_message['intent'].get('name')
        required_slots_list = relation_required_entity_mapping[intent]
        return required_slots_list

    def submit(self, dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        # intent = tracker.latest_message['intent'].get('name')

        ip = tracker.get_slot("ip")
        direction = tracker.get_slot("direction")

        response = ip + "," + direction

        dispatcher.utter_message(response)

        return [SlotSet("ip", None), SlotSet("direction", None)]