# Open Source Chatbot & Automation System

This project is a simple open-source chatbot engine combined with automation triggers.
It allows you to:
- Parse user input using intent rules
- Respond with predefined messages
- Trigger automation scripts when specific intents are detected

## Features
- Rule-based chatbot with JSON-configurable intents
- Easy to extend
- CLI for quick usage
- Ideal as a starter project for automation workflows

## Usage

### Install dependencies
```
pip install -r requirements.txt
```

### Run the chatbot CLI
```
python cli.py
```

Type a message and see the bot respond.

## Structure
```
open_source_chatbot_automation/
│
├── bot/
│   ├── chatbot.py
│   └── intents.json
│
├── automation/
│   └── autoscript.py
│
├── cli.py
└── requirements.txt
```

## License
MIT License
