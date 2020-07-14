# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
# import os
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
# import subprocess
#
#
# class ActionSearchVMState(Action):
#
#     def name(self) -> Text:
#         return "action_search_vmstate"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         res = os.popen("st2 run core.local cmd=vmstat").read()
#         print(res)
#         print(type(res))
#         # p = subprocess.Popen(['vmstat', ''], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#         # out, err = p.communicate()
#         # print(out)
#         # print(type(out))
#
#         dispatcher.utter_message(text="hello world")
#
#         return []

from typing import Dict, Text, Any, List, Union, Optional
from rasa_sdk.forms import FormAction
from typing import Dict, Text, Any, List, Union
from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset, SlotSet, EventType
from rasa_sdk.forms import FormAction, REQUESTED_SLOT
from markdownify import markdownify as md



# class ActionWeather(FormAction):
#     def name(self):
#         # self.name = 'weather_form'
#         # print('我执行了name方法啦 666666666666666')
#         return 'weather_form'
#
#     @staticmethod
#     def required_slots(tracker: Tracker) -> List[Text]:
#         '''
#                 print tracker information
#         '''
#         # print('latest_message777777777777777',tracker.latest_message)
#         intent = tracker.latest_message['intent'].get('name')
#         print('%'*30)
#         print('intent name 111111111',intent)
#
#         print('%' * 30)
#         required_slots_list = relation_required_entity_mapping[intent]
#         # print('required_slots_list 111111111', required_slots_list)
#         return required_slots_list
#         # return ["location", "date_time"]
#         # required_slots_list = relation_required_entity_mapping[intent]
#         # print('ddddddddd',required_slots_list)
#         # return required_slots_list
#
#     def submit(self, dispatcher: CollectingDispatcher,
#                tracker: Tracker,
#                domain: Dict[Text, Any]) -> List[Dict]:
#         # intent = tracker.latest_message['intent'].get('name')
#
#         location = tracker.get_slot("location")
#         if location is None:
#             dispatcher.utter_template('utter_ask_location',tracker)
#
#         date_time = tracker.get_slot("date_time")
#         if date_time is None:
#             dispatcher.utter_template('utter_ask_date_time', tracker)
#
#         temperature_c = '27'
#         humidity = '33'
#         wind_mph = '8m/s'
#         response = """the city  {} in {}. The temperature is {} degrees, the humidity is {}% and the wind speed is {} mph.""".format(
#             location, date_time, temperature_c, humidity, wind_mph)
#
#         dispatcher.utter_message(response)
#
#         return [SlotSet("location", None), SlotSet("date_time", None)]


# class ActionCpu(FormAction):
#     def name(self):
#         # self.name = 'cpu_form'
#         return 'cpu_form'
#
#     @staticmethod
#     def required_slots(tracker: Tracker) -> List[Text]:
#         intent = tracker.latest_message['intent'].get('name')
#         print('%' * 30)
#         print('intent name 111111111', intent)
#         # print('latest_message777777777777777', tracker.latest_message)
#         # print('latest_action_name2222222', tracker.latest_action_name)
#         # print('slots   2222222', tracker.slots)
#         #
#         print('%' * 30)
#         required_slots_list = relation_required_entity_mapping[intent]
#         # print('required_slots_list 111111111', required_slots_list)
#         return required_slots_list
#         # return ["ip","direction"]
#
#     def submit(self, dispatcher: CollectingDispatcher,
#                tracker: Tracker,
#                domain: Dict[Text, Any]) -> List[Dict]:
#         # intent = tracker.latest_message['intent'].get('name')
#
#         ip = tracker.get_slot("ip")
#         direction = tracker.get_slot("direction")
#
#         response = ip + " and " + direction
#
#         dispatcher.utter_message(response)
#
#         return [SlotSet("ip", None), SlotSet("direction", None)]



# class Actionform(FormAction):
#     def name(self):
#         # self.name = 'cpu_form'
#         return 'action_form'
#
#     @staticmethod
#     def required_slots(tracker: Tracker) -> List[Text]:
#         intent = tracker.latest_message['intent'].get('name')
#         required_slots_list = relation_required_entity_mapping[intent]
#         return required_slots_list
#
#
#     def submit(self, dispatcher: CollectingDispatcher,
#                tracker: Tracker,
#                domain: Dict[Text, Any]) -> List[Dict]:
#         # intent = tracker.latest_message['intent'].get('name')
#
#         ip = tracker.get_slot("ip")
#         direction = tracker.get_slot("direction")
#
#         response = ip + " and " + direction
#
#         dispatcher.utter_message(response)
#
#         return [SlotSet("ip", None), SlotSet("direction", None)]


