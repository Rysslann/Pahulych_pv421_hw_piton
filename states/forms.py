import json

from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from creds import main
from keyboards import reply
from ai import main as ai

dp = main.dp


class RegistrationStates(StatesGroup):
    wait_for_feedback = State()


class SimplePromptGPT(StatesGroup):
    wait_for_prompt = State()
    wait_for_image = State()


class RequestForm(StatesGroup):
    wait_for_name = State()
    wait_for_email = State()
    wait_for_comment = State()


class AddNewAdmin(StatesGroup):
    wait_for_admin_id = State()


class MassSending(StatesGroup):
    wait_for_content_msg = State()


@dp.message(SimplePromptGPT.wait_for_prompt)
async def send_prompt(msg: types.Message, state: FSMContext):
    wait_msg = await main.bot.send_message(msg.from_user.id, 'Генерується...')
    result = await ai.test_send_prompt(msg.text)
    if result:
        await main.bot.delete_message(msg.from_user.id, wait_msg.message_id)
        await msg.answer(result.choices[0].message.content)
        await state.clear()


@dp.message(SimplePromptGPT.wait_for_image)
async def generate_image_link(msg: types.Message, state: FSMContext):
    wait_msg = await main.bot.send_message(msg.from_user.id, 'Генерується...')
    result = ai.generate_img(msg.text)

    if result:
        await main.bot.delete_message(msg.from_user.id, wait_msg.message_id)
        await main.bot.send_photo(msg.from_user.id, result)
        await state.clear()

@dp.message(RequestForm.wait_for_name)
async def get_name_req_form(msg: types.Message, state: FSMContext):
    await state.update_data(name=msg.text)
    await msg.answer("Введіть вашу пошту: ")
    await state.set_state(RequestForm.wait_for_email)


@dp.message(RequestForm.wait_for_email)
async def get_email_req_form(msg: types.Message, state: FSMContext):
    await state.update_data(email=msg.text)
    await msg.answer("Введіть ваш коментар: ")
    await state.set_state(RequestForm.wait_for_comment)


@dp.message(RequestForm.wait_for_comment)
async def get_comment_req_form(msg: types.Message, state: FSMContext):
    await state.update_data(comment=msg.text)
    with open("data/requests.json", "r", encoding="utf-8") as file:
        all_req = json.load(file)
        req_data = await state.get_data()
        all_req.append(req_data)
    with open("data/requests.json", "w", encoding="utf-8") as f:
        json.dump(all_req, f)

    await state.clear()
    await msg.answer("Дякуємо! За ваш коментар!", reply_markup=reply.main_menu())
