import logging
import sys
from argparse import ArgumentParser, Namespace

from bot import run
from bd import init_db
from config import TOKENS, BD_CREDENTIALS

LOGGING_LEVELS = {
    'TEST': logging.DEBUG,
    'PROD': logging.INFO
}

def parse_argv() -> Namespace:
    parser = ArgumentParser(description="Starts telegram bot for lessons materials")
    parser.add_argument('action', type=str,
                        help="run|init_db")
    parser.add_argument('--token', '-t', type=str, default="TEST",
                        help="api token name (from config) for access to bot")
    parser.add_argument('--workers', '-w', type=int, default=10,
                        help="number of workers for running bot")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_argv()
    if args.action == "init_db":
        init_db(BD_CREDENTIALS)
    elif args.action == "run":
        run(
            token=TOKENS.get(args.token.upper(), TOKENS["TEST"]),
            logger_level=LOGGING_LEVELS.get(args.token.upper(), logging.DEBUG),
            workers=args.workers
        )
    else:
        print(f"Wrong command: {args.action}", file=sys.stderr)
