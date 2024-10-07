"""
from chatterbot import ChatBot
import yaml

# Load the custom corpus data using yaml.safe_load
corpus_path = r"C:\Users\vrish\OneDrive\Desktop\output.yml"  # Replace with your file path

with open(corpus_path, 'r') as corpus_file:
    user_data = yaml.safe_load(corpus_file)

# Create a new instance of a ChatBot
bot = ChatBot('CustomTrainingBot')

# Function to get a user's password based on their username
def get_password(username):
    for user in user_data:
        if user['username'] == username:
            return user['password']
    return "User not found"

while True:
    user_input = input("Enter a username: ")
    if user_input == "exit":
        break

    response = get_password(user_input)
    print(response)

"""
from chatterbot import ChatBot
from chatterbot.storage import SQLStorageAdapter

# Create a new instance of a ChatBot
bot = ChatBot(
    'MySQLTerminalBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='mysql://root:vrishank@localhost:3306/chatbot',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch'
    ]
)

# Get a few responses from the bot
x=input('ask a question')
response1 = bot.get_response(x)
response2 = bot.get_response('What is 7 plus 7?')

print(response1)
print(response2)
