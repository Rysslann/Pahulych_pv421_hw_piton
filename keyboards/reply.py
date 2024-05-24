from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram.types.keyboard_button import KeyboardButton


# REPLY KEYBOARD
def main_menu():
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="chatGPT"),
                KeyboardButton(text="DALL-E"),
                KeyboardButton(text="Згенерувати котиків")
            ],
            [
                KeyboardButton(text="Про проєкт"),
                KeyboardButton(text="Реквізити"),
                KeyboardButton(text='Надіслати відгук')
            ],

        ],
        resize_keyboard=True
    )
    return kb



