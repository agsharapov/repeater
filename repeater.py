import os
from dotenv import load_dotenv
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

load_dotenv()
token = os.getenv('TOKEN')


def greeting(update, context):
    update.message.reply_text('Привет! Напиши мне любой текст (кроме команд),'
                              ' и я повторю его')


def repeat(update, context):
    update.message.reply_text(update.message.text)


def main():
    updater = Updater(token)
    updater.dispatcher.add_handler(
        CommandHandler('start', greeting)
    )
    updater.dispatcher.add_handler(
        MessageHandler(Filters.text & ~Filters.command, repeat)
    )
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
