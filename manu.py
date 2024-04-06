import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram.types.keyboard_button import KeyboardButton
from aiogram.types.reply_keyboard_remove import ReplyKeyboardRemove
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.types.inline_keyboard_button import InlineKeyboardButton

# Bot token can be obtained via https://t.me/BotFather
TOKEN = "6938585575:AAH8ZQEwDhhWzhG0e9epc-iOLs8OfKHulqU"

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()
bot = Bot(TOKEN)


# REPLY KEYBOARD
def r_main_menu():
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Про проект")],
            [KeyboardButton(text="Реквізити"), KeyboardButton(text="Про мене")],
            [KeyboardButton(text="Про вас")]
        ],
        resize_keyboard=True
    )
    return kb


def r_who_you():
    kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Пес"), KeyboardButton(text="Норм чувак"),
             KeyboardButton(text="Затрудняюсь відповісти")],
            [KeyboardButton(text="Назад")]
        ],
        resize_keyboard=True
    )
    return kb


# INLINE KEYBOARD
def i_who_am_I():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Як звати?", callback_data="name")],
            [InlineKeyboardButton(text="Де живу?", callback_data="city")],
            [InlineKeyboardButton(text="Номер картки?", callback_data="money")],
            [InlineKeyboardButton(text="Скільки років?", callback_data="years"),
             InlineKeyboardButton(text="Стать?", callback_data="sex")],
            [InlineKeyboardButton(text="Про вас?", callback_data="you")]
        ]
    )

@dp.callback_query(lambda c: c.data)
async def process_callback(callback_query: types.CallbackQuery):
    data = callback_query.data
    cid = callback_query.from_user.id
    msg_id = callback_query.message.message_id
    if data == "name":
        # await bot.send_message(cid, "Program Python: ")
        await bot.edit_message_text(
            text="Руслан, ось мій інстаграм: https://www.instagram.com/rysslann36/ ",
            chat_id=cid,
            message_id=msg_id,
            reply_markup=i_who_am_I(),
            disable_web_page_preview=True,
        )
    elif data == "city":
        await bot.edit_message_text(
            text="Дрогобич",
            chat_id=cid,
            message_id=msg_id,
            reply_markup=i_who_am_I(),
        )
    elif data == "money":
        await bot.edit_message_text(
            text="4441 1144 6869 9317",
            chat_id=cid,
            message_id=msg_id,
            reply_markup=i_who_am_I(),
        )
    elif data == "years":
        await bot.edit_message_text(
            text="27",
            chat_id=cid,
            message_id=msg_id,
            reply_markup=i_who_am_I(),
        )
    elif data == "sex":
        await bot.edit_message_text(
            text="чоловіча",
            chat_id=cid,
            message_id=msg_id,
            reply_markup=i_who_am_I(),
        )
    elif data == "you":
        await bot.delete_message(chat_id=cid, message_id=msg_id)
        await bot.send_message(cid, "Ви відкрили підменю для вибору хто ви ↓", reply_markup=r_who_you())
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!", parse_mode="HTML", reply_markup=r_main_menu())


@dp.message()
async def special_msg(message: types.Message) -> None:
    cid = message.chat.id
    content = message.text
    print("__test", content)
    print("__id", cid)

    if content == "/secret":
        await message.answer("You activeted secret modу. Which does nothing", reply_markup=ReplyKeyboardRemove())
    elif content == "Реквізити":
        await message.answer("<b>Кинь пару копійок</b>", parse_mode="HTML")
        await message.answer("<b>4441 1144 6869 9317</b>", parse_mode="HTML")
    elif content == "Про проект":
        await message.answer("Поки що він не робить нічого корисного")
    elif content == "Про мене":
        await message.answer("Що саме вас цікавить?", reply_markup=i_who_am_I())
    elif content == "Про вас":
        await message.answer("А ви хто? Оберіть в під меню ↓", reply_markup=r_who_you())
    elif content == "Пес":
        await message.answer("Ти як сюда попав?")
    elif content == "Норм чувак":
        await message.answer("Є сумніви")
    elif content == "Затрудняюсь відповісти":
        await message.answer("Норм чувак")
    elif content == "Назад":
        await message.answer("Ви вернулись в головне меню ↓ ", reply_markup=r_main_menu())


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
