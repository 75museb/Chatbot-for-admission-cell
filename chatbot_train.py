from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

def setup():
    chatbot = ChatBot('Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    trainer='chatterbot.trainers.ListTrainer')
    for file in os.listdir('D:/DYP-ATU Chabot/ai properties.yaml/'):
        convData = open(r'D:/DYP-ATU Chabot/dypatudata2.csv/' + file, encoding='latin-1').readlines()
        chatbot.set_trainer(ListTrainer)
        chatbot.train(convData)
print("Training completed")
    

setup()
