from aiogram import types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from aiogram.utils.markdown import hbold
from creds import main
from keyboards import reply
from auth import main as auth
import pandas as pd
import requests
import pdfkit
import qrcode

dp = main.dp


@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!", parse_mode="HTML")
    await message.answer('Hello World! I am live!', reply_markup=reply.main_menu())


@dp.message(Command("poll"))
async def poll(msg: types.Message):
    cid = msg.from_user.id
    await main.bot.send_poll(
        chat_id=cid,
        question="Test Question",
        options=["One", "Two"],
        type="regular",
        is_anonymous=False,
        allows_multiple_answers=True
    )


@dp.message(Command("admin"))
async def welcome_admin(msg: types.Message):
    print()
    if auth.is_admin(msg.from_user.id):
        await msg.answer("Вітаємо у режимі адміністратора", reply_markup=reply.admin_main())
    else:
        await msg.answer("You haven`t access!", reply_markup=reply.main_menu())


# @dp.message(Command("exel"))
# async def generate_exel(msg: types.Message):
#     data={
#         'Name': ["John", "Jane", "Peter"],
#         "age": [31, 21, 15],
#         'Posotion':["Engineer", "doctor", "Designer"],
#         'Data': ["911", "22", "321"]
#     }
#     df = pd.DataFrame(data)
#
#     writer = pd.ExcelWriter('files/expl.xlsx', engine='openpyxl')
#
#     df.to_excel(writer, sheet_name="Users")
#
#     writer._save()


@dp.message(Command("exel"))
async def generate_exel(msg: types.Message):
    products = requests.get("https://fakestoreapi.com/products")
    products = products.json()
    data = {
        'Title': [],
        'Price': [],
        'Description': [],
        'Category': [],
        'Image': []
    }

    for products in products:
        data["Title"].append(products["title"])
        data["Price"].append(products["price"])
        data["Description"].append(products["description"])
        data["Category"].append(products["category"])
        data["Image"].append(products["image"])

    df = pd.DataFrame(data)

    writer = pd.ExcelWriter('files/expl.xlsx', engine='openpyxl')

    df.to_excel(writer, sheet_name="Users")

    writer._save()

    await main.bot.send_document(chat_id=msg.from_user.id,
                                 document=FSInputFile("files/expl.xlsx"))


@dp.message(Command("pdf"))
async def generate_pdf(msg: types.Message):
    html_content = """
    <!DOCTYPE html>
<html>
<head>
    <title>Page Title</title>
</head>
<body>
    <h1>This is a Heading</h1>
    <p>This is a paragraph.</p>
</body>
</html>
    """

    path_wkthmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)
    output_file = 'files/tpl.pdf'
    pdfkit.from_string(html_content, output_file, configuration=config)

    await  main.bot.send_document(chat_id=msg.from_user.id,
                                  document=FSInputFile("files/tpl.pdf"))


@dp.message(Command("qr"))
async def generate_qr(msg: types.Message):
    # Create a QR code object with a larger size and higher error correction
    qr = qrcode.QRCode(version=3, box_size=20, border=10, error_correction=qrcode.constants.ERROR_CORRECT_H)

    # Define the data to be encoded in the QR code
    data = "https://medium.com/@rahulmallah785671/create-qr-code-by-using-python-2370d7bd9b8d"

    # Add the data to the QR code object
    qr.add_data(data)

    # Make the QR code
    qr.make(fit=True)

    # Create an image from the QR code with a black fill color and white background
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code image
    img.save("files/qr_code_with_logo.png")

    await main.bot.send_document(chat_id=msg.from_user.id,
                                 document=FSInputFile("files/qr_code_with_logo.png"))
