from aiogram.utils import executor  # для запуска бота в режиме long_polling (постоянный опрос сервера)
from create_bot import dp
from handlers import client, admin, other
from data_base import pgsql_db
import os


async def on_startup(_):
    print('Бот вышел в онлайн')
    pgsql_db.pga_start()


client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

