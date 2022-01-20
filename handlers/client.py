from aiogram import types, Dispatcher
from create_bot import bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove

async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Беспроблемной эксплуатации', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/Car_dealerBot')


async def dealer_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вс-Чт с 9:00 до 20:00, Пт-Сб с 10:00 до 23:00')


async def dealer_destination_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'ул. Сухаревское шоссе 24', reply_markup=ReplyKeyboardRemove())


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(dealer_open_command, commands=['Режим_работы'])
    dp.register_message_handler(dealer_destination_command, commands=['Адрес'])