gragh_mapping = {
    "configuration":["microservice","ip","cpu","memory"],
    "status":["ip","cpu"],
    "configuration" + "+" + "ip":["microservice","memory","cpu"],
    "configuration" + "+" + "microservice":["ip"],
    "configuration" + "+" + "cpu":["ip"],
    "configuration" + "+" + "memory":["ip"],
    "status" + "+" + "ip": ["cpu"],
    "status" + "+" + "cpu": ["ip"]
}



ip_data = {
    "2.2.2.2":[{"cpu":"64core"},{"cpu":"30%"},{"microservice":["ms1","ms2"]}],
    "1.1.1.1":[{"cpu":"64core"},{"cpu":"40%"},{"memory":"32G"},{"microservice":"ms1"}]
}
microservice_data = {
    "ms1":[{"ip":["1.1.1.1","2.2.2.2"]}],
    "ms2":[{"ip":"2.2.2.2"}]
}

cpu_C_data = {
    "64core":[{"ip":"2.2.2.2"}],
    "32core":[{"ip":"1.1.1.1"}]
}

cpu_S_data = {
    "30%":[{"ip":"2.2.2.2"}],
    "40%":[{"ip":"1.1.1.1"}]
}

memory_data = {
    "32G":[{"ip":"1.1.1.1"}]
}
from rasa.core.events import Restarted
class Action_configuration(Action):
    def __init__(self):
        self.spo = set()
        self.spo.add("configuration")
        self.inetnt = "configuration"
        self.utter_ask = True
        #initial方法只执行一次
    def name(self) -> Text:
        return "configuration_action"
    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]):
        possible_s = gragh_mapping["configuration"]
        input_text = tracker.latest_message["text"]
        input_text = str(input_text).lower()


        if tracker.get_slot('s') is not None:
            print('按钮选择器种的S是：',tracker.get_slot('s'))
            self.spo.add(tracker.get_slot('s'))
        for slot in possible_s:
            if slot in input_text:#在文本种直接输入了需要查询的实体，比如我要查CPU
                if len(self.spo) < 3:
                    print('通过关键字匹配添加了一元：',slot)
                    self.spo.add(slot)
            if tracker.get_slot(slot) is not None:#在文本种直接输入了具体的实体值，比如1。1.1.1
                if len(self.spo) < 3:
                    print('通过实体提取，添加了一元：',slot)
                    self.spo.add(slot)
        for node in list(self.spo):
            if node != "configuration":
                if tracker.get_slot(node) is not None:
                    print('**************',tracker.get_slot(node))
                    self.utter_ask = False
        if len(self.spo) > 1:
            spo = "configuration" + "+"
            for node in list(self.spo):
                if node != "configuration":
                    spo += str(node)
            print('目前拿到的spo：',spo)
            if spo in gragh_mapping.keys():#表示spo里只有2元
                print('目前拿到的两元：',spo)
                need_slots = gragh_mapping[spo]
                buttons = []
                for slot in need_slots:
                    buttons.append(
                        {"title": "{}".format(slot),
                         "payload": '/configuration{{"s":"{0}"}}'.format(slot)})
                    dispatcher.utter_button_message("according to your inputs, pls select your entity", buttons)
            else:#已经确定三元了
                s_left = select_s(list(self.spo))
                # print('**************************************************',s_left,tracker.get_slot(s_left))
                if self.utter_ask :
                    print('999999999999999999999999999999999999999999999999999999999999999')
                    dispatcher.utter_template('utter_ask_' + s_left, tracker)
                else:
                    responce = "you select fixed spo:  {0}，and the left entity's slot is: {1}".format(' '.join(list(self.spo)),tracker.get_slot(s_left))
                    dispatcher.utter_message(responce)
        else:#what is the configuration本身只有一元的情况
            buttons = []
            for slot in possible_s:
                buttons.append(
                    {"title": "{}".format(slot),
                     "payload": '/configuration{{"s":"{0}"}}'.format(slot)})
            dispatcher.utter_button_message("according to your inputs, pls select your entity", buttons)
            print('2222222222',list(self.spo))
            if len(self.spo) == 3:
                s_left = select_s(list(self.spo))
                if tracker.get_slot(s_left) is None:
                    dispatcher.utter_message(template='utter_ask_' + s_left)
                else:
                    responce = "you select fixed spo {0}，and the left entity's slot is{1}".format(' '.join(list(self.spo)), tracker.get_slot(s_left))
                    dispatcher.utter_message(responce)
        return []


