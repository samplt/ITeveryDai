from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters

#import telegram

from echo.config import TG_TOKEN


def do_start (bot: Bot, update: Update):
    bot.send_message(
        chat_id = update.message.chat_id,
        text = "Privet. Otprav' mne chto-nibud'"
    )


def do_echo(bot: Bot, update: Update):
    text = update.message.text
    bot.send_message(
        chat_id=update.message.chat_id,
        text=text
    )


def main():
    bot = Bot(
        token=TG_TOKEN,
    )
    updater = Updater(
        bot=Bot
    )

    start_handler = CommandHandler("start", do_start)
    message_handler = MessageHandler(Filters.text, do_echo)

    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(message_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()