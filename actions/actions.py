from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import AllSlotsReset

from communication import send


class ActionConfirmAddEvent(Action):

    def name(self) -> Text:
        return "action_confirm_add_event"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("confirm adding event")

        dispatcher.utter_message(
            text="you are about to start the procedure to add an event, do you want to continue?")

        dispatcher.utter_message(
            json_message={"requestForm": True}, text="hello")
        return []


class ActionAddEvent(Action):

    def name(self) -> Text:
        return "action_add_event"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("adding event")
        dispatcher.utter_message(text="adding event")
        dispatcher.utter_message(json_message={"requestForm": True})
        return []

class ActionAddTask(Action):
    def name(self) -> Text:
        return "action_add_task"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("adding task")
        dispatcher.utter_message(text="adding task")
        dispatcher.utter_message(json_message={"formtype": "add_task"})
        return []  


class ActionRemoveTask(Action):
    def name(self) -> Text:
        return "action_remove_task"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("removing task")
        dispatcher.utter_message(text="removing task")
        dispatcher.utter_message(json_message={"formtype": "remove_task"}) 
        return [] 

class ActionMoveTask(Action):
    def name(self) -> Text:
        return "action_move_task"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("moving task")
        dispatcher.utter_message(text="moving task")
        dispatcher.utter_message(json_message={"formtype": "move_task"})
        return [] 

class ActionResetAllSlots(Action):

    def name(self):
        return "action_reset_all_slots"

    def run(self, dispatcher, tracker, domain):
         return [AllSlotsReset()]
