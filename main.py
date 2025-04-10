from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from dotenv import load_dotenv
import os

from handlers.register import register_command, login_command
from handlers.predict import predict_command
from handlers.admin import admin_command
from database import init_db

load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Initialisation de la base de données
init_db()

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

# Handlers de base
app.add_handler(CommandHandler("register", register_command))
app.add_handler(CommandHandler("login", login_command))
app.add_handler(CommandHandler("predict", predict_command))
app.add_handler(CommandHandler("admin", admin_command))

# Démarrer le bot
print("🤖 Bot prophète andruze  en ligne...")
app.run_polling()
