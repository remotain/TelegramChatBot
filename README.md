# Telegram Chatbot project

This project combine different concepts learned about [Natural Language Processing|https://www.coursera.org/learn/language-processing] into a simple dialog chatbot capable of:

* Answering user software-programming-related questions (using StackOverflow dataset);
* Chit-chatting and simulating a dialogue on all non-programming-related questions.

The chit-chat mode uses a pre-trained Neural Network Engine available from [ChatterBot|https://chatterbot.readthedocs.io/en/stable/].

## Install requirements

The project is developed entirely in Python3 and depends on some external libraries. Once you cloned the git repository on your local computer, please follow these instructions to install the dependencies:

```
python3 -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Telegram token

The chatbot is integrated with the Telegram messenger and need a token to run.

Talk to @BotFather in Telegram. The command "/newbot" will create a bot for you. You will be prompted to enter a name and a username for your bot. After that, you will be given a token.

Then you can activate your chatbot by typing:

```
python3 main_bot.py --token=YOUR_TOKEN
```

You can now talk to this bot in Telegram (make sure to talk via the messenger, not via your console).