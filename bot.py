import openai
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from config import TELEGRAM_BOT_TOKEN, OPENAI_API_KEY
from database import create_table, add_user, get_users

openai.api_key = OPENAI_API_KEY

def start(update: Update, context: CallbackContext):
    user = update.message.from_user
    add_user(user.id, user.username, user.first_name, user.last_name)
    update.message.reply_text("Bienvenue, je suis votre prophète. Posez-moi une question!")

def chat(update: Update, context: CallbackContext):
    user_message = update.message.text
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Prédisez l'avenir de cette personne : {user_message}",
        temperature=0.7,
        max_tokens=100
    )
    prediction = response.choices[0].text.strip()
    update.message.reply_text(prediction)

def main():
    create_table()
    updater = Updater(TELEGRAM_BOT_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, chat))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
