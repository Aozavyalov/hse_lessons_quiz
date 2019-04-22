import logging
from argparse import ArgumentParser, Namespace

from bot import run
from config import TOKEN
from database.tools import init_db


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)


def parse_argv() -> Namespace:
    parser = ArgumentParser(description="Telegram bot for lessons materials")
    parser.add_argument('action', type=str, help="run|init_db")
    parser.add_argument('--workers', '-w', type=int, default=10,
                        help="number of workers to run the bot")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_argv()

    if args.action == "init_db":
        init_db()
    elif args.action == "run":
        run(token=TOKEN, workers=args.workers)
    else:
        logging.fatal("Invalid action: %s", args.action)
        exit(1)
