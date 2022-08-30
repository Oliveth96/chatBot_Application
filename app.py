from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

"""
A module that defines and trains a chatBot
"""


"""
This create the ChatBot application
"""
app = Flask(__name__)

englishBot = ChatBot('ChatterBot', storage_adapter='chatterbot.storage.SQLStorageAdapter')
trainer = ChatterBotCorpusTrainer(englishBot)
trainer.train('chatterbot.corpus.english')


'''
Defines the function home, that renders the .html document.
'''


@app.route('/')
def home():
    return render_template('chatIndex.html')


'''
Defines a function for the bot to receive responses/text messages
'''


@app.route('/get')
def botResponses():
    usersText = request.args.get('msg')
    return str(englishBot.get_response(usersText))


if __name__ == '__main__':
    app.run()
