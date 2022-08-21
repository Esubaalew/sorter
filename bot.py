
from typing import final
import telegram
from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from text import get_info
from nltk import word_tokenize
import os
telegram_bot_token =\
updater = Updater(token='5646540816:AAGh2djjpa7g_WHkkl3kG0-4wrjHPJEJPzw', use_context=True)
dispatcher = updater.dispatcher



# set up the introductory statement for the bot when the /start command is invoked
def start(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text='''
    
Hello there!!
Provide any  English text(contents of text must be all lowercase OR ALL UPPERCASE) and I will give you the sorted list of words in it.
    enter /help for all commands list
    enter /how to learn how to use the bot 
    '''
                                                   )

def help(update: Update, context: CallbackContext):
    update.message.reply_text("""USE THE FOLLOWING COMMANDS :-
/start - About me[bot]
/how - how to use bot
/help - for all commands list
/about - to know about my designer
    
	""")
def about(update: Update, context: CallbackContext):
    update.message.reply_text("""
My name is Esubalew Chekol.
I am not a developer/coder/programmer i am still learning to code.
I thank my groupmates, East(A), Ros(H), lead(L)  and bek(B)] of  my IS dept.
Dear A,H,L and B I really love you all.

በጣም እወዳችኋለሁ!!
___________ከ እሱባለው ቸኮል | from Esubalew_____________________




   


    
	""")
def how(update: Update, context: CallbackContext):
    update.message.reply_text("""

The purpose of this bot is to handle any text document and send the sorted list back to the user.\n
To use the bot, just send any text and it will automaticaly send the sorted list of words and numbers[if any].\n
If there are any special characters in your text, this bot will filter them out and these characters will not be included in the list.\n 
If there are number in the list, these numbers will be considered as any other word.

NOTE THAT THE INPUT TEXT MUST BE WRITTEN IN ALL LOWERCASE OR ALL UPPERCASE!!

___________ከ እሱባለው ቸኮል | from Esubalew_____________________

	""")
# obtain the information of the word provided and format before presenting.
def getSorted(update, context):
    # get the word info
    fulltext = get_info(update.message.text)
    words=word_tokenize(fulltext)
    words.sort()

    
    update.message.reply_text(


       [
            word.lower() for word in words if word.isalnum()]


        )

dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('how', how))
updater.dispatcher.add_handler(CommandHandler('about', about))
dispatcher.add_handler(MessageHandler(Filters.text, getSorted))
updater.start_webhook(listen="0.0.0.0",
                      port=int(os.environ.get('PORT', 5000)),
                      url_path='5646540816:AAGh2djjpa7g_WHkkl3kG0-4wrjHPJEJPzw',
                      webhook_url=  + '5646540816:AAGh2djjpa7g_WHkkl3kG0-4wrjHPJEJPzw'
                      )