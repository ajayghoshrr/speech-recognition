#chat bot - first run - you have to give the training data - and train it first. Download the training data from Github.
#second time no need for train it again, you can comment the training code snippet.


from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
bot = ChatBot('Bot')
bot.set_trainer(ListTrainer)
#training snippet start
for files in os.listdir(r"C:/Python36-32/projects/day1/chatterbot-corpus-master/chatterbot-corpus-master/chatterbot_corpus/data/english/"):
    data = open("C:/Python36-32/projects/day1/chatterbot-corpus-master/chatterbot-corpus-master/chatterbot_corpus/data/english/" + files, 'r').readlines()
    bot.train(data)
#training set ends----

while True:
    message = input('You ::')
    if message.strip()!='Bye':
        reply = bot.get_response(message)
        print('ChatBot ::', reply)
    if message.strip() == 'Bye':
        print('ChatBot :: Bye')
        break

