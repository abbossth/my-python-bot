import telebot
import asyncio
from config import BOT_TOKEN



def main():
    bot = telebot.TeleBot(BOT_TOKEN)
    @bot.message_handler(commands=['start', 'survey'])
    def start(message):
        bot.send_message(message.chat.id, message.text)
    bot.polling(non_stop=True, interval=0)


if __name__ == "__main__":
    print("Bot started...")
    asyncio.run(main())