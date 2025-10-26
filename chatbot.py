import json
import os

class ChatBot:
    def __init__(self):
        intents_path = os.path.join(os.path.dirname(__file__), "intents.json")
        with open(intents_path, "r", encoding="utf-8") as f:
            self.intents = json.load(f)

    def get_response(self, user_input):
        user_input = user_input.lower()
        for item in self.intents["intents"]:
            for pattern in item["patterns"]:
                if pattern.lower() in user_input:
                    return item["response"], item.get("action")
        return "I'm not sure how to respond to that.", None
