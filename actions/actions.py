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

class ActionConfirmAddTask(Action):

    def name(self) -> Text:
        return "action_confirm_add_task"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("confirm adding task")

        dispatcher.utter_message(
            text="you are about to start the procedure to add a task, do you want to continue?")

class ActionConfirmRemoveTask(Action):

    def name(self) -> Text:
        return "action_confirm_remove_task"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("confirm removing task")

        dispatcher.utter_message(
            text="you are about to start the procedure to remove a task, do you want to continue?")

class ActionConfirmUpdateTask(Action):

    def name(self) -> Text:
        return "action_confirm_update_task"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("confirm updating task")

        dispatcher.utter_message(
            text="you are about to start the procedure to update a task, do you want to continue?")

class ActionConfirmMoveTask(Action):

    def name(self) -> Text:
        return "action_confirm_move_task"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("confirm moving task")

        dispatcher.utter_message(
            text="you are about to start the procedure to move a task, do you want to continue?")


class ActionAddEvent(Action):

    def name(self) -> Text:
        return "action_add_event"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("adding event")
        dispatcher.utter_message(text="adding event")
        dispatcher.utter_message(json_message={"formtype": "add_event"})
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

class ActionUpdateTask(Action):
    def name(self) -> Text:
        return "action_update_task"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("update task")
        dispatcher.utter_message(text="updating task")
        dispatcher.utter_message(json_message={"formtype": "update_task"})
        return [] 

class ActionResetAllSlots(Action):

    def name(self):
        return "action_reset_all_slots"

    def run(self, dispatcher, tracker, domain):
         return [AllSlotsReset()]
