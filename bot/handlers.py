from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram import Router, F
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import bot.keyboards as kb
import bot.search as search

router = Router()

class FindAuthors(StatesGroup):
    author = State()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Добрый день. Я спарсила несколько страниц с сайта elibrary.ru в качестве дипломного проекта. В этом боте вы можете увидеть количество публикаций, цитирований и индекс Хирша авторов, фамилия которых начинается на букву А.", reply_markup=kb.main)


# @router.message(Command('help'))
# async def cmd_help(message: Message):
#     await message.answer("I cn't help you right now")

# @router.message(Command('find_author'))
# async def cmd_find_author(message: Message):
#     await message.answer("Please enter author's name")

@router.message(F.text == "Поиск по автору")
async def cmd_find_author(message: Message, state: FSMContext):
    await state.set_state(FindAuthors.author)
    await message.answer("Пожалуйста, введите имя автора")

@router.message(FindAuthors.author)
async def cmd_find_author_name(message: Message, state: FSMContext):
    await state.update_data(author=message.text)
    authorsName = await state.get_data()
    data = search.find_row(authorsName['author'])
    if data == "":
        await message.answer(f"К сожалению, автор {authorsName['author']} не найден")
    while len(data) > 0:
        await message.answer(f"{data[0:4000]}")
        data = data[4000:]
    await message.answer("Поиск завершён", reply_markup=kb.secondary)
    await state.clear()

@router.message(F.text == "Закончить работу")
async def cmd_find_author(message: Message):

    await message.answer("Чтобы начать новую сессию нажмите /start")

@router.message(F.text == "О боте")
async def cmd_find_author(message: Message):
    await message.answer("Это моя выпускная квалификационная работа")