def select_s(spo):
    if "ip" in spo and "cpu" in spo:
        return "ip"
    elif "ip" in spo and "memory" in spo:
        return "ip"
    elif "ip" in spo and "microservice" in spo:
        return "microservice"

class Action_status(Action):
    def __init__(self):
        self.spo = set()
        self.spo.add("status")

    def name(self) -> Text:
        return "status_action"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]):
        possible_s = gragh_mapping["status"]
        input_text = tracker.latest_message["text"]
        input_text = str(input_text).lower()
        if tracker.get_slot('s') is not None:
            print('按钮选择器种的S是：', tracker.get_slot('s'))
            self.spo.add(tracker.get_slot('s'))
        for slot in possible_s:
            if slot in input_text:  # 在文本种直接输入了需要查询的实体，比如我要查CPU
                if len(self.spo) < 3:
                    print('通过关键字匹配添加了一元：', slot)
                    self.spo.add(slot)
            if tracker.get_slot(slot) is not None:  # 在文本种直接输入了具体的实体值，比如1。1.1.1
                if len(self.spo) < 3:
                    print('通过实体提取，添加了一元：', slot)
                    self.spo.add(slot)
        if len(self.spo) > 1:
            spo = "status" + "+"
            for node in list(self.spo):
                if node != "status":
                    spo += str(node)
            print('目前拿到的spo：', spo)
            if spo in gragh_mapping.keys():  # 表示spo里只有2元
                print('目前拿到的两元：', spo)
                need_slots = gragh_mapping[spo]
                buttons = []
                for slot in need_slots:
                    buttons.append(
                        {"title": "{}".format(slot),
                         "payload": '/status{{"s":"{0}"}}'.format(slot)})
                    dispatcher.utter_button_message("according to your inputs, pls select your entity", buttons)
            else:  # 已经确定三元了
                s_left = select_s(list(self.spo))
                if tracker.get_slot(s_left) is None:
                    dispatcher.utter_template('utter_ask_' + s_left, tracker)
                else:
                    responce = "you select fixed spo {0}，and the left entity's slot is{1}".format(' '.join(list(self.spo)), tracker.get_slot(s_left))
                    dispatcher.utter_message(responce)
        else:  # what is the configuration本身只有一元的情况
            buttons = []
            for slot in possible_s:
                buttons.append(
                    {"title": "{}".format(slot),
                     "payload": '/status{{"s":"{0}"}}'.format(slot)})
            dispatcher.utter_button_message("according to your inputs, pls select your entity", buttons)
            print('2222222222', list(self.spo))
            if len(self.spo) == 3:
                s_left = select_s(list(self.spo))
                if tracker.get_slot(s_left) is None:
                    dispatcher.utter_message(template='utter_ask_' + s_left)
                else:
                    responce = "you select fixed spo {0}，and the left entity's slot is{1}".format(' '.join(list(self.spo)), tracker.get_slot(s_left))
                    dispatcher.utter_message(responce)
        return []

# class ActionDonKnow(Action):
#     def name(self) -> Text:
#         return "action_donknow"
#
#     def run(self,
#             dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]):
#         dispatcher.utter_template("utter_donknow", tracker)
#         # dispatcher.utter_template("utter_howcanhelp", tracker)
#         dispatcher.utter_message(md("you can ask me like these: <br/>configuration<br/>\
#                                       configuration of ip<br/>\
#                                       status of ip<br/>\
#                                       status of cpu<br/>\
#                                       configuration of cpu<br/>\
#                                       configuration of memory<br/>"))
#         return []

        # s_entity = tracker.get_slot('s_cpu')
        # if s_entity is None:
        #     buttons = []
        #     for t in possible_s:
        #         buttons.append(
        #             {"title": "{}".format(t),
        #              "payload": '/search_cpu{{"s_cpu":"{0}"}}'.format(t)})
        #     dispatcher.utter_button_message("根据你的描述，请你选择你要查询的 s_cpu ", buttons)
        # else:
        #     extracted_entity = tracker.get_slot(s_entity)
        #     if extracted_entity is None:
        #         dispatcher.utter_template('utter_ask_'+s_entity , tracker)
        #     else:
        #         dispatcher.utter_message(
        #             "According to the system, when {0} is:{1}, the CPU state is good".format(s_entity,extracted_entity))
        # return []


















