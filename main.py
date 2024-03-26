import asyncio
from bot_logic import bot_logic
from db_setup import db_setup

def main():
    db_setup()
    bot_logic()


if __name__ == "__main__":
    print("Bot started...")
    asyncio.run(main())