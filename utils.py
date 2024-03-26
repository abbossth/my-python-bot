import telebot
from telebot import types

# Helper function to generate inline keyboard markup
def generate_markup_languages():
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton(f"O'zbek Tili", callback_data=f"uz_latin")
    btn2 = types.InlineKeyboardButton(f"Ўзбек тили", callback_data=f"uz_kiril")
    btn3 = types.InlineKeyboardButton(f"Русский язык", callback_data=f"ru")
    markup.add(btn1, btn2, btn3)
    return markup

# Helper function to generate inline keyboard markup
def generate_markup(options, order_num):
    select_symbol = "⚪️"
    
    markup = types.InlineKeyboardMarkup(row_width=2)
    for option in options:
        markup.add(types.InlineKeyboardButton(text=f"{select_symbol} {option[2]}", callback_data=f"{order_num}_{option[0]}_none"))
    return markup

