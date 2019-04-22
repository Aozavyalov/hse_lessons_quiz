from typing import NoReturn

from telegram import Bot
from telegram.ext import Dispatcher, Filters, MessageHandler, Updater

from bot import *  # TODO add bot parts here


def register(dispatcher: Dispatcher) -> NoReturn:
    """ Register all handlers with bot dispatcher """
    # TODO register services as
    # service.register(dispatcher)
    dispatcher.add_handler(MessageHandler(Filters.text, start))


def run(token: str, workers: int=10) -> NoReturn:
    """ Application' entry point """

    updater = Updater(token, workers=workers)
    api = Bot(token)  # api is used to resolve name conflicts with main module
    register(updater.dispatcher)

    updater.start_polling()
    updater.idle()
