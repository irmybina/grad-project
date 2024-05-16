from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='О боте')],
                                     [KeyboardButton(text='Поиск по автору')]],
                           resize_keyboard=True,
                           one_time_keyboard=True,
                           input_field_placeholder='Выберите пункт...')

secondary = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='О боте')],
                                     [KeyboardButton(text='Поиск по автору')],
                                    [KeyboardButton(text='Закончить работу')]],
                           resize_keyboard=True,
                           one_time_keyboard=True,
                           input_field_placeholder='Выберите пункт...')

