#Import required dependencies first
import asyncio
import os
import sys
import time
from flask import Flask, request, jsonify
from telegram.ext import CommandHandler, Updater
from requests import get, post
from logging import basicConfig, getLogger, INFO
import spamwatch

server = Flask(__name__)

basicConfig(level=INFO)
log = getLogger()

# Checks if going to use environment mode.
ENV = bool(os.environ.get("ENV", False))
if ENV:
    ipAddr = get('https://api.ipify.org').text
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", None)
    MONGO_DB_URL = os.environ.get("MONGO_DB_URL", None)
    API_HOST = os.environ.get("API_HOST", ipAddr)
    LOG_CHAT = os.environ.get("LOG_CHAT", 777000)
else:
    import config
    TG_BOT_TOKEN = config.TG_BOT_TOKEN
    MONGO_DB_URL = config.MONGO_DB_URL
    API_HOST = config.API_HOST
    LOG_CHAT = config.LOG_CHAT

# Check if Bot API token is valid.
# If fails either the Bot Token is blank or invalid, it will exit with error code 1.
TG_BOT_API = f'https://api.telegram.org/bot{TG_BOT_TOKEN}/'
if TG_BOT_TOKEN == "":
    log.error("Bot Token is empty, exiting...")
    exit(1)
elif not TG_BOT_TOKEN:
    log.error("Bot Token is not defined, exiting...")
    exit(1)
elif TG_BOT_TOKEN == "123456:someRandomTextGoesHere":
    log.error("Is that token from config.example.py? Please change it.")
else:
    checkbot = get(TG_BOT_API + 'checkMe').json()
    if not checkbot['ok']:
        log.error("Bot Token is invalid or Telegram went down.")
        exit(1)
    else:
        log.info(
        f"[INFO] Logged in as @{username}, waiting for webhook requests...")

updater = Updater(token=BOT_TOKEN, workers=1)
dispatcher = updater.dispatcher

def start(_bot, update):
    """/start message for bot"""
    message = update.effective_message
    message.reply_text(
        "**Welcome to BanWatch API Key Manager Bot!**\n\nManage your API keys without leaving Telegram easily.\n\nNeed help? Join @BanWatchAPISupport.",
        parse_mode="markdown")

start_handler = CommandHandler("start", start)
help_handler = CommandHandler("help", help)
sourceCode = CommandHandler("source", source)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(sourceCode)
updater.start_polling()


@server.route("/", methods=['GET'])
# Just send 'Hello, world!' to tell that our server is up.
def helloWorld():
    return jsonify(ok="true", description="Hello, world!")

if __name__ == "__main__":
    # We can't use port 80 due to the root access requirement.
    port = 8080
    server.run(host="0.0.0.0", port=port)
