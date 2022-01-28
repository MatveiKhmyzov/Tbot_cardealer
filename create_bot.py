# базовый класс бота; диспетчер простых обновлений (сообщения, отредактированные
# сообщения, сообщения канала)
from aiogram import Bot, Dispatcher
from utils.config import TOKEN
# класс хранит данные в оперативной памяти
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token=TOKEN) # экземпляр бота
dp = Dispatcher(bot, storage=storage) # экземпляр диспетчера
