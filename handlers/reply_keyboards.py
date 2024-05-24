from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove, FSInputFile
from aiogram.utils.media_group import MediaGroupBuilder

from keyboards import reply
from creds import main
from states import forms
from auth import main as auth


dp = main.dp


@dp.message()
async def special_msg(message: types.Message, state: FSMContext) -> None:
    cid = message.chat.id
    content = message.text

    # btn
    if content == "Реквізити":
        await message.answer("Моно банк 4441 1144 6869 9317")
    elif content == "Про проєкт":
        await message.answer("В цьому боті ви можете згенерувати картинки і отримати відповіді на свої питання")
    elif content == "Надіслати відгук":
        await message.answer("Введіть своє ім*я: ")
        await state.set_state(forms.RequestForm.wait_for_name)
    elif content == "chatGPT":
        await message.answer("Впишіть, що ви б хотіли дізнатись в мене: ")
        await state.set_state(forms.SimplePromptGPT.wait_for_prompt)
    elif content == "DALL-E":
        await message.answer("Впишіть, що ви б хотіли, об я намалював: ")
        await state.set_state(forms.SimplePromptGPT.wait_for_image)

