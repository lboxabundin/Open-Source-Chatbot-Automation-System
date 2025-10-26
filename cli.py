from bot.chatbot import ChatBot
from automation.autoscript import run

bot = ChatBot()

print("Chatbot ready. Type something (Ctrl+C to exit).")

while True:
    try:
        msg = input("You: ")
        response, action = bot.get_response(msg)
        print("Bot:", response)
        if action == "run_script":
            run()
    except KeyboardInterrupt:
        print("\nExiting...")
        break
