from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from app.generators import generate_response

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Hi, I\'m Mori. How can I help you today?')

@router.message()
async def handle_message(message: Message):
    response_text = await generate_response(message.text)
    print(response_text.choices[0].message.content)
    await message.answer(response_text.choices[0].message.content)