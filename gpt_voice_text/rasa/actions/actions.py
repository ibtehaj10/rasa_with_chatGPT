from typing import Any, Dict, List, Text

from rasa_sdk import Action, Tracker
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher
import openai
from config import apikey





openai.api_key = apikey

def openais(message):
    res = openai.Completion.create(
                model="text-davinci-003",
                prompt=message,
                max_tokens=50,
                temperature=0.6,
            )
    r = res.choices[0].text 
    return r

class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        txt=tracker.latest_message.text
        repl = openais(txt)

        # tell the user they are being passed to a customer service agent
        dispatcher.utter_message(text=repl)
        
    


class ActionCustomFallback(Action):
    def name(self) -> Text:
        return "action_custom_fallback"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        txt=(tracker.latest_message)['text']
        repl = openais(txt)

        # tell the user they are being passed to a customer service agent
        dispatcher.utter_message(text=repl)
     
        return [ UserUtteranceReverted()]