def make_button(title, payload):
    return {'title': title, 'payload': payload}


# class Actioncpu(Action):
#     def name(self) -> Text:
#         return "search_cpu_action"
#     def run(self,
#             dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]):
#
#         intent = tracker.latest_message['intent'].get('name')
#         print('2222222222222222222222',tracker.latest_message)
#         possible_s = s_p_mapping[intent]
#
#         s_entity = tracker.get_slot('s_cpu')
#         if s_entity is None:
#             buttons = []
#             for t in possible_s:
#                 buttons.append(
#                     {"title": "{}".format(t),
#                      "payload": '/search_cpu{{"s_cpu":"{0}"}}'.format(t)})
#             dispatcher.utter_button_message("根据你的描述，请你选择你要查询的 s_cpu ", buttons)
#         else:
#             extracted_entity = tracker.get_slot(s_entity)
#             if extracted_entity is None:
#                 dispatcher.utter_template('utter_ask_'+s_entity , tracker)
#             else:
#                 dispatcher.utter_message(
#                     "According to the system, when {0} is:{1}, the CPU state is good".format(s_entity,extracted_entity))
#         return []


# class Actionip(Action):
#     def name(self) -> Text:
#         return "search_ip_action"
#     def run(self,
#             dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]):
#
#         intent = tracker.latest_message['intent'].get('name')
#         possible_s = s_p_mapping[intent]
#
#         s_entity = tracker.get_slot('s_ip')
#         if s_entity is None:
#             buttons = []
#             for t in possible_s:
#                 buttons.append(
#                     {"title": "{}".format(t),
#                      "payload": '/search_ip{{"s_ip":"{0}"}}'.format(t)})
#             dispatcher.utter_button_message("根据你的描述，请你选择你要查询的 s_ip ", buttons)
#         else:
#             extracted_entity = tracker.get_slot(s_entity)
#             if extracted_entity is None:
#                 print('s_entity is :',s_entity)
#                 dispatcher.utter_template('utter_ask_'+s_entity , tracker)
#             else:
#                 dispatcher.utter_message(
#                     "According to the system, when {0} is:{1}, the ip state is bad".format(s_entity,extracted_entity))
#
#         return []

# class ActionCpu2(FormAction):
#     def name(self):
#         # self.name = 'cpu_form'
#         return 'search_cpu_action'
#
#     @staticmethod
#     def required_slots(tracker: Tracker) -> List[Text]:
#         intent = tracker.latest_message['intent'].get('name')
#         required_slots_list = relation_required_entity_mapping[intent]
#         return required_slots_list
#
#     def submit(self, dispatcher: CollectingDispatcher,
#                tracker: Tracker,
#                domain: Dict[Text, Any]) -> List[Dict]:
#         # intent = tracker.latest_message['intent'].get('name')
#
#         ip = tracker.get_slot("ip")
#         direction = tracker.get_slot("direction")
#
#         response = ip + " and " + direction
#
#         dispatcher.utter_message(response)
#
#     return [SlotSet("ip", None), SlotSet("direction", None)]
#         # buttons = []
#         # if len(possible_s) > 1:
#         #     for d in possible_s:
#         #         buttons.append(make_button(d, '/search_cpu'))
#         #     dispatcher.utter_button_message("请点击选择你要的查询，若没有想要的，请忽略此消息", buttons)
#         # elif len(possible_s) == 1:
#         #     required_slot = possible_s[0]
#         #     required_entity = tracker.get_slot(required_slot)
#         #     if required_entity is None:
#         #         dispatcher.utter_template('utter_ask_'+required_slot , tracker)
#         #     else:
#         #         dispatcher.utter_message("According to the system, the IP is:{0}, the CPU state is good".format(required_entity))
#         # else:
#         #
#         # return []



