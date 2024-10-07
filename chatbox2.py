from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a new instance of a ChatBot
bot = ChatBot(
    'StandaloneBot',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',  # Add the MathematicalEvaluation logic adapter
        'chatterbot.logic.BestMatch',  # Add the BestMatch logic adapter
    ]
)

# Create a trainer
trainer = ChatterBotCorpusTrainer(bot)

# Train the bot on English language data
trainer.train('chatterbot.corpus.english')

# Basic greeting responses
basic_greetings = ['hello', 'hi', 'hey', 'how are you', 'good day']
response_to_greetings = 'Hello! How can I assist you today?'

while True:
    user_input = input('You: ')
    if user_input.lower() in basic_greetings:
        print('Bot:', response_to_greetings)
    elif user_input.lower() == 'exit':
        break
    elif user_input.lower()=='great job':
        print('thank you') 
    else:
        response = bot.get_response(user_input)
        print('Bot:', response)

