from flask import Flask, request, render_template_string
from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters
from text import get_info
from nltk import word_tokenize
import os

# Initialize Flask app
app = Flask(__name__)

# Initialize the Telegram Bot
TOKEN = '5646540816:AAGh2djjpa7g_WHkkl3kG0-4wrjHPJEJPzw'
bot = Bot(token=TOKEN)

# Initialize dispatcher
dispatcher = Dispatcher(bot, None, workers=0, use_context=True)

# Define command handlers
def start(update: Update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text='''
    Hello there!!
    Provide any English text (contents of text must be all lowercase OR ALL UPPERCASE) and I will give you the sorted list of words in it.
    Enter /help for all commands list
    Enter /how to learn how to use the bot
    ''')

def help(update: Update, context):
    update.message.reply_text("""USE THE FOLLOWING COMMANDS :-
/start - About me[bot]
/how - how to use bot
/help - for all commands list
/about - to know about my designer
    """)

def about(update: Update, context):
    update.message.reply_text("""
My name is Esubalew Chekol.
I am not a developer/coder/programmer I am still learning to code.
I thank my groupmates, East(A), Ros(H), lead(L), and Bek(B) of my IS dept.
Dear A, H, L, and B, I really love you all.
    በጣም እወዳችኋለሁ!!
    ___________ከ እሱባለው ቸኮል | from Esubalew_____________________
    """)

def how(update: Update, context):
    update.message.reply_text("""
The purpose of this bot is to handle any text document and send the sorted list back to the user.\n
To use the bot, just send any text and it will automatically send the sorted list of words and numbers [if any].\n
If there are any special characters in your text, this bot will filter them out and these characters will not be included in the list.\n 
If there are numbers in the list, these numbers will be considered as any other word.
NOTE THAT THE INPUT TEXT MUST BE WRITTEN IN ALL LOWERCASE OR ALL UPPERCASE!!
___________ከ እሱባለው ቸኮል | from Esubalew_____________________
    """)

def getSorted(update: Update, context):
    # Get the word info
    fulltext = get_info(update.message.text)
    words = word_tokenize(fulltext)
    words.sort()
    sorted_words = [word.lower() for word in words if word.isalnum()]
    
    update.message.reply_text(sorted_words)

# Add handlers to dispatcher
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('how', how))
dispatcher.add_handler(CommandHandler('about', about))
dispatcher.add_handler(MessageHandler(Filters.text, getSorted))

# Define webhook route
@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(), bot)
    dispatcher.process_update(update)
    return "ok"

# Set webhook
@app.route('/set_webhook', methods=['GET', 'POST'])
def set_webhook():
    webhook_url = f"https://sorteer-i0qdavrp.b4a.run/{TOKEN}"
    bot.set_webhook(webhook_url)
    return f"Webhook set to {webhook_url}"

# Define the 'about' route with proper HTML formatting
@app.route('/about', methods=['GET'])
def do_about():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>About Esubalew</title>
    </head>
    <body>
        <h1>About Me</h1>
        <p>My name is Esubalew Chekol.</p>
        <p>I am not a developer/coder/programmer; I am still learning to code.</p>
        <p>I thank my groupmates, East(A), Ros(H), lead(L), and Bek(B) of my IS department.</p>
        <p>Dear A, H, L, and B, I really love you all.</p>
        <p>በጣም እወዳችኋለሁ!!</p>
        <p>___________ከ እሱባለው ቸኮል | from Esubalew_____________________</p>
    </body>
    </html>
    """
    return render_template_string(html_content)

@app.route('/', methods=['GET'])
def do_about():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>About Esubalew</title>
    </head>
    <body>
        <h1>About Me</h1>
        <p>My name is Esubalew Chekol.</p>
        <p>I am not a developer/coder/programmer; I am still learning to code.</p>
        <p>I thank my groupmates, East(A), Ros(H), lead(L), and Bek(B) of my IS department.</p>
        <p>Dear A, H, L, and B, I really love you all.</p>
        <p>በጣም እወዳችኋለሁ!!</p>
        <p>___________ከ እሱባለው ቸኮል | from Esubalew_____________________</p>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
