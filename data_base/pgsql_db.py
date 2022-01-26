import psycopg2 as ps
from data_base.config import host, user, password
from create_bot import bot


def pga_start():
    global base, cur
    base = ps.connect(user=user,
                      password=password,
                      host=host)
    cur = base.cursor()
    if base:
        print('Database connected OK!')
    cur.execute('CREATE TABLE IF NOT EXISTS cars(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT);')
    base.commit()


async def data_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO cars VALUES(%s,%s,%s,%s)', tuple(data.values()))
        base.commit()


async def pga_read(message):
    cur.execute('SELECT * FROM cars')
    cars_records = cur.fetchall()
    for ret in cars_records:
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')
